# A=int(input("Enter Your percentage"))
# B=input("Enter in which you want to go? Aga khan or bahria ?")
# if(B=="bahria" and A>=80):
#     print("You are eligable to go in bahria")
# else:
#     print("You are not eligable to go in bahria")



B=input("Enter in which you want to go? medical or engineering ?")
A=int(input("Enter Your percentage :"))
if(B=="medical" and A>=80):
    print("You are eligable to go in medical")
if(B=="medical" and A<=80):
    print("You can take admission in private")
if(B=="engineering" and A>=50):
    print("You are eligabl to go in engineering")
if(B=="engineering" and A<=50):
    print("You can take admission in private")