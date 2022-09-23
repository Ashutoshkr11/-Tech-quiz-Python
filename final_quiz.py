import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#dv
def menu():
    ans=True
    while ans:
        print("""
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Tech Competition ANALYSIS SYSTEM
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
1- Data Visualisation
2- Exit
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")
        inp=int(input("Enter your choice: "))
        if inp==1:
            datavisual()
        elif inp==2:
            ex=input("Are you sure you want to exit?(y/n)")
            if ex=='y' or ex=='Y':
                print(" Exiting now............Done! \nHave A Nice Day!!")
        else:
            print("\nInvalid Input Try again")
#DATAVISUAL

def datavisual():
    ans=True
    while ans:
        print('''
====================================
DATA VISUALISATION OF 10 COUNTRIES in I.T sector
====================================
1- Line Chart~> COUNTRIES VS TOTAL MEDALS
2- Bar Chart ~> COUNTRIES VS TOTAL NO. OF GOLD MEDALS
3- scatter Chart ~> DISTRIBUTION OF GOLD, SILVER & BRONZE MEDALS
4- Exit to Main Menu
====================================
===================================''')
        ans=input("Please enter your choice:")
        if ans=='1':
            line_chart1()
        elif ans=='2':
            bar_chart1()
        elif ans=='3':
            scatter_plot()            
        elif ans=='4':
            menu()
        else:
            print("\nInvalid choice.Try again")
            continue
#LINECHART
def line_chart1():
    df=pd.read_csv('tech_data.csv')
    df.sort_values(by='TotalMedal', ascending=False, inplace=True)
    df=df.loc[:,['Country','TotalMedal']]
    df1=df.head(10)
    Countries=df1['Country']
    Totalmedals=df1['TotalMedal']
    plt.plot(Countries,Totalmedals,linestyle=':',color='green',marker='.')
    plt.xticks(Countries,rotation=30)
    plt.xlabel('Country~ ~ ~~~ >',fontsize=12,color='r')
    plt.ylabel('Total Medals~~~~>',fontsize=12,color='r')
    plt.title('TOTAL MEDALS WON BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
    plt.show()
    
#BARCHART
def bar_chart1():
    df=pd.read_csv('tech_data.csv')
    df=df.sort_values('Tgoldmedal',ascending=False)
    Countries=df['Country']
    totalgold=df['Tgoldmedal']
    plt.bar(Countries,totalgold,width=.6, label='Total No. of Gold Medals by Top 10 Countries',color='gold')
    plt.xticks(Countries,rotation=30)
    plt.title('Olympics Gold Medal Analysis of Top 10 Countries',color='blue',fontsize= 16)
    plt.xlabel('Countries~~~~~>',fontsize=12,color='red')
    plt.ylabel('No. of Gold Medals~~~~~>',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()

#SCATTERCHART
def scatter_plot():
    df=pd.read_csv('tech_data.csv')
    clm=df['Tbronzemedal']
    clm1=df['Tsilvermedal']
    clm2=df['Tgoldmedal']
    plt.title("Medals Distribution",color='navy')
    plt.scatter(clm,clm1,clm2)
    plt.show()
#quiz_ -------------------------
def quiz():
    score=0
    q1=input('how many computer languages are in use?: \na)2000 \nb)5000 \nc)50 \nd)20 \nanswer:')
    if q1=='a':
        score+=1
        print('correct,there are about 2000 compter languages in active use,whereas there were on;y 15 in use in 1970.')
    else:
        print('incorrect')
    q2=input('which of these is not an early computer?: \na)ENIAC \nb)UNIVAC \nc)NASA \nd)SAGE \nanswer:')
    if q2=='c':
        score+=1
        print('correct')
    else:
        print('incorrect')
    q3=input('which of these is not a peripheral in computer terms?: \na)keyboard \nb)monitor \nc)mouse \nd)motherboard \nanswer:')
    if q3=='d':
        score+=1
        print('correct')
    else:
        print('incorrect')
    q4=input('a network designed to allow communication within an organicatio  is called?: \na)worldwideweb \nb)yahoo \nc)intranet \nd)internet \nanswer:')
    if q4=='c':
        score+=1
        print('correct')
    else:
        print('incorrect')
    q5=input('who founded apple computer?: \na)stephen fry \nb)bill gates \nc)steve jobs \nd)stephan hawking \nanswer:')
    if q5=='c':
        score+=1
        print('correct')
    else:
        print('incorrect')
    print('your final score:',score,'out of 5')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    
#question portal
import csv

def Question():
    ch='Y'
    while ch=='Y' or ch=='y':
        print("Welcome to Question Portal")
        print("***********************")
        q=input("Enter the question :")
        op1=input("Enter the option 1 :")
        op2=input("Enter the option 2 :")
        op3=input("Enter the option 3 :")
        op4=input("Enter the option 4 :")
        ans=0
        while ans==0:
            op=int(input("Which option is correct answer (1,2,3,4) :"))
            if op==1:
                ans=op1
            elif op==2:
                    ans=op2
            elif op==3:
                        ans=op3
            elif op==4:
                            ans=op4
            else:
                print("Please choose the correct option as answer")
        A.append([q,op1,op2,op3,op4])
        ch=input("Question added successfully.. Do you want to add more (Y/N)")

#attributes
import random
print("-------------------------------------------------------------------------------")
print('|!!!!!!!*******$$$$$$$ WELCOME TO Tech Quiz $$$$$$$*******!!!!!!!                   |')
print("-------------------------------------------------------------------------------")
print("|######!!!!!{{{{ THIS GAME IS DEVELOPED BY ASHUTOSH  }}}}!!!!!######          |")
print("-------------------------------------------------------------------------------")
print('|RULES of game are very simple:                                               |')
print('|1.FIVE questions will be displayed on your screen .')
print('|2.You will get 1 points for each correct answer.                            |')
print("-------------------------------------------------------------------------------")
print(" SO LETS BEGIN..........!")
#methods
while True:
    print("")
    """MAIN MENU
                      FOR YOUR CHOICE"""
    print("\t\t 1.REGISTER YOURSELF")
    print("\t\t 2.ADMIN-LOGIN")
    print("\t\t 4.Exit")
    ch=int(input("ENTER YOUR CHOICE :"))
    

#PROCEDURE FOR SIGN UP
    if(ch==1):
        print("\t\t\t ALL information prompted are mandatory to be filled"),
        username= input("Create username:")
        password=int(input("PASSWORD (IN NUMERIC):"))
        password1=int(input("RE-ENTER PASSWORD :"))
        db=open('database.txt','r')
        d=[]
        for i in db:
            a,b=i.split(',')
            b=b.strip()
            c=a,b
            d.append(a)
        else:
            db = open("database.txt", "a")
            db.write(username+", "+str(password1)+"\n")
            print("User created successfully!")
            print("Please login to proceed:")
    if(ch==2):
        print("\t\t\t Admin-LOGIN")
        pname=input("NAME:")
        PASS=int(input("PASSWORD"))

    f=1
    while f!=3:
        print("Welcome to Quiz")
        print("********************")
        print("1. Enter Questions")
        print("2. Take Quiz")
        print('3. Database visualistion')
        print("4. Exit")
        f=int(input("Enter your choice: "))
        if f==1:
            Question()
        elif f==2:
            quiz()
        elif f==3:
            menu()
        else:
            exit()
            
