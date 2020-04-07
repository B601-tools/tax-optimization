# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:33:11 2020

@author: Vuyo-Minenhle.Hlongw
"""

import numpy as np
from scipy.optimize import minimize

class client:
    '''
    all input arguments must be annual values
    '''
    def __init__(self, name='Generic', age='Generic', gross_salary=0, rental_income=0, commission=0, local_dividends=0, 
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
        '''returns tax rate and contribution 
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
    

    def fund_constraints(self,Fund_1=False,Fund_2=False,Fund_3=False,Fund_4=False):
        
        All_funds=[Fund_1,Fund_2,Fund_3,Fund_4]
        
        accessible_funds=[]
        
        for item in list(range(0,len(All_funds),1)):
            
            if bool(All_funds[item])==True:
                accessible_funds.append(All_funds[item])
        
                
                
        
        def Access_Constraint(x):
            
            ME_rental=sum(x[56:60])
            ME_rental=sum(x[52:56])
            ME_interest=sum(x[40:44])
            ME_foreign_dividends=sum(x[44:48])
            ME_local_dividends=sum(x[48:52])
            
            ME1=ME_local_dividends+ME_foreign_dividends+ME_interest+ME_rental+ME_rental
            
            
            NC_local_dividends=sum(x[28:32])
            NC_interest=sum(x[20:24])
            NC_rental=sum(x[32:36])
            NC_rental=sum(x[36:40])
            NC_foreign_dividends=sum(x[24:28])
            
            NC1=NC_local_dividends+NC_foreign_dividends+NC_interest+NC_rental+NC_rental
            
            
            KC_rental=sum(x[12:16])
            KC_rental=sum(x[16:20])
            KC_interest=sum(x[0:4])
            KC_foreign_dividends=sum(x[4:8])
            KC_local_dividends=sum(x[8:12])
            
            KC1=KC_local_dividends+KC_foreign_dividends+KC_interest+KC_rental+KC_rental
            
            Total_funds_var={'KC':KC1,
                             'NC':NC1,
                             'ME':ME1}
            
            portfolio=['KC','NC','ME']
            
            constraint=[]
            for item in list(range(0,len(portfolio),1)):
                if portfolio[item] not in accessible_funds:
                    constraint.append(Total_funds_var[portfolio[item]])
                    
                
                
            return sum(constraint)
        return Access_Constraint
        
        
        
        
        
    






#%%
class Fund:
    def __init__(self,interest=0, foreign_dividends=0,
                 local_dividends=0,rental=0,capital_gains=0):
        self.interest=interest
        self.foreign_dividends=foreign_dividends
        self.local_dividends=local_dividends
        self.rental=rental
        self.capital_gains=capital_gains
        
    def returns(self):
        return [self.interest,self.foreign_dividends,
                self.local_dividends,self.rental,self.capital_gains]
    

        
      
        
def obj_func(x):
    
    Ntsika=client(name='Ntsika', age=23, gross_salary=256508, rental_income=22055+sum(x[12:53:20]), 
                  commission=111905, local_dividends=2917+sum(x[8:49:20]), foreign_dividends=0+sum(x[4:45:20]), 
                  interest=0+sum(x[0:41:20]), capital_gains=0+sum(x[16:57:20]), ra_contribution=0)
    
    Refiloe=client(name='Refiloe', age=22, gross_salary=7500, rental_income=21170+sum(x[13:54:20]), 
                   commission=0, local_dividends=0+sum(x[9:50:20]), foreign_dividends=0+sum(x[5:46:20]),
                   interest=0+sum(x[1:42:20]), capital_gains=0+sum(x[17:58:20]), ra_contribution=0)
    
    Thando=client(name='Thando', age=8, gross_salary=0, rental_income=0+sum(x[14:55:20]), 
                 commission=0, local_dividends=0+sum(x[10:51:20]), foreign_dividends=0+sum(x[6:47:20]),
                 interest=0+sum(x[2:43:20]), capital_gains=0+sum(x[18:59:20]), ra_contribution=0)
    
    Lerato=client(name='Lerato', age=15, gross_salary=0, rental_income=0+sum(x[15:56:20]), 
                  commission=0, local_dividends=0+sum(x[11:52:20]), foreign_dividends=0+sum(x[7:48:20]),
                  interest=0+sum(x[3:44:20]), capital_gains=0+sum(x[19:60:20]), ra_contribution=0)


    total_tax=Ntsika.tax()+Refiloe.tax()+Thando.tax()+Lerato.tax()
  
    return total_tax   


KC=Fund(129715,0,0,110556,0)
NC=Fund(154,0,0,0,0)
ME=Fund(0,28000,55000,0,480000) 

Ntsika1=client()
Refiloe1=client()
Thando1=client()
Lerato1=client()
    

def constraint_1(x):
    return sum(x[0:4])-KC.interest

def constraint_2(x):
    return sum(x[20:24])-NC.interest

def constraint_3(x):
    return sum(x[40:44])-ME.interest

def constraint_4(x):
    return sum(x[4:8])-KC.foreign_dividends

def constraint_5(x):
    return sum(x[24:28])-NC.foreign_dividends

def constraint_6(x):
    return sum(x[44:48])-ME.foreign_dividends
     
def constraint_7(x):
    return sum(x[8:12])-KC.local_dividends

def constraint_8(x):
    return sum(x[28:32])-NC.local_dividends

def constraint_9(x):
    return sum(x[48:52])-ME.local_dividends        

def constraint_10(x):
    return sum(x[12:16])-KC.rental

def constraint_11(x):
    return sum(x[32:36])-NC.rental

def constraint_12(x):
    return sum(x[52:56])-ME.rental

def constraint_13(x):
    return sum(x[16:20])-KC.capital_gains

def constraint_14(x):
    return sum(x[36:40])-NC.capital_gains

def constraint_15(x):
    return sum(x[56:60])-ME.capital_gains
 
            


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
#con16={'type':'eq','fun':Ntsika1.fund_constraints('KC','NC')}
##con17={'type':'eq','fun':Refiloe1.fund_constraints('KC','ME','NC')}
#con18={'type':'eq','fun':Thando1.fund_constraints('KC','ME')}
#con19={'type':'eq','fun':Lerato1.fund_constraints('KC','ME')}






cons=[con1,con2,con3,con4,con5,con6,con7,con8,con9,
      con10,con11,con12,con13,con14,con15]#,con16,con18,con19]#con17 omitted



b=(0,np.inf)

bnds=tuple([b]*60)
    
x0=np.array([100000]*60)

sol = minimize(obj_func,x0,method='SLSQP',bounds=bnds,constraints=cons)

solution_vector=sol.x[:]

np.set_printoptions(suppress=True)
print(sol.message,end='\n\n')
print(solution_vector)

















        