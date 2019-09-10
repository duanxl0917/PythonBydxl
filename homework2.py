#1.一个五边形的面积
#import math
#r = eval(input("Enter the length from the center to a vertex:"))
#s = 2 * r * math.sin(math.pi / 5)
#area = 5 *s ** 2 / (4 * math.tan(math.pi / 5))
#print("The area of the pentagon is %.2f" %area  )
#2.大圆距离
#import math
#x1,y1 = eval(input("Enter point 1 (latiude and longitude) in degress: "))
#x2,y2 = eval(input("Enter point 2 (latiude and longitude) in degress: "))
#radius = 6371.01
#x11 = math.radians(x1)
#y11 = math.radians(y1)
#x22 = math.radians(x2)
#y22 = math.radians(y2)
#d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
#print("The distance between the two points is %.11f km" %d)
#3.五角星的面积
#import math
#s = eval(input("Enter the side:"))
#area = 5 * s ** 2 / (4 * math.tan(math.pi / 5 ))
#print ("The area of the pentagon is %.14f"%area)
#4.一个正多边形的面积
#import math
#n = eval(input("Enter the number of sides: ")) 
#s = eval(input("Enter the side: "))
#area = n * s ** 2 / (4 * math.tan(math.pi / n ))
#print ("The area of the polygon is %.14f"%area)
#5.找出ASCII字符
#a = eval(input("Enter an ASCII code："))
#b = chr(a)
#print("The character is",b )
#6.工资表
#name = input("Enter employee’s name:")
#hours = eval(input("Enter number of hours worked in a week:"))
#PayRate = eval(input("Enter hourly pay rate:"))
#federalRate = eval(input("Enter federal tax withholding rate:"))
#stateRate = eval(input("Enter  input state tax withholding rate:"))
#Federal = hours * PayRate * federalRate
#State = hours * PayRate * stateRate
#Gross = hours * PayRate
#NetPay = hours * PayRate - Federal - State
#Total = Federal + State
#print("Employee Name:",name)
#print("Hours Worked:",hours)
#print("Pay Rate:$",PayRate)
#print("GrossPay:$",Gross)
#print("Deductions:")
#print("\t Federal withholding (20.0%):$",Federal) 
#print("̲\t State withholding(9.0%):$",State)
#print("\t Total Deduction:$" ,Total)
#print("NetPay:$" ,NetPay)
#反向数字
#num = int(input("Enter an integer:"))
#i = 0
#num1 = num
#while True:
#    if num1 // 10 == 0:
#        break
#        i += 1
#        num1 = num1 // 10
#        sum = 0
#while i >= 0:
#    sum = sum + (num % 10) * (10 ** i)
#    num = num // 10
#    i = i - 1
#    print("The reversed number is :",sum)
#解一元二次方程
#import math
#a,b,c = map(float,input("Enter a,b,c：").split(","))
#jisuan = b*b-4*a*c
#if jisuan >0:
#   r1=(-b+math.sqrt(b*b-4*a*c))/ 2*a
#   r2=(-b-math.sqrt(b*b-4*a*c))/ 2*a
#   print("the roots are  {}  and {}  ".format(r1,r2))
#elif jisuan == 0:
#   r1=(-b+math.sqrt(b*b-4*a*c))/ 2*a
#   print(r1)
#else:
#   print("the equation has no real roots")
#学习加法
#import random
#a=random.randrange(0,100)
#a1=random.randrange(0,100)
#print(a,a1)
#he = float(input("计算这两个数的和并输入："))
#he1=a+a1
#if he==he1:
#    print("true")
#else:
#    print("flase")
#找未来数据
#today=int(input("Enter today's day:"))
#wl=int(input('Enter the number of days slapsed since today:'))
#s=(today+wl)%7
# if today==0 :
#     xq='Sunday'
# elif today==1 :
#     xq='Monday'
# elif today==2 :
#     xq='Tuesday'
# elif today==3 :
#     xq='Wednesday'
# elif today==4 :
#     xq='Thursday'
# elif today==5 :
#     xq='Friday'
# elif today==6 :
#     xq='Saturday'

