# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:36 2020

@author: Vuyo-Minenhle.Hlongw
"""

# %% Import Statements
import numpy as np
from scipy.optimize import minimize
exec(open('class_check.py').read())

# %% Initial Variables
Income={
#        'Heading':['Salary', 'Rental', 'Commission', 'Dividends', 'Interest', 'CapitalGain'],
        'Ntsika':[256508, 22055, 111905, 2917, 0,0],
        'Refiloe':[7200, 21170, 0, 0, 0, 0], 
        'Thando':[0, 0, 0, 0, 0, 0],
        'Lerato':[0, 0, 0, 0, 0, 0], 
        }


Funds={
#       'Heading':['Interest','Local Dividends','Rental Income', 'Capital Gain', 'Foreign Dividends'],
       'KC':[129715, 0, 110556, 0, 0],
       'NC':[154, 0, 0, 0, 0],
       'ME':[0, 55000, 0, 480000, 28000],
       }

RA_contributions={
        'Ntsika': 600*12,
        'Refiloe': 300*12,
        'Thando': 300*12,
        'Lerato': 300*12
        }



# %% Objective Function and Constraints 
    
def obj_func(x):
#   Here is what x stands for:
#   KC1+ KC2+ KC3+ KC4+ NC1+ NC2+ NC3+ NC4+ ME1+ ME2+ ME3+  ME4
#   x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]+x[10]+x[11]
    Ntsika=tax(sum(Income['Ntsika'])+x[4]+x[8])[1]
    Refiloe=tax(sum(Income['Refiloe'])+x[1]+x[5]+x[9])[1]    
    Thando=tax(sum(Income['Thando'])+x[2]+x[10])[1]
    Lerato=tax(sum(Income['Lerato'])+x[11])[1]
    
    total_tax=Ntsika+Refiloe+Thando+Lerato
    return total_tax

x0=np.array([0, sum(Funds['KC']), 0, 0, 0, sum(Funds['NC']), 0, 0, sum(Funds['ME']), 0, 0, 0])# initial guess

#define constraints
def constraint1(x):
    return x[0]+x[1]+x[2]+x[3]-sum(Funds['KC'])

def constraint2(x):
    return x[4]+x[5]+x[6]+x[7]-sum(Funds['NC'])
    
def constraint3(x):
    return x[8]+x[9]+x[10]+x[11]-sum(Funds['ME'])

def constraint4(x):
    return x[0]

def constraint5(x):
    return x[6]+x[7]



con1={'type':'eq','fun':constraint1}
con2={'type':'eq','fun':constraint2}
con3={'type':'eq','fun':constraint3}
con4={'type':'eq','fun':constraint4}
con5={'type':'eq','fun':constraint5}

# %% Solver
b=(0,np.inf)

bnds=(b,b,b,b,b,b,b,b,b,b,b,b)

cons=[con1,con2,con3,con4,con5]

sol = minimize(obj_func,x0,method='SLSQP',bounds=bnds,constraints=cons)

solution_vector=sol.x[:]

np.set_printoptions(suppress=True)
print(solution_vector)

