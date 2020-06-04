"""Program:  camper_age_input.py
Author:  Lisa Kilmer
last date modified:  06/03/2020
The purpose of this program is to convert input age of child in months
and convert it to years
"""
def convert_to_months(x):
    return x/12

if __name__=='__main__':
    age_in_months = input("enter age in months: ") #user input in months
    age_in_years = convert_to_months(int(age_in_months)) #call function with input
    print(str(age_in_years) + ' years is ' + str(age_in_months) + ' months') #print month and years result

