print("Enter a Roman Numeral to convert to decimal: ")
numeral = raw_input()

RomanDecimalMap = {
	"I" : 1,
	"V" : 5,
	"X" : 10
}

print(RomanDecimalMap[numeral])

