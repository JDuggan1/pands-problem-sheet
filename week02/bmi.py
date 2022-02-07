#BMI Calculator by Jonathon Duggan
Reference : https://www.sololearn.com/Discuss/2686226/bmi-calculator-python-beginner-project


weight = int((97));
height = float((160));
x = weight/float(height*height);
if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')