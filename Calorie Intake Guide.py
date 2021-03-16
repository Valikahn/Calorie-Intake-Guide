# Copyright (C) 2020 - 2021 Valikahn <git@insentrica.net>
# Program v0.2.1-alpha - Code Name: Amun
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# 
# Website:  https://www.insentrica.net
# Github:   https://github.com/Valikahn/Calorie-Intake-Guide
#
# Calorie Intake Guide - pulling source data from https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation.
# The program will show from basic input the estimated BMR, BMI and IBW.

# Disclaimer
print('DISCLAIMER')
print('----------\n')
print('All information and tools presented within this site are intended for educational purposes.')
print('Any health, diet or exercise advice is not intended as medical diagnosis or treatment.')
print('If you think you have any type of medical condition you must seek professional advice even if')
print('you believe it may be due to diet, food or exercise. We are not a medical institute and')
print('therefore we will never offer/give any diagnosis or medical advice.\n')

# Imports
import os
import time

# Male Required Harris–Benedict equation inputs 
# Source:  https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
# BMR = 66.5 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) – ( 6.755 × age in years )
mmw=13.75 # Weight standard input
mmh=5.003 # Height standard input
mma=6.755 # Age standard input
mmbmr=66.5 # Basal Metabolic Rate (BMR) standard input

# Female Required Harris–Benedict equation inputs 
# Source:  https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
# BMR = 655 + ( 9.563 × weight in kg ) + ( 1.850 × height in cm ) – ( 4.676 × age in years )
wmw=9.563 # Weight standard input
wmh=1.850 # Height standard input
wma=4.676 # Age standard input
wmbmr=655 # Basal Metabolic Rate (BMR) standard input

# Universal Entries
defi=10000
ibwform=22
calmet=3.5
meta=200*60

# Do while if yes or no
answer = ''
morf = ''
while (answer!='yes' and answer!='no'):
  answer = input("Enter yes or no to continue: ").lower()

if answer == "yes":
    # Input from user
    os.system("cls")
    fname = input('Please enter your first name: ')
    age = int(input('What is your age '+fname+' ? '))
    heightCM = int(input('What is your height in centimeters (CM) '+fname+' ? '))
    weightKG = int(input('What is you weight in kilograms (KG) '+fname+' ? '))
    met = int(input('OK '+fname+', on average, on a scale of 1-10 how active are you per day? '))
    timemin = int(input('How many minutes, on average are you active per day? '))
    morf = input("Enter your sex as male or female to continue: ").lower()
    
    # Calculation for each factor
    mw=mmw*weightKG
    mh=mmh*heightCM
    ma=mma*age
    ww=wmw*weightKG
    wh=wmh*heightCM
    wa=wma*age

    # Male Equation formula
    mbmranswer=mmbmr+mw+mh-ma
    mbmr = str(round(mbmranswer, 0))
    mbmianswer = weightKG/heightCM/heightCM*defi
    mbmi = str(round(mbmianswer, 2))
    mibwanswer = ibwform*heightCM*heightCM/defi
    mibw = str(round(mibwanswer, 2))
    timesecs = timemin*60
    mmetanswer = timesecs*met*calmet*weightKG/meta
    mmetadd = mmetanswer+mbmranswer
    mmet = str(round(mmetadd, 0))
    
    # Female Equation formula
    wbmranswer=wmbmr+ww+wh-wa
    wbmr = str(round(wbmranswer, 0))
    wbmianswer = weightKG/heightCM/heightCM*defi
    wbmi = str(round(wbmianswer, 2))
    wibwanswer = ibwform*heightCM*heightCM/defi
    wibw = str(round(wibwanswer, 2))
    
    if morf == "male":
 
        # Male Section
        #print('Male Entry')
        print('\nPlease wait '+fname+' working. . . . . . . . . . .')
        time.sleep(5)
        os.system("cls")
        print('This is your Calorie Intake Guide '+fname+'')
        print('Your Age: '+str(age)+' | Your Height: '+str(heightCM)+'cm | Your Weight: '+str(weightKG)+'kg')
        print('Your Activity Rate: '+str(met)+' | Your Activity Time: '+str(timemin)+' mins | Your Gender: '+str(morf))
        print('\nYour estimated Basal Metabolic Rate (BMR) is: '+mbmr+' kcals')
        print('Your personal BMR formula is = 66.5 + ( 13.75 × '+str(weightKG)+' ) + ( 5.003 × '+str(heightCM)+' ) – ( 6.755 × '+str(age)+' )\n')
        print('Your calorie intake to maintain body weight is:  '+str(mmet)+' - This is estimated based on your answers')
        print('Your formula to maintan body weight is = '+str(timemin)+' × '+str(met)+' × '+str(calmet)+' × '+str(weightKG)+' / '+str(meta)+'\n')
        print('Your Body Mass Index is: '+mbmi)
        print('Your personal BMI formula is = '+str(weightKG)+' / '+str(heightCM)+' / '+str(heightCM)+' × '+str(defi)+'\n')
        print('Your Ideal Body Weight is: '+mibw+' KG')
        print('Your personal IBW formula is = '+str(ibwform)+' × '+str(heightCM)+' × '+str(heightCM)+' / '+str(defi)+'\n')

        # Pause code from ending...
        os.system("pause")
    
    elif morf == "female":

        # Female Section
        #print('Female Entry')
        print('\nPlease wait '+fname+' working. . . . . . . . . . .')
        time.sleep(5)
        os.system("cls")
        print('This is your Calorie Intake Guide '+fname+'\n')
        print('Your Basal Metabolic Rate (BMR) is: '+wbmr+' kcals')
        print('Your personal BMR formula is = 665 + ( 9.563 × '+str(weightKG)+' ) + ( 1.850 × '+str(heightCM)+' ) – ( 4.676 × '+str(age)+' )\n')
        print('Your Body Mass Index is: '+wbmi)
        print('Your personal BMI formula is = '+str(weightKG)+' / '+str(heightCM)+' / '+str(heightCM)+' × '+str(defi)+'\n')
        print('Your Ideal Body Weight is: '+wibw+' KG')
        print('Your personal IBW formula is = '+str(ibwform)+' × '+str(heightCM)+' × '+str(heightCM)+' / '+str(defi)+'\n')

        # Pause code from ending...
        os.system("pause")
 
elif answer == 'no': 
    os.system('cls')
