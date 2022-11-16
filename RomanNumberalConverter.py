print("Enter a decimal to convert to Roman numeral: ")
num = raw_input()

RomanList = ["X","IX", "V", "IV", "I"]
DecimalList = [10, 9, 5, 4, 1]

temp = int(num)
output_string = ""

for i, decimal in enumerate(DecimalList):
	while(temp>=decimal):
		temp -= decimal 
		output_string += RomanList[i]

print(output_string)
