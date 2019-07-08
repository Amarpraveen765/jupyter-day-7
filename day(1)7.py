#!/usr/bin/env python
# coding: utf-8

# # Markdown Basics
# ## markdown basics
# ### Markdown Basics
# 
# *point1*(italic)
# **point2**(bold)
# ***point3***(bold an italic)
# 
# 
# 
# * normel text
#  * subtext1
#  * subtext2
#  
# > 1. point1
# > 2. poitn26
# 
# 
# * google Site -- [1]: http://www.google.com
# * msn Site -- [2]: http://www.msn.com
# 
# 
# - []option 1
# * google Site -- [google][1]
# [1]: http://www.google.com

# In[3]:


print("hello,gitam")
print("hyderabad")


# In[13]:


print("hello, gitam", "|||")
print("hyderabad", end=" ||| ")
print("python programming")


# In[7]:


print("hello, gitam ||| hyderbad ||| python programming")


# ### Assignments
# 

# In[10]:


n1 = 100 # single variable assignment
a = b = c = 20 # multiple variable assignment
a1,b1,c1 = 111,222,333 # multiple variable assignment 2
print(n1)
print(a,b,c)
print(a1,b1,c1)


# ### Data types and converstions
# * int
# * float
# * string

# In[26]:


n1 = 100;
s1 = "python"
s2 = 'p'
f1 = 10.2
print(a)
print(s1)
print(s2)
print(f1)
print(type(a)) # to find its data type
print(type(s1))
print(type(s2))
print(type(f1))
print("   ")
# or(all in one line)
print(a,s1,s2,f1)
print(type(a),type(s1),type(s2),type(f1))


# In[27]:


print("Hello world!\nHello world!")


# In[32]:


s1 = "100"
print(type(s1))
a = int(s1)
print(type(a))
print(a)
print("\n")
f = 1.5
a1 = int(f)
print(type(a1))
print(a1)


# In[33]:


# a number is give 1234 -
# digit count
a1 = 1234
print(len(str(a1)))


# ## reading a value
# ### * input("message") --string

# In[36]:


s1 = input("enter your name")
print(s1)
print(type(s1))


# In[38]:


# want a number as the input
s1 = int(input("enter a number"))
print(s1,"\t",type(s1))


# # operations
# 
# 
# 
# ### arithetic operators
# 
# * + 
# * -
# * *
# * /
# * //
# * %
# 
# **
# 
# 

# In[55]:


