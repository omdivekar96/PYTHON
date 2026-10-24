print("hello world")
#a=int(input("enter the 1st no:"))
#b=int(input("enter the 2nd no:"))
#add=a+b
#print(add)
string='ANUTOPIAN'
print(string[2:9])

print("escape sequence characters\nin python\ncoding language")

#f STRING.......
#if(marks>75):
#marks=int(input("enter ur marks:"))
#else:
#    print(f"distinction with marks:{marks}")
#    print("no distinction")    

#lists(mutable) and tuples(immutable)
list=['apple',12,'roll-no',80]
print(list[0])
list[0]="mango"
print(list[0])#..........list can be changed/slicing is enable
list.append("banana")
list.pop(0)
list.insert(0,69)#...............inserting 69 at 0th index
print(list)
l1=[12,45,34,22,68,90]
l1.sort()
print(l1)#.......sorting

tup=(True,69,'Baramati',False,100,'Pune')
A=tup.count(69)
print(A)
i=tup.index('Baramati')
print(i)
tup1=(89,90,91)
tup2=('Bar','Car','War')
print(tup1+tup2)#...............concatination

#DICTIONARY......
marks={"om":100,"vedant":90,"shrey":80}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"shree":400,"nihansh":60})
print(marks)
#print(marks.get["suyash"])#....it will return error
print(marks.get("suyash"))#....it will return none
# d={}
# name=input('enter name')
# lang=input('enter language')
# print(d.update({name:lang}))
# print(d)

#SETS.........
a=set()#avoid{}cuz it will create empty dict 
set={1,5,'omi',77,54,54,54}#it doesnt repeat elements
set.add(69)#set.remove
s1={1,56,79,3}
s2={59,90,4,1,34}
print(s1.union(s2))
print(s1.intersection(s2))

#conditional statements with and,in........
marks=100
if(marks>90 and marks<100):
    print('distinction')
elif(marks>70 and marks<90):
    print('first class')
else:
    print('fail')

city=['pune','baramati','bombay','delhi']
# # info=input('enter city:')
# if(info in city):
#     print('verified')
# else:
#     print('sorry')


#loops..............
list=[1,2,'word',90,'low']
i=0
while(i<len(list)):
    print(list[i])
    i+=1
for i in list:#.........simililarly with tuples and strings
    print(i)
#range function and forloop with else......
for j in range(1,5,2):#...step slicing(adding +2 till (n-1=4))
    print(j)
for item in list:
    print(item)
else:#....it will get print when the for loop get fully exhausted
    print('all items are printed')

#break and continue..........
for i in range(10):
    if(i==5):
        break#exit the loop
    print(i)
for i in range(5):
    if(i==3):
        continue#...skips 3
    print(i)  

#functions..............
def fact(n):
    if(n==1 or 0):
        return 1
    else:
        return n*fact(n-1)
n=4
print(fact(n))





    
    


