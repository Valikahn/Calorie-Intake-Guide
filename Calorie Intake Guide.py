# Required Harris–Benedict equation inputs 
mmw=13.75 # Weight standard input
mmh=5.003 # Height standard input
mma=6.755 # Age standard input
mmbmr=66.5 # Basal Metabolic Rate (BMR) standard input
defi=10000
ibwform=22

# Input from user
age = int(input('What is your age? '))
heightCM = int(input('What is your height in CM? '))
weightKG = int(float(input('What is you weight in KG? ')))

# Calculation for each factor
w=mmw*weightKG
h=mmh*heightCM
a=mma*age

# Equation formula
bmranswer=mmbmr+w+h-a
bmr = str(round(bmranswer, 0))
bmianswer = weightKG/heightCM/heightCM*defi
bmi = str(round(bmianswer, 2))
ibwanswer = ibwform*heightCM*heightCM/defi
ibw = str(round(ibwanswer, 2))

# Print output
print('')
print('Your Basal Metabolic Rate is: '+bmr+' kcals')
print('Your Body Mass Index is: '+bmi)
print('Your Ideal Body Weight is: '+ibw+' KG')