print("Enter a decimal to convert to Roman numeral: ")
num = raw_input()

RomanList = ["X", "V", "I"]
DecimalList = [10, 5, 1]

#print(RomanDecimalMap[numeral])

temp = int(num)
output_string = ""
while(temp>0):
	for i, decimal in enumerate(DecimalList):
		if(temp>=decimal):
			temp -= decimal
			output_string += RomanList[i]

print(output_string)
