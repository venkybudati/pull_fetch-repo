'''sentence=input("Enter any string")
var=len(sentence)
for character in range(var,-1,-1):
    print(character)
'''

'''
#print odd numbers from 10 to 100
for i in range(10,101):
    if i % 2 == 1:
        print(i)

#print even numbers from 10 to 100
for i in range(10,101):
    if i%2 ==0:
        print(i)



#print prime numbers from 10 to 100
count=0
for i in range(10,101):
    if i%1==0 and i%i==0:
        count +=1
    if count==2:
        print(i)
'''

                   
for number in range (10, 101):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
