import cx_Oracle
con=cx_Oracle.connect("system/amit@127.0.0.1/orcl")
cur=con.cursor()

def new_account():
        ACCOUNT_NO=int(input("Enter New account Number:"))
        NAME=input("Enter Your Name:")
        AMMOUNT=int(input("Enter Amount you want to credit:"))
        iq="insert into bank_demo values(%d,'%s',%d)"
        cur.execute(iq%(ACCOUNT_NO,NAME,AMMOUNT))
        print("Rs.{} Credited to your Ac XXXX{}".format(AMMOUNT,ACCOUNT_NO))
        con.commit()