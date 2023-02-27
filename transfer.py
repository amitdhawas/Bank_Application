import cx_Oracle
con=cx_Oracle.connect("system/amit@127.0.0.1/orcl")
cur=con.cursor()
def transfer():
        ACCOUNT_NO=int(input("Enter Your Account Number:"))
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
            AM=int(input("Enter Ammount you want to Transfer:"))
            print("="*40)
            if((AM+500)>sbal):
                print("Insuffiecient funds in your account")
                print("="*40)
            else:
                found=False
                TACC_NO=int(input("Enter Account Number You want to transfer:"))
                for rec in recs:
                    if(TACC_NO ==rec[0]):
                        found=True
                        break
                if(found==False):
                    print("{} is invalid account number".format(TACC_NO))
                else:
                    cur.execute("update bank_demo set AMMOUNT=AMMOUNT-%d where ACCOUNT_NO=%d" %(AM,ACCOUNT_NO))
                    cur.execute("update bank_demo set AMMOUNT=AMMOUNT+%d where ACCOUNT_NO=%d" %(AM,TACC_NO))
                    con.commit()
                    print("="*40)
                    print("Rs.{} Transfer Succesfully from Ac No XXXX{} to Ac No XXXX{}".format(AM,ACCOUNT_NO,TACC_NO))
                    print("="*40)