a = 1
print(a+10)
print(a-10)
print(a*10)
print(a/10) 
print(a%10)
print(a//10) # gives coefficent in int
print(a**10) #gives power of the number


# ### Procedence of arth operator 
# 
# * parenthesis (problem in th brackets) 
# * power
# * division
# * multiplication
# * addition
# * sub

# In[58]:


x = 1 + 2 ** 3 / 4 + 5
print(x)


# In[59]:


x = 1 + 2 ** 3 / 4 * 5
print(x)


# ## Relational operators
# 
# * ==
# * !=
# * greater than(>)
# * lesser than (<)
# * greater than equal to(>=)
# * lesser than equal to(<=)

# In[69]:


i = 100
a = (i>15) and (i<75)
b = (i>15) and (i<150)


# ## logical operators
#  
#  
# used to combine mor than singal comand
# 
# * and 
# * or 
# * not 

# In[62]:


# to check a given number is even or odd
n = int(input("enter a number"))
if n%2 == 0:
    print("even")
else:
    print("odd")
           


# In[67]:


# to check if given number is perfect multiple of 3 and 5
n = int(input("enter a number"))
if n%3==0 and n%5 == 0:
    print("yes")
else:
    print("no")


# In[74]:


# to check given number is positive,negative or zero
n = int(input("enter a number"))
if n>0:
    print("positive")
elif n==0:
    print("zero")
elif n<0:
        print("negative")
        


# In[2]:


# to check the greatest number
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if (a>b) and (a>c):
    print (a,"is greatest")
elif (b>a) and (b>c):
    print (b,"is greatest")
if (c>b) and (c>a):
    print (c,"is greatest")


# In[6]:


# to check if given year is leap year or not
y = int(input("enter the year"))
if (y%4==0) and (y%100!=0):
    print ("it is a leap year")
else:
    print ("it is not a leap year")


# ## while loop

# In[12]:


# print gitam 5 times 
print("gitam")
print("gitam")
print("gitam")
print("gitam")
print("gitam")
print("\nor using while loop ")
a=0
n = int(input("enter how many time u want to print ==\t"))
while a < n :
    print("gitam")
    a=a+1


# In[17]:


# print N natural numbers using while loop
a=1
n = int(input("enter the end number==\t"))
while a < n :
    print(a,end = " ")
    a=a+1


# In[24]:


# adding of even number from 1
a = 0
s = 0 
n = int(input("enter the end number==\t"))
while a <=n:
    print(a,end=" ")
    s = s + a
    a=a+2
print("\nsum of even numbers is =",s)    


# In[32]:


# given number is -- 123
# print the given number like -- 321
a = int(input("enter a number ==\t"))
b = a
s = 0
c=0
while a != 0:
    c= a % 10
    s= c + (s*10)
    a= a // 10
print(b,"\n",s)    


# ## functional programming
# * simple
# * easy read
# * Lengthy program divides into sub programs
def name of the function(<parameters>):
    statements
    return
# In[34]:


# sum of even numbers
def sumofeven(n):
    i=0
    sum=0
    while i<n:
        i=i+1
        if (i%2==0):
            sum=sum + i
    return(sum)
k=int(input("enter end number"))
l= sumofeven(k)
print(l)


# In[3]:


# read a number --1234
#Output --6 (2+4)
def addEvenDigits(n):
    sum=0
    while n!= 0:
        r=n%10
        if r%10 ==0:
            sum=sum+r
        n=n//10
    print(sum)    
    return
addEvenDigits(1234)


# In[9]:


# read a number --1234
#Output --6 (2+4)
def addEvenDigits(n):
    s=0
    while n!= 0:
        r=n%10
        if r%10 ==0:
            s=s+r
        n=n//10  
    return s
addEvenDigits(1234)


# In[7]:


# read a number -- 19528
# print the large digit print the number
def printlarge(n):
    large = 0
    while n != 0:
        r = n%10
        if large < r:
            large =r
        n = n// 10
    return large
printlarge(19528)
            


# In[6]:


# read the number input
# Output reverse of the given number
# 123 - 321
def reverseNumber(n):
    a = int(input("enter a number ==\t"))
    b = a
    s = 0
    c=0
    while a != 0:
        c= a % 10
        s= c + (s*10)
        a= a // 10
    return s
reverseNumber(123)         


# In[10]:


# given number is palendrome or not
# input
# 123 -- 321 No
# 121 -- 121 Yes
def palindrome(n):
   rev = 0
   buffer = n
   while n != 0:
       r =n%10
       rev = rev * 10 +r
       n = n // 10
   if buffer == rev:
       return "Yes"
   else:
       return "No"
   
print(palindrome(123))
print(palindrome(121))


# In[11]:


# function to print N natural Numbers
def NNaturalNumbers(n):
    for x in range(1,n+1):
        print(x,end=" ")
    return    
NNaturalNumbers(10)


# In[13]:


# function to print two numbers bitween two limits
# input: 11,25
# Output: 11,12,13...25
def printseries(lb,ub):
    for x in range(lb,ub+1):
        print(x,end=" ")
    return    
printseries(11,25)


# In[15]:


# function to print alternate number
# [500,520] -- 500 502 504 506..... 520
# [100,150] -- 100 102 104 106 ..150
def alternateNumbers(lb,ub):
    for x in range(lb,ub+1,4):
        print(x,end=" ")
    return    
alternateNumbers(500,520)
print("\n")
alternateNumbers(100,150)        


# In[18]:


# function to print the serice in reverse
# input 1,10
# Output: 10,9,8,7....1
def reverserange(start,end):
    for x in range(end,start-1,-1):
        print(x,end=" ")
    return
reverserange(1,10)


# In[8]:


# given number is prime 
def isprime(n):
    flag = True
    for i in range(2,n//2+1):
        if n %i==0:
            flag = False
            return flag
    return flag
isprime(3)
    


# In[27]:


# find factors of given number
# 12.....> 1 2 3 4  6 12
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
    return
factors(12)


# In[14]:


# function to find prime number count from 1 to n
def prime(n):
    cnt=0
    for a in range(2,n+1):
        k = 0
        for i in range(2,a//2+1):
            if a % i== 0:
                k = k + 1
            if (k<=0):
                cnt=cnt+1
    return cnt
prime(10)    
        
    


# In[18]:


# individual digit factorial sum is same as original number
def fact(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact
def factsum(n):
    sum=0
    a=n
    while n!=0:
        r=n%10
        sum=sum+fact(r)
        n=n//10
    if (sum==a):
        return "YES"
    else:
        return "NO"
    return
factsum(145)
        
    
    
    
    
    
    
 


# In[26]:


# function to return the count of palindrome number two limits
# Input : 1 10
# Output : 9 (1,2,3,4,5,6,7,8,9)

# Input : 11 100
# Output : 9(11,22,33,44,....,99)

def ispalindrome(n):
    rev=0
    buffer = n
    while n!=0:
        r = n % 10
        rev = rev *10 + r
        n= n// 10
    if rev == buffer:
        return True
    else:
        return False
    return
def count(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if ispalindrome(lb) == True:
            cnt = cnt + 1
        lb =lb +1
    return cnt 
count(11,100)


# In[28]:


# function to generate the perfect numbers in a given range
# perfect number : sum of all its same as the original number 
# Example : 6 -- 123(1+2+3)
#Input : 1 10
# Output : 6
def factors(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum =sum+ i
    return sum
def isperfect(n):
    if factors(n) == n:
        return True
    return False
def generateperfect(lb,ub):
    for x in range(lb,ub+1):
        if isperfect(x):
            print(x,end=" ")
    print()
    return
generateperfect(1,10)
generateperfect(1,10000)


# # strings

# In[34]:


s='praveen'
print(s[0])
print(s[3])
print(s[-1]) # Another way to acess last charecter
print(s[len(s)-1]) # Aother way to acess last charecter
print(s[-4])
print(s[0:2]) # Access the first characters
print(s[-3:]) # last three characters
print(s[2:])


# In[38]:


s='praveen'
print(s[1:-1]) # printing all characters except first and last
print(s[len(s)//2]) # Middle of the string
print(s[-1::-1]) # Reverse of the string
print(s[-1:-3:-1]) # accessing lat two characters in revers order
      # accesing characters in revers order
print(s[:2]) # two characters 
print(s[::3]) # Three characters 


# In[40]:


def reversestring(str):
    return str[-1::-1]
reversestring("programming")


# In[39]:


def ispalindrome(str):
    if str == str[::-1]:
        return True
    else:
         return False
    return
print(ispalindrome("praveen"))
print(ispalindrome("nivin"))


# In[44]:


# Function to print upper case characters
# Exampl : Python -- P
#ASCII :-
# A - Z : 65 -90
# a - z : 97 - 122
# 0 - 9 : 48 -57
# Space : 32
def printupper(x):
    for i in range(len(x)):
        if ord(x[i]) >=65 and ord(x[i]) <=90:
            print(x[i],end=" ")
    return
printupper("PyThon")


# In[45]:


ord('A') # it gives the ascii value of the character


# In[46]:


# Function to print "Python" if the count of 
# Upper and lower case is same 
# Print "programming" if not same 
# Example :-  PyThOn -- 3 P T O(Upper case) -- same count
#                       3 y h n (Upper case)
# PytHon -- P H (2)
#        -- y t o n (4) -- programming
def findcount(str):
    cntupper = 0
    cntlower = 0
    for x in range(len(str)):
        if ord(str[x]) >=65 and ord(str[x]) <=90:
            cntupper =cntupper+1
        elif ord(str[x]) >=97 and ord(str[x]) <=122:
            cntlower = cntlower + 1 
    if cntupper == cntlower:
        return "same count"
    else:
        return "programming"
    return
print(findcount('PyThOn')) # same count
print(findcount('PYTHOn')) # programming
            


# In[49]:


# extract digits form given string
# Example :
# Input : Appli1cat8ion89
# output : 1 8 8 9
def extractdigits(str):
    for x in range(len(str)):
        if ord(str[x]) >=48 and ord(str[x]) <=57:
            print(str[x],end=" ")
    return
extractdigits("AppLi1cat8ion89") # 1 8 8 9


# In[52]:


# function to return the sum of digits in a given string
#Example:
#Input : Appli1cat8ion89
# Output : 26(1+8+8+9)
# 0 1 2 3 4 5 ..9
# 48 49 50 51 52 53 ....57
def sumofdigits(str):
    sum =0
    for x in range(len(str)):
        if ord(str[x]) >= 48 and ord(str[x]) <=57:
            sum =sum +(ord(str[x])-48)
    return sum
sumofdigits('Appli1cat8ion89')
        


# In[53]:


# function to return the sum of digits in a given string 2
#Example:
#Input : Appli1cat8ion89
# Output : 16(8+8)
def sumofevendigits(str):
    sum =0
    for x in range(len(str)):
        if ord(str[x]) >= 48 and ord(str[x]) <=57:
            if (ord(str[x])-48) % 2 ==0:
                sum =sum +(ord(str[x])-48)
    return sum       
sumofevendigits('Appli1cat8ion89')


# In[54]:


# function to print the specific word in upper case 
# example :
# input : Python made Easy
# output : MADE 
# input : learn Python Programming
#output : PYTHON
def worduppercase(s):
    spacecnt =0 
    for x in range(len(s)):
        if ord(s[x]) ==32:
            spacecnt += 1 # spacecnt = spacecnt+1
        if spacecnt ==1:
            if ord(s[x]) >=65 and ord(s[x]) <=90:
                print(s[x],end=" ")
            elif ord(s[x]) >=97 and ord(s[x]) <=122:
                print(chr(ord(s[x])-32),end=" ")
        if spacecnt ==2:
            break
    return
worduppercase('Python made Easy') # MADE


# In[ ]:




