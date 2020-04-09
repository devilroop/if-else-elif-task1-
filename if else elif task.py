#task1
a="malayalam"
if a==a[::-1]:
    print(a,"palindrome")

else:
    print("not",a)
#task2
a=int(input("student marks:"))
if a==100:
    print("A grade")
elif a>=90 and a<=99:
    print("B grade")
elif a>=80 and a<=89:
    print("C grade")
elif a>=70 and a<=79:
    print("C grade")
elif a>=50 and a<=69:
    print("E grade")
elif a>=0 and a<=49:
    print("fail")
else:
    print("invalid")
#task3
a=str(input("first number:"))
b=input("second number:")
if a[0]+a[1]<=b:
    print("True")
else:
    print("Flase")
#task4
#python
a=input("word1:")
count=0
list1=['a','e','i','o','u']
for chr in a:
    if chr in list1:
        count+=1
print(count)
#frt   
b=input("word2:")
count=0
list1=['a','e','i','o','u']
for chr in b:
    if chr in list1:
        count+=1
print(count)
#benguluru
c=input("word3:")
count=0
list1=['a','e','i','o','u']
for chr in c:
    if chr in list1:
        count+=1
print(count)
#task5
a="avvacca"
print(int(len(a)/2))
if a[0]==a[3]==a[-1]:
    print("True")
else:
    ("Flase")
b="hello"
print(int(len(a)/2))
if a[0]==a[2]==a[-1]:
    print("True")
else:
    print("Flase")




