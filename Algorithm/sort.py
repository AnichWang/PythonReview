# 冒泡排序
def bubble_sort(testList):
    for i in range(len(testList)):
		for j in range(i, len(testList)):
			if testList[i]>testList[j]:
				temp = testList[i]
				testList[i] = testList[j]
				testList[j] = temp
	print(testList)

#插入排序


#希尔排序

#快速排序

#直接选择排序

#堆排序

#归并排序

#基数排序

if __name__ == "__main__":
	testList = [9,8,7,6,5,4,3,2,1,0]
	bubble_sort(testList)