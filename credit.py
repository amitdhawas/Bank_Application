import cx_Oracle
con=cx_Oracle.connect("system/amit@127.0.0.1/orcl")
cur=con.cursor()
def credit():
        ACCOUNT_NO=int(input("Enter your Account Number:"))
        AM=int(input("Enter Ammount you want to credit:"))
        cur.execute("select * from bank_demo")
        recs=cur.fetchall()
        print("="*40)
        found=False
        for rec in recs:
            if(ACCOUNT_NO == rec[0]):
                found=True
                sbal=rec[2]
                break
        if(found==False):
            print("{} is invalid account number".format(ACCOUNT_NO))
        else:
            validamt=False
            if((AM+500)>sbal):
                print("Insuffiecient funds in your account")
                print("="*40)
            else:
                cur.execute("update bank_demo set AMMOUNT=AMMOUNT-%d where ACCOUNT_NO=%d" %(AM,ACCOUNT_NO))
                con.commit()
                print("Rs.{} Credited from your Ac XXXX{}".format(AM,ACCOUNT_NO))