"""Task7:

Covert below two lists in to a dictionary

[1,2,3,4,5]
["python","cpp","c","java","php"]
"""

a = [1,2,3,4,5]
b = ["python","cpp","c","java","php"]
c_dict = dict(zip(a,b))
print(c_dict) #{1: 'python', 2: 'cpp', 3: 'c', 4: 'java', 5: 'php'}


