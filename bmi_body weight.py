weight=float(input("enter weight in kg"))
height=float
bmi = weight / height ** 2
if bmi<18.5:
    print(f"your BMI is {bmi} and you are under weight".)
elif bmi<25:
    print(f"your BMI is {bmi} and you are normal weight".)
elif bmi<30:
    print(f"your BMI is {bmi} and you are over weight".)
elif bmi<35:
    print(f"your BMI is {bmi} and you are under obese".)
else:
    print(f"your BMI is {bmi} and you are under weight".)