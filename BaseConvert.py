import math

strTag = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUNWXY".strip())

def Convert10Base(srcBase, numStr):
	global strTag
	numBase10 = 0	
	i = 0
	for item in numStr:
		index = strTag.index(item)
		numBase10 = numBase10 + index*math.pow(srcBase, len(numStr)-1-i)
		i = i + 1
	return numBase10

def ConvertDesBase(desBase, numBase10):
	global strTag
	numBaseDes = []
	if(numBase10 == 0):
		numBaseDes.append(strTag[numBase10])
		return ''.join(numBaseDes).reverse
	while(numBase10 !=0):
		k = int(numBase10 / desBase)
		if(k ==0):
			left =int(numBase10)
			numBaseDes.append(strTag[left])
			print(left)
			break
		else:
			left = int(numBase10 % desBase)
			print(left)
			numBaseDes.append(strTag[left])
			numBase10 = k
	return numBaseDes[::-1]

def mainInput():
	inputList = input().strip().split(" ")
	srcBase = int(inputList[0])
	desBase = int(inputList[1])
	numStr = inputList[2]
	if(srcBase > 62 or srcBase <2 or desBase >62 or desBase <2):
		print("Error")
		return 0
	if(srcBase == desBase):
		print(numStr)
		return 0
	else:
		numBase10 = Convert10Base(srcBase,numStr)
		print(''.join(ConvertDesBase(desBase,numBase10)))
		return 0
mainInput()	
