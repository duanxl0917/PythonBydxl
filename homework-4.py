#逆序读取的数字
# a = [1,5,7,3,2]
# print(sorted(a,reverse=True))
#分析成绩
# def achievement(ach):
#     achievement = ach.split(' ')
#     sum_ = 0
#     count = 0
#     for i in achievement:
#         i = int(i)
#         sum_=sum_ + i
#         count += 1
#     average = sum_ / count
#     print(average)
#     count_1 = 0
#     count_2 = 0
#     for i in achievement:
#         i = int (i)
#         if i >= average :
#             count_1+=1
#         else :
#             count_2+=1
    
#     print('低于平均分数的有%d个'%count_2)
#     print('大于、等于平均分数的有%d个'%count_1)

# ach=input('请输入分数:')
# achievement (ach) 
#统计单个数字
# import random
# ls = list()
# ls = [random.randint(0,9) for i in range(1000)]
# st = set(ls)
# for i in st:
#     print(i,"出现的次数：",ls.count(i))
#找出最小元素
# list = [10, 20, 1, 45, 99]
# list.sort()
# print("最小元素为:", *list[:1])
#冒泡排序
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j] 
# arr = [65, 33, 25, 12, 22, 11, 90]
# bubbleSort(arr)
# for i in range(len(arr)):
#     print ("%d" %arr[i])
#消除重复
# list1 = input("Enter list: ")
# list2 = []
# [list2.append(i) for i in list1 if not i in list2]
# print(list2)
#统计字符串中的字母个数
# str=input('输入字符串：')
# resoult={}
# for i in str:
#     resoult[i]=str.count(i)
#     print(resoult)
#反向字符串
# s='helloword'
# a=list(s)
# a.reverse()
# print("".join(a))   
# print("".join(a[::-1]))