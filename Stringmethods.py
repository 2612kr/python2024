#1 #capitalize #Upper case the first letter in this sentence


"""
name = "kamalakkannan"
x = name.capitalize()
print(name.capitalize())

header = "i am kamalakkannan and i am living in chennai"
print(header.capitalize())
h= header.capitalize()
print(h)


#2 casefold() #Make the string lower case



class1 = " This Method is Simiar to the lower() string method but casefold method is stronger"
print(class1.casefold()) # this method is simiar to the lower() string method but casefold method is stronger


#3 # Center ()


text = " banana"
print(text.center(30)) #            banana



text = " kamal is an Engineer"
print(text.center (40)) #           kamal is an Engineer


#4 # endswith() # Check if the string end with punctuation sign(.)

mind = " Is phython is simple? no, its not."

print(mind.endswith(".")) # true

val = " No Python is simple and easy to learn"
print(val.endswith(".")) # false

text = " Kamal,"
print(text.endswith(",")) #true

text = " Kamal,Kannan"
print(text.endswith(",kannan")) # because of lowercase # False


#5 expandtabs() #The expandtabs() method sets the tab size to the specified number of whitespaces


txt = " K\ta\tm\ta\tl"
print(txt.expandtabs()) # default tabsize is 8.
print(txt.expandtabs(1))
print(txt.expandtabs(2))
print(txt.expandtabs(3))
print(txt.expandtabs(4))
print(txt.expandtabs(5))
print(txt.expandtabs(8))



# 6 find() 
#The find() method finds the first occurrence of the specified value.
#The find() method returns -1 if the value is not found.


txt = " hello, Welcome to Python world"
print(txt.find("world")) # 26 # find the first char index slicing
print(txt.find("Python")) # 19 # "P" indexing value is 19
print(txt.find("python")) # -1 # becaus of lower case

txt1 = " I am kamal and i am live in chennai"
print(txt1.find("a",5,10)) # 7 , while we giving int value 5,10 it will search the "a" in index 5 to 10 and found a in 7 position



#7 Format()

txt ="I am {}, and my age is {}"
txt1 = " I want {}, what is the price"

print(txt.format("Kamal",30))
print(txt1.format("Banana"))

txt2 = " for only {price: .2f} dollars!"
print(txt2.format(price = 49))


# 8 Index()

# Index() and find both are almost same, whent he value not found index throw and exception error but find() print "-1" value

val1 = " I am kamal"
print(val1.index("kamal"))

# 9 isalnum(), 
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
#Example of characters that are not alphanumeric: (space)!#%&? etc.

txt = "Kamal2612"
print(txt.isalnum()) # true

txt1 = "Kamal@2612"
print(txt1.isalnum()) # false, because of spl character

# 10 isalpha()

var = "Kamal"
print(var.isalpha()) # true, All the char are Alphabatic
Var1 = "Kamal26"
Var2 = "26"
print(Var1.isalpha()) # false, Kamal26 has int in it
print(Var2.isalpha()) # false, 26 is a int



#11 isdecimal(), all the characters in a string are decimals (0-9) print "True"

val = "1234"
val2 = "Kamal26"
val3 = "Kamal"
print(val.isdecimal(),val2.isdecimal(),val3.isdecimal()) 


#12 isdigit()

date = "12.26.92"
time = "1155"
print(date.isdigit()) # false
print(time.isdigit()) # true


# 13 isidentifier()

txt = "Kamal"
txt1 = "Kamal26"
txt2 = "$!@#$"
txt3 = "1kamal"
txt4 = "_Kamal"
txt5 = "Kamal Lamak"
print(txt.isidentifier()) # True, (a-z is a identifier)
print(txt1.isidentifier()) # True, ( a-z, 0-9 is a identifier)
print(txt2.isidentifier()) # False, spl char id not the identifier
print(txt3.isidentifier()) # False, Identifier will not start with number
print(txt4.isidentifier()) # True, Identifier will start with (_)
print(txt5.isidentifier()) # False, between space is not the identifier



#14 islower() , if all the texts are lower print true

a = " hello kamal 123"
b = "Hello Kamal 123"
c = "hello kamal123 ! "
d = "HELLO KAMAL 123"
e = "12k34"
f = "1234"

print(a.islower()) # True all the text are lower case
print(b.islower()) # False first char is upper case
print(c.islower()) # True text are lowercase
print(d.islower()) # False not all the chat lowercase
print(e.islower()) # True , k is a lower case
print(f.islower()) # False, no char in the text


#15 isnumeric()

a = "1234"
b = "kamal 123"
c = " Kamal"
d = "-1"
print(a.isnumeric()) # True, All the text are numberic
print(b.isnumeric()) # False
print(c.isnumeric()) # False
print(d.isnumeric()) # False


# 16 join

a = {"name":"Kamal","Country":"India"}
x = "#".join(a)
print(x)
b = {"Kamal", "Jagan", "Sakthi", "jai"}
y = "test"
print(y.join(b))

#17 lower()

a = " HEllo My Friends"
print(a.lower())


# 18 Partition()
#The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
a = " I Love Python and it easy to learn"
b = " I am in India "
print(a.partition("Python"))
print(b.partition("in"))



# 19 replace()

a = " I love America"
print(a.replace("America","India"))

# 20 rfind()
#The rfind() method finds the last occurrence of the specified value.
#The rfind() method returns -1 if the value is not found.
#The rfind() method is almost the same as the rindex() method. 

a = " I love India and India my Country"
print(a.rfind("India"))
print(a.find("India"))

"""

#21 rspilt

a = " Apple, Banana, Organe"
print(a.rsplit(","))
print(a.split(","))


