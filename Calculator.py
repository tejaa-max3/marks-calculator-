name = input("Naam: ")
maths = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))
social = int(input("Social Science: "))
geography = int(input("Geography: "))

total = maths + science + english + social + geography
percentage = total / 5

print("Hello", name)
print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Topper!")
elif percentage >= 60:
    print("very goodd!")
else:
    print("do ur best dear!")
