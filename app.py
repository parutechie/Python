#Simple Python Program for Converting KiloGram(kg) to Pounds or Converting Pounds to KiloGram(kg) Using "if else statement"
weight = int(input("Weight: "))
unit = input("(L)bs or (k)g: ")
if unit.upper() == "L":
    converter = weight * 0.45
    print(f"yor are {converter} Kilos")
else:
    converter = weight // 0.45
    print(f"you are {converter} pounds")
