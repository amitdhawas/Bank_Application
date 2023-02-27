import cx_Oracle
con=cx_Oracle.connect("system/amit@127.0.0.1/orcl")
cur=con.cursor()
def debit():
        ACCOUNT_NO=int(input("Enter your Account Number:"))
        AM=int(input("Enter Ammount you want to debit:"))
        cur.execute("update bank_demo set AMMOUNT=AMMOUNT-%d where ACCOUNT_NO=%d" %(AM,ACCOUNT_NO))
        con.commit()
        print("Rs.{} Debited from your Ac XXXX{}".format(AM,ACCOUNT_NO))