col=["red","blue","black","purple"]
pos=[1,2,3,4]
print("WELCOME TO MASTERMIND!!!")
a=0
b=0
choice="wrong"
while choice=="wrong":
    for i in range (0,4):
        x=input("enter colour(red,purple,blue,white,orange,black,green):")
        y=int(input("enter position:"))
        if x=="red":
            a=a+1
            if y==1:
                b=b+1
        if x=="blue":
           a=a+1
           if y==2:
               b=b+1        
        if x=="black":
            a=a+1
            if y==3:
                b=b+1       
        if x=="green":
            a=a+1
            if y==4:
                b=b+1
    if a==4 and b==4:
        choice="correct"
        print("all 4 options are correct!")
    else:
        print("you got ",a," colours and ",b," positions correct")
        a=0
        b=0
    print("game complete")
