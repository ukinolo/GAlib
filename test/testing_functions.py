import numpy as np
from types import FunctionType

def Rastrigin_function(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]**2 - 10*np.cos(2*np.pi*x[i])
    return 10*len(x) + sum

def Ackley_function(x):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2 + x[1]**2))) - np.exp(0.5*(np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))) + np.e + 20

def Sphere_function(x):
    return np.sum(np.power(x, 2))

def Rosenbrock_function(x):
    sum = 0
    for i in range(len(x) - 1):
        sum += 100*((x[i+1] - x[i]**2)**2) + (1 - x[i])**2
    return sum

def Beale_function(x):
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2

def Booth_function(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def Bukin_function_N6(x):
    return 100*np.sqrt(np.abs(x[1] - 0.01*x[0]**2)) + 0.01*np.abs(x[0] + 10)

def Matyas_function(x):
    return 0.26*(x[0]**2 + x[1]**2) - 0.48*x[0]*x[1]

def Lévi_function_N13(x):
    return np.sin(3*np.pi*x[0])**2 + (x[0] - 1)**2*(1 + np.sin(3*np.pi*x[1])**2) + (x[1] - 1)**2*(1 + np.sin(2*np.pi*x[1])**2)

def Three_hump_camel_function(x):
    return 2*x[0]**2 - 1.05*x[0]**4 + x[0]**6/6 + x[0]*x[1] + x[1]**2

def Eggholder_function(x):
    return -(x[1] + 47)*np.sin(np.sqrt(np.abs(x[0]/2 + x[1] + 47))) - x[0]*np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))

def McCormick_function(x):
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1

def Styblinski_Tang_function(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]**4 - 16*x[i]**2 + 5*x[i]
    return sum/2

#Function for returning minimum position and value of minimum
def stored_minimums(f, system_size):
    if(isinstance(f, str)):
        name = f
    else:
        name = f.__name__
    if(name == 'Rastrigin_function'):
        return np.zeros(system_size), 0.
    
    if(name == 'Ackley_function'):
        return np.zeros(2), 0.
    
    if(name == 'Sphere_function'):
        return np.zeros(system_size), 0.

    if(name == 'Rosenbrock_function'):
        return np.ones(system_size), 0.

    if(name == 'Beale_function'):
        return np.array([3, 0.5]), 0.

    if(name == 'Booth_function'):
        return np.array([1, 3]), 0.

    if(name == 'Bukin_function_N6'):
        return np.array([-10, 1]), 0.

    if(name == 'Matyas_function'):
        return np.zeros(2), 0.

    if(name == 'Lévi_function_N13'):
        return np.array([1, 1]), 0.
    
    if(name == 'Three_hump_camel_function'):
        return np.zeros(2), 0.
    
    if(name == 'Eggholder_function'):
        return np.array([512, 404.2319]), -959.6407

    if(name == 'McCormick_function'):
        return np.array([-0.54719, -1.54719]), -1.9133

    if(name == 'Styblinski_Tang_function'):
        value = -2.903534
        temp = np.zeros(system_size)
        for i in range(system_size):
            temp[i] = value
        return temp, -39.166166*system_size

    return np.nan

functions = np.array([[Rastrigin_function, 2],
                      [Rastrigin_function, 3],
                      [Rastrigin_function, 4],
                      [Rastrigin_function, 5],
                      [Rastrigin_function, 10],
                      [Rastrigin_function, 20],
                      [Rastrigin_function, 50],
                      [Ackley_function, 2],
                      [Sphere_function, 2],
                      [Sphere_function, 3],
                      [Sphere_function, 4],
                      [Sphere_function, 5],
                      [Sphere_function, 10],
                      [Sphere_function, 20],
                      [Sphere_function, 50],
                      [Rosenbrock_function, 2],
                      [Rosenbrock_function, 3],
                      [Rosenbrock_function, 4],
                      [Rosenbrock_function, 5],
                      [Rosenbrock_function, 10],
                      [Rosenbrock_function, 20],
                      [Rosenbrock_function, 50],
                      [Beale_function, 2],
                      [Booth_function, 2],
                      [Bukin_function_N6, 2],
                      [Matyas_function, 2],
                      [Lévi_function_N13, 2],
                      [Three_hump_camel_function, 2],
                      [Eggholder_function, 2],
                      [McCormick_function, 2],
                      [Styblinski_Tang_function, 2],
                      [Styblinski_Tang_function, 3],
                      [Styblinski_Tang_function, 4],
                      [Styblinski_Tang_function, 5],
                      [Styblinski_Tang_function, 10],
                      [Styblinski_Tang_function, 20],
                      [Styblinski_Tang_function, 50]])