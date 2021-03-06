# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:33:11 2020

@author: Vuyo-Minenhle.Hlongw
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize

class client:
    '''
    all input arguments must be annual values
    '''
    def __init__(self, name='Generic', age=50, gross_salary=0, rental_income=0, commission=0, local_dividends=0, 
                 foreign_dividends=0,interest=0, capital_gains=0, ra_contribution=0):
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
        gross_income = (self.gross_salary+self.rental_income+self.commission+
                        self.local_dividends+self.foreign_dividends+self.interest+self.capital_gains)
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

    def total_deductions(self) :
        total_deductions = (self.deduction_ra()+self.deduction_foreign_div()+
                            self.deduction_local_div()+self.deduction_interest())
        return total_deductions
        
    def taxable_income(self) :
        taxable_income=self.gross_income()-self.total_deductions()
        return taxable_income    
    
    def rebate(self):
        if self.age < 65:
            rebate = 13635
        elif self.age < 75:
            rebate = 13635 + 7479
        else:
            rebate = 13635 + 7479 + 2493
    
        return rebate
    
    def tax(self):
        '''returns tax  contribution 
        for an individual's annual income'''
        
        taxable_income=self.taxable_income()
        
        if self.rebate()<taxable_income<189880 :
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

        return cont
     
       
def Access_Constraint(x):
    constraint=[]
    all_funds=['KC','NC','ME']
    clients=['Ntsika','Refiloe','Thando','Lerato']
    fund_arguments=5
    
    inaccessible_funds={'Ntsika':['KC'],'Refiloe':[],'Thando':['NC'],'Lerato':['NC']}        
    for client in list(inaccessible_funds.keys()):
        for item in inaccessible_funds[client]:
            b=item
            item=[b]
            x_0=len(clients)*fund_arguments*all_funds.index(b)
            x_i=list(range(x_0+(clients.index(client)),x_0+len(clients)*int(fund_arguments),len(clients)))
            for i in x_i:
                constraint.append(x[i])                        
    return sum(constraint)

class Fund:
    def __init__(self,interest=0, foreign_dividends=0,
                 local_dividends=0,rental=0,capital_gains=0):
        self.interest=interest
        self.foreign_dividends=foreign_dividends
        self.local_dividends=local_dividends
        self.rental=rental
        self.capital_gains=capital_gains
        
        
    def returns(self):
        return sum([self.interest,self.foreign_dividends,
                self.local_dividends,self.rental,self.capital_gains])
    

Ntsika=client(name='Ntsika', age=23, ra_contribution=0, gross_salary=256508)    
Refiloe=client(name='Refiloe', age=22, ra_contribution=0, gross_salary=72000)    
Thando=client(name='Thando', age=8, ra_contribution=0)    
Lerato=client(name='Lerato', age=15,  ra_contribution=0)
       
def obj_func(x):
    Ntsika.rental_income=22055+sum(x[12:53:20])
    Ntsika.local_dividends=2917+sum(x[8:49:20])
    Ntsika.foreign_dividends=sum(x[4:45:20])
    Ntsika.interest=sum(x[0:41:20])
    Ntsika.capital_gains=sum(x[16:57:20])
    
    Refiloe.rental_income=21170+sum(x[13:54:20])
    Refiloe.local_dividends=sum(x[9:50:20])
    Refiloe.foreign_dividends=sum(x[5:46:20])
    Refiloe.interest=sum(x[1:42:20])
    Refiloe.capital_gains=sum(x[17:58:20])
    
    Thando.rental_income=sum(x[14:55:20])
    Thando.local_dividends=sum(x[10:51:20])
    Thando.foreign_dividends=sum(x[6:47:20])
    Thando.interest=sum(x[2:43:20])
    Thando.capital_gains=sum(x[18:59:20])
    
    Lerato.rental_income=sum(x[15:56:20])
    Lerato.local_dividends=sum(x[11:52:20])
    Lerato.foreign_dividends=sum(x[7:48:20])
    Lerato.interest=sum(x[3:44:20])
    Lerato.capital_gains=sum(x[19:60:20])
       
    total_tax=Ntsika.tax()+Refiloe.tax()+Thando.tax()+Lerato.tax()
    
    return total_tax

KC=Fund(129715,0,0,110556,0)
NC=Fund(154,0,0,0,0)
ME=Fund(0,28000,55000,0,480000) 

def constraint_1(x):
    return sum(x[0:4])-KC.interest

def constraint_4(x):
    return sum(x[4:8])-KC.foreign_dividends

def constraint_7(x):
    return sum(x[8:12])-KC.local_dividends

def constraint_10(x):
    return sum(x[12:16])-KC.rental

def constraint_13(x):
    return sum(x[16:20])-KC.capital_gains

def constraint_2(x):
    return sum(x[20:24])-NC.interest

def constraint_5(x):
    return sum(x[24:28])-NC.foreign_dividends

def constraint_8(x):
    return sum(x[28:32])-NC.local_dividends

def constraint_11(x):
    return sum(x[32:36])-NC.rental

def constraint_14(x):
    return sum(x[36:40])-NC.capital_gains

def constraint_15(x):
    return sum(x[56:60])-ME.capital_gains   

def constraint_3(x):
    return sum(x[40:44])-ME.interest    

def constraint_6(x):
    return sum(x[44:48])-ME.foreign_dividends  

def constraint_9(x):
    return sum(x[48:52])-ME.local_dividends  

def constraint_12(x):
    return sum(x[52:56])-ME.rental  

con1={'type':'eq','fun':constraint_1}        
con2={'type':'eq','fun':constraint_2}          
con3={'type':'eq','fun':constraint_3}          
con4={'type':'eq','fun':constraint_4}         
con5={'type':'eq','fun':constraint_5}          
con6={'type':'eq','fun':constraint_6}  
con7={'type':'eq','fun':constraint_7}
con8={'type':'eq','fun':constraint_8}  
con9={'type':'eq','fun':constraint_9}  
con10={'type':'eq','fun':constraint_10}  
con11={'type':'eq','fun':constraint_11}
con12={'type':'eq','fun':constraint_12}  
con13={'type':'eq','fun':constraint_13}  
con14={'type':'eq','fun':constraint_14}  
con15={'type':'eq','fun':constraint_15}
con16={'type':'eq','fun':Access_Constraint}


cons=[con1,con2,con3,con4,con5,con6,con7,con8,con9,
      con10,con11,con12,con13,con14,con15,con16]

b=(0,np.inf)

bnds=tuple([b]*60)
    
x0=np.array([5000]*60)

sol = minimize(obj_func,x0,method='SLSQP',bounds=bnds,constraints=cons)

solution_vector=sol.x[:]

np.set_printoptions(suppress=True)

all_funds=['KC','NC','ME']
income_types = ['Interest', 'Foreign Dividends', 'Local Dividends', 'Rentail Income', 'Capital Gains']

line_items = []
for fund in all_funds:
    for income in income_types:
        line_items.append(fund + ' ' + income)

clients=['Ntsika','Refiloe','Thando','Lerato']
fund_arguments=5

solution_vector.shape = (len(all_funds)*fund_arguments, len(clients))

solution_df = pd.DataFrame(data = solution_vector, columns = clients)
solution_df.round(2)
solution_df.insert(0, "Fund Income", line_items)
solution_df

overall_tax_rate = (sol.fun/(KC.returns()+NC.returns()+ME.returns()))*100

print(sol.message,end='\n\n')

print('Tax_payable: %.2f' % sol.fun)
print('Overall tax rate: %.2f%% \n \n' % overall_tax_rate)

print(solution_df)