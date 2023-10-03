#SOURCE CODE
import os 
import platform
import mysql.connector
import datetime
global z
mydb=mysql.connector.connect(user='root',password='dps',host='localhost',database='air')
mycursor=mydb.cursor()

def registercust():
    L=[]
    name=input("Enter name:")
    L.append(name)
    addr=input("enter address:")
    L.append(addr)
    jr_date=input("enter date of journey:")
    L.append(jr_date)
    source=input("enter source:")
    L.append(source)
    destination=input("enter destination:")
    L.append(destination)
    cust=(L)
    sql="insert into pdata(custname,addr,jrdate,source,destination)"         
    values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()
def classtypeview():
    print("Do you want to see class type available: Enter 1 for yes:")
    ch=int(input("enter your choice:"))
    if ch==1:
       sql="select*from classtype"
       mycursor.execute(sql)
       rows=mycursor.fetchall()
       for x in rows:
           print(x)
def ticketprice():
    print("We have the following rooms for you:-")
    print("1. type First class------->rs6000PN\-")
    print("1. type Business class------->rs4000PN\-")
    print("1. type economy class------->rs2000PN\-")
    x=int(input("Enter your choice Please-."))
    n=int(input("No of passengers:"))
    if(x==1):
        print("You have opted first class")
        s=6000*n
    elif(x==2):
        print("You have opted business class")
        s=4000*n
    elif(x==3):
        print("You have opted economy class")
        s=2000*n
    else:
        print("Please choose a class type")
    print("Your rent is=",s,"\n")
def menuview():
    print("Do you want to see menu available: Enter 1 for yes:")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select*from food"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)

def orderitem():
    global s
    print("Do you want to see menu available: Enter 1 for yes:")
    ch=int(input("Enter your choice:"))
    if(d==1):
         print("you have ordered tea")
         a=int(input("enter quantity"))
         s=10*a
         print("your amount for tea is:",s,"\n")
    elif(d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for coffee is:",s,"\n")
    elif (d==3):
        print("you have ordered colddrink")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for colddrink is:",s,"\n")
    elif(d==4):
        print("you have ordered samosa")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for samosa is:",s,"\n")
    elif(d==5):
         print("you have ordered sandwich")
         a=int(input("enter quantity"))
         s=50*a
         print("your amount for sandwich is:",s,"\n")
    elif(d==6):
         print("you have ordered dhokla")
         a=int(input("enter quantity"))
         s=30*a
         print("your amount for dhokla is:",s,"\n")
    elif(d=7):
         print("you have ordered kachori")
         a=int(input("enter quantity"))
         s=10*a
         print("your amount for kachori is:",s,"\n")
    elif(d==8):
         print("you have ordered milk")
         a=int(input("enter quantity"))
         s=20*a
         print("your amount for milk is:",s,"\n")
    elif(d==9):
         print("you have ordered noodles")
         a=int(input("enter quantity"))
         s=50*a
         print("your amount for noodles is:",s,"\n")
    elif(d==10):
         print("you have ordered pasta")
         a=int(input("enter quantity"))
         s=50*a
         print("your amount for pasta is:",s,"\n")
    else:
        print("please enter your choice from the menu")
def luggagebill():
    global z
    print("Do you want to see rate for luggage: Enter 1 for yes:")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select*from luggage"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("enter your weight of extra luggage->"))
    z=y*1000
    print("You bill:",z,"\n")
    return z
def lb():
    print(z)
def res():
    print(s)
def ticketamount():
    a=input("Enter customer name:")
    print("customer name:",a,"\n")
    print("luggage bill:")
    print(lb)
    print("food bill:")
    print(res)

def Menuset():
    print("enter 1:to enter customer data")
    print("enter 2 : to view class")
    print("enter 3: for ticketamount")
    print("enter 4: for viewing food menu")
    print("enter 5: for food bill")
    print("enter 6: for luggage bill")
    print("enter 7: for complete amount")
    print("enter 8: for exit")

    userinput=int(input("enter your choice"))
    if(userinput==1):
        registercust()
    elif(userinput==2):
        classtypeiew()
    elif(userinput==3):
        ticketprice()
    elif(userinput==4):
        menuview()
    elif(userinput==5):
        orderitem()
    elif(userinput==6):
        luggagebill()
    elif(userinput==7):
        ticketmaount()
    elif(userinput==8):
        quit()
    else:
        print("enter correct choice")
def runagain():
    runagn=input("\n want to run again y/n:")
    while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input("\n want to run again y/n:")

menuset()
runagain()
    
