dict_1 = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

x = dict_1.get(3)
tup = tuple(x)
print(tup)


new_dict= (tup[0])
a = (new_dict[:10:2])
print(a) # bobtn
new_dict1= (tup[2])
b = (new_dict1[-1:-6:-1])
print(b) # arbeg

"""sum = (a + b)
print(sum)
tup1 = tuple(sum)
print(tup1) """

all_key = dict_1.keys()
con = tuple(all_key)
print(con) # out put of all keys


y = dict_1.get(2)
import statistics

avg = statistics.mean(y)
print(avg) # Avg of key 2




