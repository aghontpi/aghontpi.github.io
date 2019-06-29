import operator
toDecode = [17488, 16758, 16599, 16285, 16094, 15505, 15417, 14832, 14450, 13893, 13926, 13437, 12833, 12741, 12533, 11504, 11342, 10503, 10550, 10319, 975, 1007, 892, 893, 660, 743, 267, 344, 264, 339, 208, 216, 242, 172, 74, 49, 119, 113, 119,106]

def checkprime(num):
	flag=True
	for x in range(3,(int(num/2))+1):
		if(num%x==0):
			flag=False
	return flag


def primeNumberGenerator():
	primeNumberArr = [2,3,5,7]
	for x in range(10,17488):
		if(checkprime(x)):
			primeNumberArr.append(x)
	return primeNumberArr

def filterPalindromeFromPrime(primeNumberArr):
	primePalindrome = []
	for x in primeNumberArr:
		if (str(x) == str(x)[::-1]):
			primePalindrome.append(x)
	return primePalindrome

def decode(PrimePalindromeArr):
	toDecode.reverse()
	url = []
	print("toDecode Count:" +str(len(toDecode)))
	print("PrimePalindromeArr Count:" +str(len(PrimePalindromeArr)))
	for index, value in enumerate(toDecode):
		character = operator.xor(PrimePalindromeArr[index],value)
		print("palindromeValue:"+str(PrimePalindromeArr[index]))
		print("value:"+str(value))
		print("character:"+chr(character))
		url.append(chr(character))

	print("url:"+"".join(url))



if __name__ == '__main__':
	primeArr = primeNumberGenerator()
	PrimePalindromeArr = filterPalindromeFromPrime(primeArr)
	decode(PrimePalindromeArr)