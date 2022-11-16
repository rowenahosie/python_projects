print("Enter a decimal to convert to Roman numeral: ")
num = raw_input()

RomanList = ["M", "CM", "D", "CD", "C", "XC","L", "XL", "X","IX", "V", "IV", "I"]
DecimalList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

temp = int(num)
output_string = ""

for i, decimal in enumerate(DecimalList):
	while(temp>=decimal):
		temp -= decimal
		output_string += RomanList[i]

print(output_string)
