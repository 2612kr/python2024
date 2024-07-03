"""
a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}


#py
#ello
#en
#zoo
#Bot



print(a)

"""
a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}

x = a.get(1)
#print(x)
print(x[3][:2])
y = a.get(2)
#print(y)
y_a = y.get(10)
#print(y_a)
print(y_a[1:])
y_b = y.get(40)
#print(y_b)
print(y_b[3:5])
z = a.get(40)
#print(z)
z_a = z.get(1)
#print(z_a)
print(z_a[:3])
z_b = z.get(2)
#print(z_b)
print(z_b[:3])



