# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:36 2020

@author: Vuyo-Minenhle.Hlongw
"""

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint

Income={
#        'Heading':['Salary', 'Rental', 'Commission', 'Dividends', 'Interest', 'CapitalGain'],
        'Ntsika':[256508, 22055, 111905, 2917, 0,0],
        'Refiloe':[7200, 21170, 0, 0, 0, 0], 
        'Thando':[200, 0, 0, 0, 0, 0],
        'Lerato':[0, 0, 0, 0, 0, 0], 
        }


Funds={
#       'Heading':['Interest','Local Dividends','Rental Income', 'Capital Gain', 'Foreign Dividends'],
       'KC':[129715, 0, 110556, 0, 0],
       'NC':[154, 0, 0, 0, 0],
       'ME':[0, 55000, 0, 480000, 28000],
       }

def tax(annual_income):
    '''returns tax rate and contribution 
    for an individual's monthly income'''
    if 4000<annual_income<189880 :
        rate=0.18
    elif 189881<annual_income<296540 :
        rate=0.26
    elif 296541<annual_income<410460 :
        rate=0.31
    elif 410461<annual_income<555600 :
        rate=0.36
    elif 555601<annual_income<708310 :
        rate=0.41
    elif 708311<annual_income<1500000 :
        rate=0.41
    elif 1500000<annual_income :
        rate=0.45
    else :
        rate=0
    cont=rate*annual_income
    
#conditions for rebates, interest exemption
#and capital gains exemptions still need to be added
    
    return [rate, cont]  


def obj_func(x):
#   Here is what x stands for:
#   KC1+ KC2+ KC3+ KC4+ NC1+ NC2+ NC3+ NC4+ ME1+ ME2+ ME3+  ME4
#   x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]+x[10]+x[11]
    Ntsika=tax(sum(Income['Ntsika'])*12+x[4]+x[8])[1]    
    Refiloe=tax(sum(Income['Refiloe'])*12+x[1]+x[5]+x[9])[1]
    Thando=tax(sum(Income['Thando'])*12+x[2]+x[10])[1]
    Lerato=tax(sum(Income['Lerato'])*12+x[11])[1]
    
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

con1={'type':'eq','fun':constraint1}
con2={'type':'eq','fun':constraint2}
con3={'type':'eq','fun':constraint3}

cons=[con1,con2,con3]

#solve using 


sol = minimize(obj_func,x0,method='SLSQP',bounds=None,constraints=cons)
print(sol)

