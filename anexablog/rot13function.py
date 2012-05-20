
def rot_13(input):
	firstList = []
	finalList= ""

	"""Check each character of the input string and add the ord conversion of it to 
	firstList if it is a-z or A-Z, otherwise just append the character as entered."""
	for c in input:
		if (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90): 
			firstList.append(ord(c))

		else:
			firstList.append(c)

	i = 0

	"""Check each item in firstList to see if it is in the range of a-z or A-Z, 
	if it is, then translate it, otherwise just append it to the finalList as is."""
	for each in firstList:
		if (97 <= each <= 122) or (65 <= each <= 90):
			if each <= 122 and each >= 97:
				if each > 109:
					firstList[i] -= 13
					
				else:
					firstList[i] += 13
					
				finalList += chr(firstList[i])

			if each <= 90 and each >= 65:
				if each > 77:
					firstList[i] -= 13
					
				else:
					firstList[i] += 13
					
				finalList += chr(firstList[i])
		
		else:
			finalList += each

		i += 1
	
	return finalList


