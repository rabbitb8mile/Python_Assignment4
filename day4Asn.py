#For with else statement
n=[10,20,30,40,50]
for num in n :
    if num ==70:
        print("70 found ")
        break
else :
    print("70 not found ")




#while with else statement
i=1
while i<=10:
    if i ==5:
        break
    else :
        print(i)
        i+=1
else :
    print("breaked")


#Break statement 
a="parth"
for i in a :
     if i=="h":
         break
     else:
         print(i)
else :  
      print("it has pass")     



#continue 
for num in range(1,15):
    if num == 10:
        continue 
    print(num)


#pass statement 

for num in range(1,15):
    if num == 10:
        pass 
    print(num)

