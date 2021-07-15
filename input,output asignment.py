# Program to allocate newly admitted students to their classes

admission= int(input("Please enter your admission number"))
if admission>=1 and admission<=25:
    print("You have been admitted to Form 1 Yellow")

elif admission>=26 and admission<50:
    print("You have been admitted to Form 1 Green")

elif admission>=51 and admission<=75:
    print("You have been admitted to Form 1 Red")

elif admission>=76 and admission<=100:
    print("You have been admitted to Form 1 Blue")

else:
    print("No such admission,please countercheck your admission number")                