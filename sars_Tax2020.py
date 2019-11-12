# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:32:43 2019

@author: irist
"""

#Calculate the South African Income Tax payable

# Tax brackets 2020
LIMIT_1 =195850
LIMIT_2 =305850
LIMIT_3 =423300
LIMIT_4 =555600
LIMIT_5 =708310
LIMIT_6 =1500000
LIMIT_7 =1500001

# Tax Rates
FIXED2 = 35253
FIXED3 = 63853
FIXED4 = 100263
FIXED5 = 147891
FIXED6 = 207448
FIXED7 = 532041

RATE1 = 0.18
RATE2 = 0.26
RATE3 = 0.31
RATE4 = 0.36
RATE5 = 0.39
RATE6 = 0.41
RATE7 = 0.45

#Input the income from the user
income = float(input("Enter the income: "))

#Compute the amount of tax payable
if income < LIMIT_1:
    tax = income * RATE1
elif income < LIMIT_2:
    tax = ((income - LIMIT_1)*RATE2)+FIXED2
elif income < LIMIT_3:
    tax = ((income - LIMIT_2)*RATE3)+FIXED3
elif income < LIMIT_4:
    tax =((income - LIMIT_3)*RATE4)+FIXED4
elif income < LIMIT_5:
    tax = ((income - LIMIT_4)*RATE5)+FIXED5
elif income < LIMIT_6:
    tax = ((income - LIMIT_5)*RATE6)+FIXED6
else:
    tax = ((income - LIMIT_6)*RATE7)+FIXED7
    
#Display the result
print("With an income of R" + format(income, ",.2f"),
     "the income tax payable is R" + format(tax, ",.2f"))

print("Effective tax rate: "+"{:.2%}".format(tax/income))

#print((tax/income)*100)