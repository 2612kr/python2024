tup_1 = (1,4,5,6,7,8) # tuple 1
tup_2 = (5,6,7,8,9)   # tuple 2
#tup = tuple(set(tup_1)&set(tup_2))
#print(tup)
x = set((tup_1))
y = set((tup_2))
com_tup = x.intersection(y)
print(com_tup) # comman element between two tuples
con_tup = ((tup_1)+ (tup_2))
print(con_tup) # concatenate of both tuples
tup = set ((con_tup)) # after convert to set it will remove duplicates
tup = tuple(tup) # revert back to tuple after removing duplicates using set
print(tup)
print(tup.index(9)) # index of 9 
print(tup*3) # multiple * 3




