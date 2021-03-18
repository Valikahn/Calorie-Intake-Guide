# Colorie-Intake-Guide by Valikahn
#
# Copyright (C) 2020 - 2021 Valikahn <git@insentrica.net>
# Program v0.3-alpha - Code Name: Amun
# Licensed under the GPLv3 License.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# 
# Website:  https://www.insentrica.net
# Github:   https://github.com/Valikahn/Calorie-Intake-Guide
# GPLv3 Licence:  https://www.gnu.org/licenses/gpl-3.0.en.html
# 
# Calorie Intake Guide - pulling source data from https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation.

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
metsubmit=''
met=''

while (answer!='yes' and answer!='no'):
  answer = input("Enter yes or no to continue: ").lower()

if answer == "yes":
    # Input from user
    os.system("cls")
    fname = input('Please enter your first name: ')
    age = int(input('What is your age '+fname+' ? '))
    heightCM = int(input('What is your height in centimeters (CM) '+fname+' ? '))
    weightKG = int(input('What is you weight in kilograms (KG) '+fname+' ? '))
    morf = input("Enter your sex as male or female to continue: ").lower()
    print('\nNow we need to gauge how active you are per day.')
    print('\nPress 0 - Not Active / No Exercise')
    print('Press 1 - Sedentary Activity / Light Exercise')
    print('Press 2 - Moderate Activity / Average Exercise')
    print('Press 3 - Vigorous Activity / Workout Exercise')
    print('Press 4 - Athlete Activity / Sports Competing Exercise')

    # While True for met entry
    while True:
        metsubmit = int(input('\nPlease give an answer of 0-4: '))
        if metsubmit == 0:
            met=0
            break
        elif metsubmit == 1:
            met=2
            break
        elif metsubmit == 2:
            met=5
            break
        elif metsubmit == 3:
            met=8
            break
        elif metsubmit == 4:
            met=10
            break
        else: 
            print('Invalid entry...  Try again...')
            continue

    timemin = int(input('\nHow many minutes, on average are you active per day? '))
    print('\nNow we need want to know from you, what is your target weight loss per week.')
    print('\nPress 1 - 0.5 lb per week')
    print('Press 2 - 1.0 lb per week')
    print('Press 3 - 1.5 lb per week')
    print('Press 4 - 2.0 lb per week')

    # While True for calsubmit entry
    while True:
        calsubmit = int(input('\nPlease give an answer of 0-4: '))
        if calsubmit == 1:
            calorie_lose=250
            break
        elif calsubmit == 2:
            calorie_lose=500
            break
        elif calsubmit == 3:
            calorie_lose=750
            break
        elif calsubmit == 4:
            calorie_lose=1000
            break
        else:
            print('Invalid entry...  Try again...')
            continue

    # Calculation for each factor
    mw=mmw*weightKG
    mh=mmh*heightCM
    ma=mma*age
    ww=wmw*weightKG
    wh=wmh*heightCM
    wa=wma*age
    timesecs = timemin*60    
    
    # Continue for IF statement for male or female entry
    if morf == "male":
    
        # Male Equation formula
        mbmranswer=mmbmr+mw+mh-ma
        mbmr = str(round(mbmranswer, 0))
        mbmianswer = weightKG/heightCM/heightCM*defi
        mbmi = str(round(mbmianswer, 2))
        mibwanswer = ibwform*heightCM*heightCM/defi
        mibw = str(round(mibwanswer, 1))
        mmetanswer = timesecs*met*calmet*weightKG/meta
        mmetadd = mmetanswer+mbmranswer
        mmet = str(round(mmetadd, 0))
        mcalorie_lose_answer = mmetadd-calorie_lose
        mcalorie_lose = str(round(mcalorie_lose_answer))

        print('\nPlease wait '+fname+' working. . . . . . . . . . .')
        time.sleep(5)
        os.system("cls")
        print('This is your Calorie Intake Guide '+fname+'')
        #
        print('\nYour Age: '+str(age)+' | Your Height: '+str(heightCM)+'cm | Your Weight: '+str(weightKG)+'kg | Your Activity Rate: '+str(met))
        print('Your Activity Time: '+str(timemin)+' mins | Your Gender: '+str(morf)+' | Calorie Drop: '+str(calorie_lose))
        print('\n------------------------------------------------------------------------------')
        #
        print('\nYour estimated Basal Metabolic Rate (BMR) is: '+mbmr+' kcals')
        print('Your personal BMR formula is = 66.5 + ( 13.75 × '+str(weightKG)+' ) + ( 5.003 × '+str(heightCM)+' ) – ( 6.755 × '+str(age)+' )\n')
        #
        print('Your calorie intake to maintain body weight is: '+str(round(mmetanswer, 0))+' + '+str(round(mbmranswer, 0))+' = '+str(mmet)+' - This is estimated based on your answers!')
        print('Your formula to maintan body weight is = '+str(timemin)+' × '+str(met)+' × '+str(calmet)+' × '+str(weightKG)+' / '+str(meta))
        #
        print('\nYou have chosen to lose '+str(calorie_lose)+' calories per day.')
        print('To lose the desired weight your calorie intake per day should not exceed: '+str(mcalorie_lose)+' calories per day.')
        #
        print('\nYour Body Mass Index is: '+mbmi)
        print('Your personal BMI formula is = '+str(weightKG)+' / '+str(heightCM)+' / '+str(heightCM)+' × '+str(defi)+'\n')
        #
        print('Your Ideal Body Weight for your height and age is: '+mibw+'kg')
        print('Your personal IBW formula is = '+str(ibwform)+' × '+str(heightCM)+' × '+str(heightCM)+' / '+str(defi)+'\n')

        # Pause code from ending...
        os.system("pause")
    
    # Continue for IF statement for male or female entry
    elif morf == "female":
            
        # Female Equation formula
        wbmranswer=wmbmr+ww+wh-wa
        wbmr = str(round(wbmranswer, 0))
        wbmianswer = weightKG/heightCM/heightCM*defi
        wbmi = str(round(wbmianswer, 2))
        wibwanswer = ibwform*heightCM*heightCM/defi
        wibw = str(round(wibwanswer, 1))
        wmetanswer = timesecs*met*calmet*weightKG/meta
        wmetadd = wmetanswer+wbmranswer
        wmet = str(round(wmetadd, 0))
        wcalorie_lose_answer = wmetadd-calorie_lose
        wcalorie_lose = str(round(wcalorie_lose_answer))
     
        print('\nPlease wait '+fname+' working. . . . . . . . . . .')
        time.sleep(5)
        os.system("cls")
        print('This is your Calorie Intake Guide '+fname+'')
        #
        print('\nYour Age: '+str(age)+' | Your Height: '+str(heightCM)+'cm | Your Weight: '+str(weightKG)+'kg | Your Activity Rate: '+str(met))
        print('Your Activity Time: '+str(timemin)+' mins | Your Gender: '+str(morf)+' | Calorie Drop: '+str(calorie_lose))
        print('\n------------------------------------------------------------------------------')
        #
        print('\nYour estimated Basal Metabolic Rate (BMR) is: '+wbmr+' kcals')
        print('Your personal BMR formula is = 66.5 + ( 13.75 × '+str(weightKG)+' ) + ( 5.003 × '+str(heightCM)+' ) – ( 6.755 × '+str(age)+' )\n')
        #
        print('Your calorie intake to maintain body weight is: '+str(round(wmetanswer, 0))+' + '+str(round(wbmranswer, 0))+' = '+str(wmet)+' - This is estimated based on your answers!')
        print('Your formula to maintan body weight is = '+str(timemin)+' × '+str(met)+' × '+str(calmet)+' × '+str(weightKG)+' / '+str(meta))
        #
        print('\nYou have chosen to lose '+str(calorie_lose)+' calories per day.')
        print('To lose the desired weight your calorie intake per day should not exceed: '+str(wcalorie_lose)+' calories per day')
        #
        print('\nYour Body Mass Index is: '+wbmi)
        print('Your personal BMI formula is = '+str(weightKG)+' / '+str(heightCM)+' / '+str(heightCM)+' × '+str(defi)+'\n')
        #
        print('Your Ideal Body Weight for your height and age is: '+wibw+'kg')
        print('Your personal IBW formula is = '+str(ibwform)+' × '+str(heightCM)+' × '+str(heightCM)+' / '+str(defi)+'\n')

        # Pause code from ending...
        os.system("pause")
    
    # Continue for IF statement for male or female entry
    else:
        print('Invalid entry...  Try again...')
 
elif answer == 'no':
    print('\nGoodbye')
    time.sleep(2)
    os.system('cls')