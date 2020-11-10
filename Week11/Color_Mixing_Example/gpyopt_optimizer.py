import GPy
from GPyOpt.methods import BayesianOptimization

def optimizer_func(X, Y, BatchSize):
    '''
    Bayesian Optimizer Function 
    
    BatchSize is the number of suggestions for the next rounds
    X should be the input variables
    Y should be the metric to be optimized
    '''

    bds = [{'name': 'x1', 'type': 'continuous', 'domain': (0, 1)},
           {'name': 'x2', 'type': 'continuous', 'domain': (0, 1)},
           {'name': 'x3', 'type': 'continuous', 'domain': (0, 1)},
          ]
 
    
    constraints = [{'name': 'constr_1', 
                    'constraint': 'x[:,0] + x[:,1] + x[:,2] -(1 + 0.005)'},###<= 0
                   {'name': 'constr_2', 
                    'constraint': '(1- 0.005) - (x[:,0] + x[:,1] + x[:,2]) '}]###<= 0

    kernel = GPy.kern.Matern52(input_dim=len(bds), ARD = True)

    optimizer = BayesianOptimization(f=None, 
                                     domain=bds,
                                     constraints = constraints,
                                     model_type='GP',
                                     acquisition_type ='EI',
                                     acquisition_jitter = 0.1,
                                     X=X,
                                     Y=Y,
                                     evaluator_type = 'local_penalization',
                                     batch_size = BatchSize,
                                     normalize_Y= True,
                                     #noise_var = 0.02**2,
                                     kernel = kernel
                                     )
    return optimizer