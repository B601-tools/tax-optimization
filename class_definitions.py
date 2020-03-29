# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:01:28 2020

@author: Mutahi.Wachira
"""

class Client:
    def _init_(self, income):
        return 
    
    def tax(income):
        #tax logic
    
# %% Example
class Person:
    def __init__(self, name, age, annual_income):
        self.name = name
        self.age = age
        self.annual_income = annual_income

    def tax(self):
        '''returns tax rate and contribution 
        for an individual's annual income'''
        if 14220<self.annual_income<189880 :
            rate=0.18
            cont=(self.annual_income)*rate+0
        elif 189881<self.annual_income<296540 :
            rate=0.26
            cont=(self.annual_income-189881)*rate+34178
        elif 296541<self.annual_income<410460 :
            rate=0.31
            cont=(self.annual_income-296541)*rate+61910
        elif 410461<self.annual_income<555600 :
            rate=0.36
            cont=(self.annual_income-410461)*rate+97225
        elif 555601<self.annual_income<708310 :
            rate=0.41
            cont=(self.annual_income-555601)*rate+149475
        elif 708311<self.annual_income<1500000 :
            rate=0.41
            cont=(self.annual_income-708311)*rate+209032
        elif 1500000<self.annual_income :
            rate=0.45
            cont=(self.annual_income-1500000)*rate+533625
        else :
            rate=0
            cont=0
            
        return cont

Ntsika = Person("Ntsika",23,100000)




