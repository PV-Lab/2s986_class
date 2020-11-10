import paramiko
import sys
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient


def ssh_connect(OT2_IP):
    """Call to set connection with remote client."""

    try:
        ssh = SSHClient()
        ssh.load_system_host_keys()
        # ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(OT2_IP, ##IP addresss of OT-2
                    username='root', 
                    key_filename = r'C:\Users\SMART\ot2_ssh_key')
                    ## the authentication file location
    except (paramiko.AuthenticationException,
            paramiko.ssh_exception.NoValidConnectionsError) as e:
        sys.exit(colored("> {}".format(e), 'red'))
    return ssh

def ssh_run_remote_command(OT2_IP, cmd):
        ssh = ssh_connect(OT2_IP)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
#         if error:
#             raise Exception('There was an error during the runtime: {}'.format(error))
        ssh.close()
        return [out, error]
    
def ssh_file_transfer(OT2_IP, local_dir, remote_dir, put_or_get):
        ssh = ssh_connect(OT2_IP)
        if put_or_get == 'put':
            with SCPClient(ssh.get_transport()) as scp:
                scp.put(local_dir, remote_dir)
        elif put_or_get == 'get':
            with SCPClient(ssh.get_transport()) as scp:
                scp.get(remote_dir, local_dir)
        else:
            print("Need to tell me if 'put' (upload) or 'get'(download) from the remote directory")
        
        ssh.close()
        return None

def ssh_take_an_image(OT2_IP, image_saving_name):
    #image_name ='image.jpg'
    ##ffmpeg -f video4linux2 -i /dev/v4l/by-id/usb-0c45_USB_camera-video-index0 -vframes 2 test%3d.jpeg
    #cmd_to_execute = 'ffmpeg -y -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:10 -frames 1 /data/user_storage/'+image_name
    image_name = 'image%d.jpg'
    cmd_to_execute = 'ffmpeg -y -f video4linux2 -s 640x480 -i /dev/video0 -vframes 3 /data/user_storage/'+image_name
    ssh_run_remote_command(OT2_IP, cmd_to_execute)
    remote_dir = '/data/user_storage/image3.jpg'       
    if image_saving_name[-4:] == '.jpg':
        local_dir  = '.\\data\\'+image_saving_name
        ssh_file_transfer(OT2_IP, local_dir, remote_dir, 'get')
        
        
def transfer_and_simulate_protocol(OT2_IP, csv_name, protocol_name):
    local_src  = ".\\"+protocol_name #file path at local computer 
    remote_des = "/data/"+protocol_name #file path at remote Pi
    ssh_file_transfer(OT2_IP, local_src, remote_des, 'put')

    local_src  = ".\\data\\"+csv_name#file path at local computer 
    remote_des = "/data/user_storage/color_test.csv"#file path at remote Pi
    ssh_file_transfer(OT2_IP, local_src, remote_des, 'put')
        
    cmd_to_execute = 'cd /data/\n'+\
                     'pwd\n'+\
                     'python -m opentrons.simulate /data/'+protocol_name #protocol_name= 'color_mixing.py'
    out, error = ssh_run_remote_command(OT2_IP, cmd_to_execute)
    print(out)
    print(error)
    
    if error:
        raise Exception('There was an error during the runtime: {}'.format(error))
    return None
    
    
def run_protocol(OT2_IP, protocol_name):
    cmd_to_execute = 'cd /data/\n'+\
                     'pwd\n'+\
                     'python -m opentrons.execute /data/'+protocol_name #protocol_name= '/data/color_mixing.py'
    out, error = ssh_run_remote_command(OT2_IP, cmd_to_execute)
    print(out)
    print(error)
    if error:
        raise Exception('There was an error during the runtime: {}'.format(error))

    return None
