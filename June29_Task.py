# Task 1

#Get one string from user
#identify the middle character of the string

my_str = "python"
new= (len(my_str)// 2)
print(my_str[new])

##############################################
"""
Task2:

string1: ***python***
string1: **python********
string: ********java*******

output: python  (strip,rstrip,lstrip method *)
"""

string1= "***python***"
print(string1.strip())
print(string1.rstrip())
print(string1.lstrip("*"))

string = "********java*******"
print(string.strip())
print(string.rstrip())
print(string.lstrip("*"))

#########################################################
"""
Task3: (name<space>float)
collect three strings from user  name<space>float
string1: "ravi 10.30"  
string2: "meghala 12.19"
string3: "Gokul 20.20"
split + indexing
10.30 + 12.19 + 20.20 ===> output ===> round (42.69000) 5 decimal places should be (format)

"""
string1= "ravi 10.30"  
string2= "meghala 12.19"
string3= "Gokul 20.20"
a = string1.split()
b = string2.split()
c = string3.split()
a1 = (a[1])
#print(type(a1))
f1 = float(a1)
#print(type(f1))
b1 = (b[1])
f2 = float(b1)
#print(b1)
c1 = (c[1])
f3 = float(c1)
sum = f1+f2+f3
final = round(sum,5)
print(final)

###########################################################


#Task4:

"""
#collect two strings from user

string1: python
String2: java

output ===> jythonpava64hv

string1: maths
string2: science

output ===> sathsmcience57te
"""

string1 = "python"
new_string = string1.replace("p", "j")
print(new_string)

string2 = "java"
new_string2 = string2.replace("j","p")
print(new_string2)


sum1 = (new_string + new_string2)


len1 = str(len(string1))
len2 = str(len(string2))


ind1 = (len(string1) // 2)
new_ind1 = string1[ind1]
print(new_ind1)


ind2 = (len(string2)//2)
new_ind2 = string2[ind2]
print(new_ind2)


print(new_string + new_string2 + len1 + len2 + new_ind1 + new_ind2 )

####################################################################


#Task5:
"""
Collect two strings from user

string1: wikipedia
string2: typescript

output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
(ord , chr)

"""

string1 = "wikipedia"
string2 = "typescript"

p1 = len(string1)//2
p= (string1[p1])
print(p)


c1 = len(string2)// 2
c = (string2[c1])
print(c)

sum1 = (ord(p)+ord(c))
#sum2 = (chr(p)+chr(c))
#print(sum1)
print("ascii value of p + ascii value of c is:", sum1)

###############################################

#Task6:
"""
collect one string from user:

string: computer
output: c6r

string: mathematics
output: m9s
"""

String_1 = "computer"
a =(String_1[0])
b =(String_1[-1])
print (a + str(len(String_1[1:-1])) + b)

String_2 =  "mathematics"
c = (String_2[0])
d = (String_2[-1])

print(c + str(len(String_2[1:-1]))+ d)


###############################

#Task7

#Say hello world with python

my_var = "Hello World"
print(my_var)


# Task8

#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2  

str_1 = "Www.HackerRank.com"
print(str_1.swapcase())
str_2 = "Pythonist 2"
print(str_2.swapcase())

# Task 9
# what;s your name

first_name = " Kamal"
last_name = "Kannan"
print("Hello" + (first_name + last_name) + "! you just deleved into python")

# Task 10
#Mutation
#Method1:

str_1 = "abracadabra"
list_1 = list((str_1))
print(list_1)
list_1 [5] = "K"
str_1 = "".join(list_1)
print(str_1)

#Method2

str_1 = str_1[:5]+"K"+str_1[6:]
print(str_1)

