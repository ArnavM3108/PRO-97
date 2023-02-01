year = int (input ("Enter any year that is to be checked for leap year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
         if (year % 400) == 0:
            print ("The given year is a leap year")
         else:
            print ("It is not a leap year")
    else:
        print ("It is not a leap year")
else:
    print ("It is not a leap year")

# ========================================================================================================
centimetre=int(input("Enter the height in centimeters..."))
inches=0.394*centimetre
feet=0.0328*centimetre
print("The length in inches is ")
print(round(inches,2))
print("The length in feet is")
print(round(feet,2))