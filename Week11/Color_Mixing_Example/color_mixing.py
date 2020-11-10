from opentrons import protocol_api
import pandas as pd 

metadata = {
    'protocolName': 'Color Liquid Mixing',
    'author': 'Zhe Liu',
    'source': 'Self Written',
    'apiLevel': '2.7'
    }

def run(protocol: protocol_api.ProtocolContext):
    #if not protocol.is_simulating():
    protocol.home()
    # define Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    pipette = protocol.load_instrument('p300_single_gen2', mount='left', tip_racks=[tiprack])

    # define Labware
    colorA_reservoir  =  protocol.load_labware('opentrons_96_tiprack_300ul', 9)
    colorBC_reservoir =  protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    mixing_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 4)
    dispense_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    water_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 8)
    cleaning_well = protocol.load_labware('corning_96_wellplate_360ul_flat', 7)
    
    # define Source Color Positions
    colorA_position = colorA_reservoir['F8']
    colorA_tip_position = tiprack['B1']

    colorB_position = colorBC_reservoir['A2']
    colorB_tip_position = tiprack['B2']

    colorC_position = colorBC_reservoir['E7']
    colorC_tip_position = tiprack['B3']

    
    # the example code below would go here, inside the run function
    
    df = pd.read_csv('/data/user_storage/color_test.csv')
    print(df.columns.values)
    colorA_amt = df.values[:,0]
    print(colorA_amt)
    colorB_amt = df.values[:,1]
    print(colorB_amt)
    colorC_amt = df.values[:,2]
    print(colorC_amt)
    dispense_position = df.values[:,3]
    print(dispense_position)
    
#     pipette.pick_up_tip(tiprack['C1'])
#     for i in range(len(dispense_position)):
#         pipette.aspirate(270, water_well['C5']) 
#         pipette.dispense(270, mixing_plate[dispense_position[i]].top(5), rate=0.5)
#     pipette.drop_tip(tiprack['C1'])
    
    
    for amt, src_pos, tip_pos in zip([colorA_amt, colorB_amt, colorC_amt],
                                     [colorA_position, colorB_position, colorC_position],
                                     [colorA_tip_position, colorB_tip_position, colorC_tip_position]):
        pipette.pick_up_tip(tip_pos)
        amt_sum = sum(amt)
        #pipette.aspirate(amt_sum, src_pos.top(-35), rate=0.5)
        for i in range(len(dispense_position)):
            pipette.aspirate(55, water_well['C5']) 
            pipette.aspirate(amt[i], src_pos.top(-35), rate=0.5)
            pipette.air_gap(10)
            pipette.dispense(amt[i]+55+10, mixing_plate[dispense_position[i]])
            pipette.blow_out(mixing_plate[dispense_position[i]].top(10))
            pipette.mix(1, 300, cleaning_well['C5'])
            pipette.blow_out()

        #pipette.blow_out(src_pos.top(30))
        pipette.drop_tip(tip_pos)
   
    pipette.pick_up_tip(tiprack['C1'])
    for i in range(len(dispense_position)):
        pipette.mix(1, 300, mixing_plate[dispense_position[i]])
        pipette.aspirate(300, mixing_plate[dispense_position[i]])
        pipette.dispense(300, mixing_plate[dispense_position[i]])
        pipette.blow_out(mixing_plate[dispense_position[i]].top(10))
        pipette.aspirate(80, mixing_plate[dispense_position[i]])
        pipette.air_gap(5)
        pipette.dispense(120, dispense_plate[dispense_position[i]], rate=0.5)
        pipette.aspirate(50, dispense_plate[dispense_position[i]])
        pipette.dispense(120, dispense_plate[dispense_position[i]], rate=0.5)
        pipette.mix(1, 300, cleaning_well['C5'])
        pipette.blow_out()

    pipette.drop_tip(tiprack['C1'])

    
    
