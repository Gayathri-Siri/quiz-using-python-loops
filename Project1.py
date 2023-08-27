print("-----------WELCOME TO QUIZ GAME----------")
name=(input("Please Enter your name: "))
print("Welcome" ,name)
a=(input("Do you want to play this game? ")).lower()
if(a=="yes"):
    print("------Lets Start------")
    x=(input("Type Yes,if you want to read the instructions :"))
    s=0
    c=0
    if(x=="yes"):
        print("Here are the instructions")
        print("It Consists of two sections")
        print("Section-1 contains 5 questions regarding python programming")
        print("Section-2 contains 5 questions regarding Mathematics")
        print("For each correct answer,you will get +1 marks")
        print("For each incorrect answer,you will get -0.5 marks")
        print()
    print("------Section-1-------")
    one=int(input("1.What will be the value of python expression 4+3%5? "))
    if(one==7):
                  s+=1
                  c+=1
                  print("correct")
    else:
        s=s-0.5
        print("incorrect")
    two=input("2.Is python case sensitive while dealing with identifiers? ").lower()
    if(two=="yes"):
              s+=1
              c+=1
              print("correct")
    else:
        s=s-0.5
        print("incorrect")
    three=input("3.Which keyword is used for function in python language? ").lower()
    if(three=="def"):
        s+=1
        c+=1
        print("correct")
    else:
        s=s-0.5
        print("incorrect")
    four=input("4.Python supports the creation of anonymous functions at runtime,using a construct called_____").lower()
    if(four=="lambda"):
        s+=1
        c+=1
        print("correct")
    else:
        s=s-0.5
        print("incorrect")
    five=input("5.In python,what does pip stands for? ").lower()
    if(five=="preferred installer program"):
        s+=1
        c+=1
        print("correct")
    else:
        s=s-0.5
        print("incorrect")
    print("------Section-2-------")
    six=int(input("6.Whart is the next prime number after 7? "))
    if(six==11):
                  s+=1
                  c+=1
                  print("correct")
    else:
        s=s-0.5
        print("incorrect")
    seven=int(input("7.60 Times of 8 equal to? "))
    if(seven==480):
              s+=1
              c+=1
              print("correct")
    else:
        s=s-0.5
        print("incorrect")
    eight=int(input("8.121 divided by 11 equal to? "))
    if(eight==11):
        s+=1
        c+=1
        print("correct")
    else:
        s=s-0.5
        print("incorrect")
    nine=int(input("9.The product of 133*0*4 is___"))
    if(nine==0):
        s+=1
        c+=1
        print("correct")
    else:
        s=s-0.5
        print("incorrect")
    ten=float(input("10.What is 6%? "))
    if(ten==0.06):
        s+=1
        c+=1
        print("correct")
    else:
        s=s-0.5
        print("incorrect") 
    print("Your score is : " ,s)
    if(s<=5):
        print("Bad performance,keep reading")
    elif(s>=8 and s<=10):
        print("Best performance")
    else:
        print("Average performance")
    print("Thank you,for paricipating")
    
else:
    print("Okay,See you next time")
