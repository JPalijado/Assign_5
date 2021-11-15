def GetAge():
    age = int(input("Input Age: "))
    return age

def DisplayOutput(age):
    if age >= 0 and age <= 12:
        print("Life Stage: Kid")
    elif age >= 13 and age <= 17:
        print("Life Stage: Teen")
    elif age == 18:
        print("Life Stage: Debut")
    else:
        print("Life Stage: Adult")

age = GetAge()

DisplayOutput(age)
