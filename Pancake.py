# coding=utf-8

count = 0

def PancakeSort():
	#多行注释
	"""
	多行注释
	"""
	print("Please input\n")
	strLen = input()
	intList = input().strip().split(" ")
	GoalList = [int(item) for item in intList]
	#print(strLen,intList)
	#print(type(strLen),GoalList)
	if len(GoalList) != int(strLen):
		print("input Error")
		return 0
	mainSort(GoalList)


def mainSort(GoalList):
	global count
	tempIndex = maxIndex(GoalList)
	if len(GoalList) == 1:
		print("Done 第%d次 最上层一个 %s\n" % (count, str(GoalList)))
		return 0
	if tempIndex == len(GoalList) - 1:
		tempitem = GoalList[tempIndex]
		count = count + 1
		print("第%d次 大小顺序 %s最大的饼%d在最底层，不用反转，缩小范围\n" % (count,str(GoalList),GoalList[tempIndex]))
		GoalList.remove(tempitem)
		print("剩余的饼层 %s\n" % str(GoalList))
		mainSort(GoalList)
	elif tempIndex == 0:
		tempitem = GoalList[tempIndex]
		count = count + 1
		print("第%d次 大小顺序 %s最大的饼%d在最上层，全体反转\n" % (count,str(GoalList),GoalList[tempIndex]))
		GoalList.remove(tempitem)
		GoalList.reverse()
		print("剩余的饼层 %s\n" % str(GoalList))
		mainSort(GoalList)
	else:
		count  = count + 1
		print("第%d次 大小顺序 %s最大的饼%d在中间，从上到中间反转\n" % (count,str(GoalList),GoalList[tempIndex]))
		tempitem = GoalList[tempIndex]
		templist = []
		templist = GoalList[:tempIndex+1]
		#最大的饼在中间,需要反转两次
		templist.reverse()
		GoalList = templist+GoalList[tempIndex+1:]
		count = count +1
		GoalList.reverse()
		print("第%d次 中间调整后 大小顺序 %s 然后整体结合反转\n" %(count, str(GoalList)))
		GoalList.remove(tempitem)
		print("剩余的饼层 %s\n" % str(GoalList))
		mainSort(GoalList)

def maxIndex(GoalList):
	return GoalList.index(max(GoalList))

"""
def judgeSort(list):
	bool = False
	for num in range(len(list)-1):
		if list[num] > list[num+1]:
			break
		bool = True
	return  bool
"""

PancakeSort()
