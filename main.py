def salary(name,Basic_salary,sales):
    commission=0
    if sales >= 100000:
        commission =sales*0.02
    salary=Basic_salary + commission
    print(f"{name}'s salary:salary{salary}")
salary("Tony", 100000, 1500000)
salary("Jared",15000000,5000000)
salary("Peter",100000,50000)
#loops
#for loops is used for iterating over a sequence
for letters in "Hellow":
    print (letters)
for i in range(10):
    print(i)
for j in range(0,10,2):#start,end,steps 2
    print(j)
for n in range(100):
    if n%2==0:
        print(n)
    else:
        print("odd number")
for i in range(10):
    for i in range (i+1):
        print("*",end="")
    print()
for n in range(99,0):
    print(n)





