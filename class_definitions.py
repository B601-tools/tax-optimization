# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:33:11 2020

@author: Vuyo-Minenhle.Hlongw
"""

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

    def total_deductions(self) :
        total_deductions = self.deduction_ra()+self.deduction_foreign_div()+self.deduction_local_div()+self.deduction_interest()
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

