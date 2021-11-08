# Python3 program for above approach

# Function to calculate roman equivalent


def intToRoman(num):

	# Storing roman values of digits from 0-9
	# when placed at different places
	m = ["", "M", "MM", "MMM"]
	c = ["", "C", "CC", "CCC", "CD", "D",
		"DC", "DCC", "DCCC", "CM "]
	x = ["", "X", "XX", "XXX", "XL", "L",
		"LX", "LXX", "LXXX", "XC"]
	i = ["", "I", "II", "III", "IV", "V",
		"VI", "VII", "VIII", "IX"]

	# Converting to roman
	thousands = m[num // 1000]
	hundereds = c[(num % 1000) // 100]
	tens = x[(num % 100) // 10]
	ones = i[num % 10]

	ans = (thousands + hundereds +
		tens + ones)

	return ans


# Driver code
if __name__ == "__main__":

	number = 3549

	print(intToRoman(number))

# This code is contributed by rutvik_56
# Python program to convert Roman Numerals
# to Numbers

# This function returns value of each Roman symbol


def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1


def romanToDecimal(str):
	res = 0
	i = 0

	while (i < len(str)):

		# Getting value of symbol s[i]
		s1 = value(str[i])

		if (i + 1 < len(str)):

			# Getting value of symbol s[i + 1]
			s2 = value(str[i + 1])

			# Comparing both values
			if (s1 >= s2):

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s1
				i = i + 1
			else:

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1

	return res


# Driver code
print("Integer form of Roman Numeral is"),
print(romanToDecimal("MCMIV"))
