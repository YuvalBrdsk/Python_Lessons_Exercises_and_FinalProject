num=int(input("Enter a number: "))
count=0

while num!=0:
    if num%3==0 or num%7==0:
        count+=1
    num = int(input("Enter a number: "))
print(count)
