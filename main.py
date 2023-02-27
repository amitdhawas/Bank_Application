import cx_Oracle,sys
from new_account import new_account
from credit import credit
from debit import debit
from transfer import transfer
from enquiry import enquiry
try:
    while(True):
        print("This is the Bank Demo")
        print("\t 1. Create  New Account")
        print("\t 2. Credit Funds")
        print("\t 3. Debit Funds")
        print("\t 4. Transfer Funds")
        print("\t 5. Enquiry")
        print("\t 6. Exit")
        n=int(input("Enter a number that you want to Do the operation:"))
        if(n==1):
            new_account()
        elif(n==2):
            credit()
        elif(n==3):
            debit()
        elif(n==4):
            transfer()
        elif(n==5):
            enquiry()
        elif(n==6):
            print("Thank you for visit our bank")
            sys.exit()
        else:
            print("Plese Enter valid operation:")
        a=input("Do you want to make another operation(yes/no):")
        if(a=='no'):
            print("Thank You for visiting our branch")
            sys.exit()
except cx_Oracle.DatabaseError as db:
    print("problem in:",db)