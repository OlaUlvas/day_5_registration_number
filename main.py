import random

letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

country = input("\nVill du ha ett danskt eller ett svenskt registreringsnummer till bilen (D/S)?: \n").lower()

swe_reg = ""
den_reg = ""

if country == "d":
    for char in range(0, 2):
        den_reg += random.choice(letter)
    den_reg += " "
    for number in range(0, 5):
        den_reg += random.choice(numbers)

    print("Ditt danska registreringsnummer är:")
    print(den_reg)

elif country == "s":
    for char in range(0, 3):
        swe_reg += random.choice(letter)
    swe_reg += " "
    for number in range(0, 3):
        swe_reg += random.choice(numbers)

    print("Ditt svenska registreringsnummer är:")
    print(swe_reg)

else:
    print("wrong input!")