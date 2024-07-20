from nada_dsl import *

def nada_main():
    # Define the parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    # Define input variables: height and weight
    height = SecretInteger(Input(name="Height", party=party1))
    weight = SecretInteger(Input(name="Weight", party=party2))
    
    # Calculate BMI: BMI = weight / (height^2)
    height_squared = height * height
    bmi_numerator = weight
    bmi_denominator = height_squared
    
    # Secure division to calculate BMI
    bmi = bmi_numerator / bmi_denominator
    
    # Define the output
    output = Output(bmi, "BMI", party3)
    
    # Return the output wrapped in a list (as required by the Nada DSL)
    return [output]
