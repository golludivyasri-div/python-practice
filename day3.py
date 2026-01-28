#CONDITIONAL STATEMENTS
#IF condition
#age=18
#if age>=18:
#    print("eligible")
#IF-ELSE condition
#balance=500
#amount=300
#if balance>=amount:
#    print("payment successful")
#else:
#    print("unsuccessful")
#marks=75
#if marks>=90:
#    print("grade A")
#elif marks>=60:
#    print("grade B")
#else:
#    print("grade c")
#EXAMPLES
#EVEN OR ODD 
#num=7
#if num%2==0:
#    print("even")
#else:
#    print("odd")
#NEGATIVE OR POSITIVE OR ZERO
#num=-5
#if num>=0:
#       print("positive")
#elif num<0:
#       print("negative number")
#else:
#       print("zero")
#LOGIN CHECK
#username = "divya"
#password = "1234"
#if username == "divya" and password == "1234":
#    print("login successful")
#else:
#    print("login unsuccessful")
#LOOPS
#FOR LOOP:used when number of iterations known
#for i in range(1,6):
#    print(i)
#WHILE LOOP:use when condition control repetition
#i=2
#while i<=10:
#   print(i)
#    i+=1
#CONDITIONAL LOOP STATEMENTS:BREAK,CONTINUE,PASS
#break
#for i in range(5):
#    if i == 3:
#        break
#    print(i)
#NESTED LOOPS:loop inside another loop
#for i in range(3):
#    for j in range(2):
#        print(i,j)
#EXAMPLES
#GREATEST OF 3 NUMBERS
#a=int(input("enter a:"))
#b=int(input("enter b:"))
#c=int(input("enter c:"))
#if a>=b and a>=c:
#    print("greatest a:",a)
#elif b>=a and b>=c:
#    print("greatest b:",b)
#else:
#    print("greatest c:",c)
#LEAP year
#year = int(input("enter year:"))
#if (year%400==0) or (year%4==0 and year%100!=0):
#    print("leap year")
#else:
#    print("not a leap year")
#PRINT 1 TO N
#n = int(input("Enter N: "))
#for i in range(1, n + 1):
#   print(i)
#LOOPS:Even numbers
#n = int(input("Enter N: "))
#for i in range(1, n + 1):
#    if i % 2 == 0:
#        print(i)
#SUM OF FIRST N numbers
#n = int(input("Enter N: "))
#total = 0
#for i in range(1, n + 1):
#   total += i
#print("Sum:", total)
#MULTIPLICATION TABLE
#n = int(input("Enter number: "))
#for i in range(1, 11):
#    print(n, "x", i, "=", n * i)
#REVERSE A NUMBER
#n = int(input("Enter number: "))
#rev = 0
#while n > 0:
#    rev = rev * 10 + n % 10
#    n = n // 10
#print("Reversed number:", rev)
#PRIME NUMBER OR NOT
#n = int(input("Enter number: "))
#is_prime = True
#if n <= 1:
#    is_prime = False
#else:
#    for i in range(2, n):
#        if n % i == 0:
#            is_prime = False
#            break
#if is_prime:
#    print("Prime")
#else:
#    print("Not Prime")
#PALINDROME
#n=int(input("enter number:"))
#temp=n
#rev=0
#while n>0:
#    rev=rev*10+n%10
#  n=n//10
#if temp==rev:
#    print("palindrome")
#else:
#    print("not palindrome")
#ARMSTRONG
#n = int(input("Enter number: "))
#temp = n
#sum = 0
#while n > 0:
#    digit = n % 10
#    sum += digit ** 3
#    n = n // 10
#if sum == temp:
#    print("Armstrong")
#else:
#    print("Not Armstrong")
