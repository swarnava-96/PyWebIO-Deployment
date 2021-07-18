

# BMI Calculator Application

from pywebio.input import *
from pywebio.output import *

# Defining the BMI function

def bmicalculator():
    height = input("Please enter your height (in cms)", type = FLOAT)
    weight = input("Please enter your weight (in kgs)", type = FLOAT)

    bmi = weight/(height/100)**2

    bmi_output = [(16, "Severely Underweight"), (18.5, "Underweight"), (25, "Normal"), (30, "Overweight"),
                  (35, "Moderately Obese"), (float('inf'), "Severely Obese")]

    for tuple1, tuple2 in bmi_output:
        if bmi < tuple1:
            put_text("Your BMI is: %.1f and the person is: %s"%(bmi,tuple2))
            break


if __name__=="__main__":
    bmicalculator()