# if  s==0:
#     xt='Sunday'
# elif  s==1:
#     xt='Monday'
# elif  s==2:
#     xt='Tuesday'
# elif  s==3:
#     xt='Wednesday'
# elif  s==4:
#     xt='Thursday'
# elif  s==5:
#     xt='Friday'
# elif  s==6:
#     xt='Saturday'
# print('Today is %s and the fulture day day is %s'%(xq,xt))
#对三个整数排序，升序显示
# a,b,c=map(int,(input('输入三个数: ').split(',')))
# if a>b and a>c :
#     if b>c:
#         print(c,b,a)
#     else:
#         print(b,c,a)
# if b>a and b>c:
#     if a>c:
#         print(c,a,b)
#     else:
#         print(a,c,b)
# if c>a and c>b:
#     if a>b:
#         print(b,a,c)
#     else:
#         print(a,b.c)
# if a==b==c:
#     print('a=b=c')
#比较价钱
# price1,weight1=map(float,(input('Enter weight and price for package1: ').split(',')))
# price2,weight2=map(float,(input('Enter weight and price for package2: ').split(',')))
# better1 = price1 / weight1
# better2 = price2 / weight2
# if better1 > better2:
#     print('package1 has the better price')
# if better2 > better1:
#     print('package2 has the better price')
# else:
#     print('package1 and package2 have the same price')
#头或尾
# import random
# a=int(input('输入0或者1：'))
# yingbi=random.randrange(0,2)
# if yingbi==1:
#     print('猜对了')
# else:
#     print('猜错了')
#剪刀、石头、布
# import random
# jisuanji = random.randrange(0,3)
# yonghu = int(input('输入0或1或2:'))
# if jisuanji ==0 and yonghu == 1:
#     print('用户赢')
# if jisuanji ==0 and yonghu == 2:
#     print('计算机赢')
# if jisuanji ==1 and yonghu == 0:
#     print('计算机赢')
# if jisuanji ==1 and yonghu == 2:
#     print('用户赢')
# if jisuanji ==2 and yonghu == 0:
#     print('用户赢')
# if jisuanji == 2 and yonghu == 1:
#     print('计算机赢')
# if jisuanji == yonghu:
#     print('平局')
#一周的星期几
# year=int(input('Enter year:(e.g..2008):'))
# mouth=int(input('Enter month:1-12:'))
# day=int(input('Ener the day of the month:1-31 :'))
# j=int(year/100)
# k=year%100
# if mouth==1 or mouth==2:
#     year-=1
#     mouth+=12
#     j=int(year/100)
#     k=year%100
#     h=(day+(26*(mouth+1)/10)+k+(k/4)+(j/4)+5*j)%7
    
# else:
#     j=int(year/100)
#     k=year%100
#     h=(day+(26*(mouth+1)/10)+k+(k/4)+(j/4)+5*j)%7

# if h==0 :
#         print('Day of the week is Saturday')
# elif h==1 :
#         print('Day of the week is Sunday')
# elif h==2 :
#         print('Day of the week is Monday')
# elif h==3 :
#         print('Day of the week is Tuesday')
# elif h==4 :
#         print('Day of the week is Wednesday')
# elif h==5 :
#         print('Day of the week is Thursday')
# else :
#         print('Day of the week is Friday')
#选出一张牌
# import numpy as np
# res1 = np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','jack','Queen','King'])
# res2 = np.random.choice(['梅花','红桃','方块','黑桃'])
# print('the card you picked is the {} of {}'.format(res1,res2))
#回文数
# number = int(input('Enter a three-difit integer: '))
# number1=number%10
# number2=number//100
# if number1==number2:
#     print('{} is a palindrome'.format(number))
# else:
#     print('{} is not a palindrome'.format(number))
#计算三角形的周长
# a,b,c = map(int,(input('Enter three edges: ').split(',')))
# d = a+b+c
# if a+b>c and a+c>b and b+c>a:
#     print('The perimeter is {}'.format(d))
# else:
#     print('不能构成三角形')
#统计正负数个数并计算平均值
# def c():
#     zheng = 0
#     fu = 0
#     sum_ = 0
#     cishu = 0
#     d = 1
#     while d !=0 :
#         d = eval(input("Enter an integer,the input ends if it is 0:"))
#         if d > 0:
#             zheng += 1
#         if d < 0:
#             fu += 1
#         sum_ += d
#         if d != 0:
#             cishu += 1
    
#     print(zheng)    
#     print(fu)
#     print(sum_ / cishu)
# c()
#计算未来学费
# def b():
#     dollar = 10000
#     for i in range(14):
#         dollar = dollar * 0.05 + dollar
#         if i == 9:
#             print(dollar)
#     print(dollar)
# b()
#指出可被5和6同时整除的数
# def c():
#     count = 0
#     for i in range(100,1001):
#         if i %5==0 and i % 6 == 0:
#             print(i,end=" ")
#             count += 1
#             if count % 10 == 0:
#                 print()
# c()