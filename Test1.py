import re

#1.1 Given a number count the total number of digits in a number
def count(l):
    c=0
    while l!=0:
        l=l//10
        c=c+1
    print("Count of total number of digits:",c)
l=int(input("Enter a number:"))
count(l)

#1.2 Reverse the following list using for loop

list1=[]
n = int(input("Enter number of elements for list 1 : "))
for i in range(0, n): 
    l = int(input())
    list1.append(l)

for i in range(len(list1)-1,-1,-1):
    print(list1[i])



#2 Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

s1=input("Enter 1st String:")
s2=input("Enter 2nd String:")
a=int(len(s1)/2)
string=s1[0:a]+s2+s1[a:]
print(string)

#3. Arrange String characters such that lowercase letters should come first

i=input("Enter a String:")
#i='JHkjnhcBJJBNmj'
l=list(i)
low=[]
up=[]
for n in l:
    if n.islower():
        low.append(n)
    else:
        up.append(n)
low=''.join(map(str,low))
up=''.join(map(str,up))
print(low+up)

#4. Given a string, return the sum and average of the digits that appear in the string, ignoring all othercharacters

#inputStr = "English = 78 Science = 83 Math = 68 History = 65"
inputStr=input("enter string with marks:")
l=[]
for marks in re.findall(r'\d\d', inputStr):
	l.append(int(marks))
print(inputStr)
print("sum",sum(l),"Average",sum(l)/len(l))

#5 Given a two list. Create a third list by picking an odd-index element from the first list and even indexelements from second.
listOne=[]
listTwo=[]

n = int(input("Enter number of elements for list 1 : "))
for i in range(0, n): 
    list1 = int(input())
    listOne.append(list1)
m = int(input("Enter number of elements for list 2 : "))
for i in range(0, m): 
    list2 = int(input())
    listTwo.append(list2)
l=listOne[0::2]
m=listTwo[1::2]
print(l+m)












