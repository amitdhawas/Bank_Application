import cx_Oracle
con=cx_Oracle.connect("system/amit@127.0.0.1/orcl")
cur=con.cursor()

def enquiry():
        ACCOUNT_NO=int(input("Enter Your Account Number:"))
        cur.execute("select * from bank_demo")
        recs=cur.fetchall()
        print("="*40)
        for rec in recs:
            for val in rec:
                if(ACCOUNT_NO ==rec [0]):
                    print(val,end=" ")
        print()
        print("="*40)