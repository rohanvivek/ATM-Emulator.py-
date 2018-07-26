print("""
WELCOME TO BANK OF VIVEK
========================

        """)
print("If You are new coustomer please enter your data")
q=input("Are you a new coustomer? yes or no")
if q=='yes':
    import pymysql
    con=pymysql.connect(host='localhost',user='root',password='shaktimaan',db='rohan')
    c= con.cursor()
    def insert(id,name,pin,account,balance):
        query="insert into bank values('%d','%s','%d','%d','%d')"%(id,name,pin,account,balance)
        c.execute(query)
        con.commit()
        print("Data Inserted")
    id=int(input("Enter Your Choice Of Id"))
    name=input("Enter Your Choice of Name")
    pin=int(input("Enter 4 digit Your Choice of pin"))
    account=int(input("Enter Your Choice Of account number"))
    balance=20000
    insert(id,name,pin,account,balance)
elif q=='no':
    print("You have selected not to enter data")
    balance = 20000
    def deposit():
        chances = 3
        while chances >= 0:
            d = int(input("Enter Amount to be Deposited"))
            if d <= 10000 and d % 100 == 0:
                print("Choice is Correct")
                break
            else:
                print("Enter Notes in multiple of 100 and less then 10,000")
        print(""""Transaction Successful
        Money Deposited""")
        print("Your Account Balance is", balance + d)
    def withdrawal():
        chances = 3
        while chances >= 0:
            a = int(input("Enter Amount to be Withdrawn"))
            if a <= 10000 and a % 100 == 0:
                print("Choice is Correct")
                break
            else:
                print("Enter Notes in multiple of 100 and less then 10,000")
        print("select Your choices of notes")
        print("100", "200", "500", "2000")
        s = int(input("Enter your choice"))
        if s == 100:
            d = a / 100
            print("No. of 100 rupees notes will be", d)
        elif s == 200:
            d = a / 200
            print("no. of 200 rupees notes will be", d)
        elif s == 500:
            d = a / 500
            print("no. of 500 rupees notes will be", d)
        elif s == 2000:
            d = a / 2000
            print("no. of 2000 rupees notes will be", d)
    chances = 3
    while chances >= 0:
        pin = (input('Please Enter You 4 Digit Pin: '))
        if pin == ('1997'):
            print('You entered you pin Correctly\n')
            break
    encodestring = pin.encode('utf-32', 'strict')
    print("your pin is ", encodestring)
    chances = chances - 1
    l = ["""1.withdraw
    2.deposit
    3.balance"""""]
    for i in range(len(l)):
        print(l[i])
    c = int(input("Enter Your Choice"))
    if c == 1:
        withdrawal()
    elif c == 2:
        deposit()
    elif c == 3:
        print("Your Balance is", balance)
    else:
        print("Invaid Choice")
