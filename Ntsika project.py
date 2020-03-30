# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:36 2020

@author: Vuyo-Minenhle.Hlongw
"""

# %% Import Statements
import numpy as np
from scipy.optimize import minimize

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

# %% Function Definitions

class client:
    '''
    all input arguments must be annual values
    '''
    def __init__(self, name, age, gross_salary=0, rental_income=0, commission=0, local_dividends=0, foreign_dividends=0,interest=0, capital_gains=0, ra_contribution=0):
        self.name=name
        self.age=age
        self.gross_salary=gross_salary
        self.rental_income=rental_income
        self.commission=commission
        self.local_dividends=local_dividends
        self.foreign_dividends=foreign_dividends
        self.interest=interest
        self.capital_gains=capital_gains
        self.ra_contribution=ra_contribution

    
    def gross_income(self) :
        gross_income = self.gross_salary+self.rental_income+self.commission+self.local_dividends+self.foreign_dividends+self.interest+self.capital_gains
        return gross_income
    
    def deduction_ra(self):
        return min(self.ra_contribution, 0.275*(self.gross_income()), 350000)
    
    def deduction_foreign_div(self):
        deduction=0.634146341463415*self.foreign_dividends
        return deduction
    
    def deduction_local_div(self):
        deduction=self.local_dividends
        return deduction
    
    def deduction_interest(self):
        if self.age<65:
            return min(self.interest,23800)
        else:
            return min(self.interest,34500)
        
    def taxable_income(self) :
        taxable_income=self.gross_income()-self.deduction_ra()-self.deduction_foreign_div()-self.deduction_local_div()-self.deduction_interest()
        return taxable_income    
    
    def tax(self):
        '''returns tax rate and contribution 
        for an individual's annual income'''
        
        taxable_income=self.taxable_income()
        
        if 14220<taxable_income<189880 :
            rate=0.18
            cont=(taxable_income)*rate+0
        elif 189881<taxable_income<296540 :
            rate=0.26
            cont=(taxable_income-189881)*rate+34178
        elif 296541<taxable_income<410460 :
            rate=0.31
            cont=(taxable_income-296541)*rate+61910
        elif 410461<taxable_income<555600 :
            rate=0.36
            cont=(taxable_income-410461)*rate+97225
        elif 555601<taxable_income<708310 :
            rate=0.41
            cont=(taxable_income-555601)*rate+149475
        elif 708311<taxable_income<1500000 :
            rate=0.41
            cont=(taxable_income-708311)*rate+209032
        elif 1500000<taxable_income :
            rate=0.45
            cont=(taxable_income-1500000)*rate+533625
        else :
            rate=0
            cont=0
    #conditions for rebates, interest exemption
    #and capital gains exemptions still need to be added
        
        return cont  
    
    
    
    






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

