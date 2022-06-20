from random import random

x=[]

def getMin(x):
    min=x[0]
    for y in x:
        if min>y:
            min=y
    print("Minimum Value :",min)


def getMax(x):
    max=x[0]
    for y in x:
        if max<y:
            max=y
    print("Maximum Value :",max)

def getAvg(x):
    avg=0
    sum=0
    for y in x:
        sum+=y

    print("Average :",(sum/len(x)))

def getSum(x):
    sum=0
    for y in x:
        sum+=y

    return sum

def find_indexby_val(x):
    val = input("Enter value for get index: ")
    
    index=0
    for y in x:
        # print("#index : ",type(val))
        if float(val) == y:
            print("index : ",index)
            break
        # else:
            # print("Not found")
        index=index+1

def replace_values(x):
    old_val = input("Enter old value : ")
    new_val = input("Enter new value : ")
    index=0

    for y in x:
        # print("#index : ",type(val))
        if float(old_val) == y:
            print("index : ",index)
            n=float(new_val)
            x[index]=n
        # else:
            # print("Not found")
        index=index+1
    print(x)


def get_new_array(x): 
    x2=[]
    print("ar",x)
    for y in x:
       
       if y>4 and y<6:
           x2.append(y)
    print("Array 2 :",x2)

def set_data():
    y=0
    while(y<=5):
        r=round((random()*1000),1)
        x.append(r)
        print(r)
        y+=1
    print(x)
    
    getMin(x)
    getMax(x)
    getAvg(x)
    getSum(x)
    find_indexby_val(x)
    replace_values(x)
    get_new_array(x)



set_data()

