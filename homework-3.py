#1.五角数
# def getPentagonalNumber(n):
#     count = 0
#     for i in range(1,n + 1):
#         wjs=int(i * (3 * i - 1) / 2)
#         print("%.f"%wjs,end=" ")
#         count += 1
#         if count % 10 == 0:
#             print("")
# getPentagonalNumber(100)
#2.求一个整数各个数字的和
# def sumDigits(n):
#     sum=0
#     ge=0
#     while n >= 10:
#         ge = n % 10
#         n = int (n // 10)
#         sum += ge
#         print(n+sum)
# sumDigits(256)
#3.对三个数排序
# def displaySortedNumbers(num1,num2,num3):
#     x = [num1,num2,num3]
#     for i in range(3):
#         for j in range(2):
#             if(x[j] > x[j+1]):
#                 t = x[j]
#                 x[j] = x[j+1]
#                 x[j+1] = t
#     return x
# num1,num2,num3 = eval(input("Enter three number: "))
# x = displaySortedNumbers(num1,num2,num3)
# print("The sorted numbers are",x[0],x[1],x[2])
#4.计算未来投资值
# sum=0
# def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
#     global sum
#     sum = investmentAmount * (1 + monthlyInterestRate * 0.01 / 12) ** years
#     return sum
# amount = int(input("The amount invested : "))
# rate = int(input("Annual interest rate : "))
# count = 0
# print("Years Future Value")
# for i in range(1,361):
#     count += 1
#     if(count == 12):
#         print(" %d %.2f"%(i/12,futureInvestmentValue(amount,rate,i)))
#         count =0
#5.显示字符
# def printChars(ch1,ch2,numberPerLine):
#     count=0
#     while ch1 != chr(ord(ch2)+1):
#         print(ch1,end=" ")
#         i=ord(ch1)
#         i += 1
#         ch1=chr(i)
#         count += 1
#         if count % numberPerLine == 0:
#             print("")
# printChars('I','Z',10)
#6.一年的天数
# def numberOfDayInYear(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('%d年有%d天'%(year,366))
#     else:
#         print('%d年有%d天'%(year,365))

# for year in range(2010,2021):
#     numberOfDayInYear(year)
#9.当前时间和日期
# def time():
#     import time
#     print(time.strftime("Current date and time is %b %d, %Y %H:%M:%S", time.localtime()))
# time()
#10.掷骰子
# import random
# def dice(x,y):
#     win = [7,11]
#     lose = [2,3,12]
#     other = [4,5,6,8,9,10]
#     count = 0
#     if(x+y in lose):
#         print("You lose")
#     elif(x+y in win):
#         print("You win")
#     elif (x+y in other):
#         count += 1 
#         print("point is %d"%(x+y))
#         num1 = random.randint(1,6)
#         num2 = random.randint(1,6)
#         print("You rolled %d + %d = %d"%(num1,num2,num1+num2))
#         while num1+num2 != x+y or num1+num2 != 7:
#             if num1+num2 == 7:
#                 print("You lose")
#                 break
#             if num1+num2 == x+y:
#                 print("You win")
#                 break
#             num1 = random.randint(1,6)
#             num2 = random.randint(1,6)
#             print("You rolled %d + %d = %d"%(num1,num2,num1+num2))

# x = random.randint(1,6)
# y = random.randint(1,6) 
# print("You rolled %d + %d = %d"%(x,y,x+y))
# dice(x,y)