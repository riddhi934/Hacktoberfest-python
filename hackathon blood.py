import os
def donate(name,hospital,bloodgrp,status,data):
    name.append(input("enter your name please :"))
    hospital.append(input("Enter your name of hospital :"))
    bloodgrp.append(input("Enter your blood group :"))
    data.write("\n ---------------- \n "+"name of patient :"+str(name[len(name)-1])+"\n Hospital Name :"+str(hospital[len(name)-1])+"\n Blood group :"+str(bloodgrp[len(name)-1])+"Status : Blood Donated")
    status.append(0)
def request(name,hospital,bloodgrp,status,data):
    name.append(input("enter your name please :"))
    hospital.append(input("Enter your name of hospital :"))
    bloodgrp.append(input("Enter your blood group you want :"))
    data.write("\n ---------------- \n "+"name of patient :"+"\n Hospital Name :"+str(hospital[len(name)-1])+"\n Blood group :"+str(bloodgrp[len(name)-1])+"Status : Blood requested")
    status.append(1)
def bloodinfo(name,hospital,bloodgrp,status):
    for i in range(len(name)):
        print("\n ---------------- \n "+"name of patient :"+str(name[i])+"\n Hospital Name :"+str(hospital[i])+"\n Blood group :"+str(bloodgrp[i]))
        if(status[i]==0):
            print("Status : Blood Donated")
        else:
            print("Status : Blood requested")
# main program
print("welcome to blood bank")
os.chdir("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python")
data=open("BloodData.txt",'a+')
name=[]
hospital=[]
bloodgrp=[]
status=[]#In 0 is for donated and 1 is requested blood 
print("1) for donatating blood to blood bank ,\n 2) for requesting blood from blood bank,\n 3) for all the data of blood Bankenteries \n 4) enteries of rare blood grp \n 5)Entries of in a perticular hospital \n 6)retiving a perticular data by name of patient \n 7) Exit")
while(1):
    n=int(input())
    if(n==1):
        donate(name,hospital,bloodgrp,status,data)
    elif(n==2):
        request(name,hospital,bloodgrp,status,data)
    elif(n==3):
        bloodinfo(name,hospital,bloodgrp,status)
    elif(n==4):
        for i in range(len(name)):
            if(bloodgrp[i]=="O-"):
                print("\n ---------------- \n "+"name of patient :"+str(name[i])+"\n Hospital Name :"+str(hospital[i])+"\n Blood group :"+str(bloodgrp[i]))
                if(status[i]==0):
                    print("Status : Blood Donated")
                else:
                    print("Status : Blood requested")
    elif(n==5):
        h=input("Enter the name of Hospital")
        for i in range(len(name)):
            if(hospital[i]==h):
                print("\n ---------------- \n "+"name of patient :"+str(name[i])+"\n Hospital Name :"+str(hospital[i])+"\n Blood group :"+str(bloodgrp[i]))
                if(status[i]==0):
                    print("Status : Blood Donated")
                else:
                    print("Status : Blood requested")
    elif(n==6):
        p=input("Enter the name of patient")
        for i in range(len(name)):
            if(name[i]==h):
                print("name of patient :"+str(name[i])+"\n Hospital Name :"+str(hospital[i])+"\n Blood group :"+str(bloodgrp[i]))
                if(status[i]==0):
                    print("Status : Blood Donated")
                else:
                    print("Status : Blood requested")
    else:
        break
