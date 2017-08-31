# coding=utf-8

import math

def floorSelect(floorlist):
	targetFloor = 0
	media = floorlist[0]
	Y = 0
	for tempIndex in range(1,len(floorlist)):
	
		Y = Y + (tempIndex)*floorlist[tempIndex]

	N3 = sum(floorlist[1:])
	N2 = floorlist[0]
	N1 = 0

	

	for index in range(1,len(floorlist)):
		if (N1 + N2 < N3):
				
			Y = Y + N1+ N2 -N3
			N1 = N1 + N2
			N2 = floorlist[index]
			N3 = N3 - floorlist[index]
			print(N1,N2,N3,Y)
			targetFloor = index
		else:
			break

	return (targetFloor,Y)


def mainInput():
	print("Please Input")
	floorStr = input().strip().split(" ")
	floorlist = [int(item) for item in floorStr]
	itemTwo = floorSelect(floorlist)
	print("电梯在%d 停, 最小需要走 %d" %(itemTwo[0]+1, itemTwo[1]))


mainInput()
	
