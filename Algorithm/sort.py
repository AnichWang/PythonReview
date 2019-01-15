
#冒泡排序
def bubble_sort(list):
	for i in range(len(list)):
		for j in range(i, len(list)):
			if list[i]>list[j]:
				temp = list[i]
				list[i] = list[j]
				list[j] = temp
    print(list)

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