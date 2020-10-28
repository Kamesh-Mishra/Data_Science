



"""
Code Challenge
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]

Solution:
'''Running avarage'''

list1 = [7, 13, 17, 231, 12, 8, 3]

def run_avg(list1):
    new_list = []
    for i in list1:
        new_list.append(i)       
        yield (round(float(sum(new_list))/float(len(new_list)),2))
        
        
        
char = run_avg(list1)

next(char)




"""



a = [7,13,17,231,12,8,3]
k = []

def ravg(a):
    aj = iter(a)
    
    while aj:
        try:
            c = next(aj)
            k.append(c)
            print("List : ",k)
            print("Average of list : ", end =" ")
            yield sum(k)/len(k)
        except StopIteration:
            yield("List exhausted")
            
cc = ravg(a)

print(next(cc))

