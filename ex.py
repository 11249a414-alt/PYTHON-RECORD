try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b
    print("division",c)
except ZeroDivisionError:
    print("zero cannot be there in denominator")
finally:
    print("division succesful")