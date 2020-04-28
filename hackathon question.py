import random
import xlrd
import os
def storingdata(a,k,d):
    book = xlrd.open_workbook("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python\\task.xlsx")
    Q_paper =book.sheet_by_index(0)
    ans.write(str(k)+":"+str(Q_paper.cell_value(a,1))+"\n")
    Question.write(str(k)+": What is the symbol of "+str(Q_paper.cell_value(a,0)))
    Question.write("Options: \n a:"+str(d[0])+"  b:"+str(d[1])+"  c:"+str(d[2])+"\n")
def QuestionPaper(n):
    book = xlrd.open_workbook("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python\\task.xlsx")
    k=1
    l=list(range(1,n+1))
    random.shuffle(l)
    for i in l:
        s=list(range(1,n+1))
        s.remove(i)
        random.shuffle(s)
        Q_paper =book.sheet_by_index(0)
        d=[str(Q_paper.cell_value(s[0],1)),str(Q_paper.cell_value(s[1],1))]
        print(k,": What is the symbol of "+str(Q_paper.cell_value(i,0)))
        d.append(str(Q_paper.cell_value(i,1)))
        random.shuffle(d)
        print("Options: \n","a:",d[0],"  b:",d[1],"  c:",d[2])
        storingdata(i,k,d)
        k=k+1
try:
    a=int(input("Enter the no of Question paper \n"))
    os.chdir("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python")
    b=int(input("Enter the no of Questions \n"))
    for i in range(a):
        print("Questionpaper ",i+1)
        ans=open("Answerkey"+str(i+1)+".txt",'w')
        Question=open("Questionpapers"+str(i+1)+".txt",'w')
        ans.write("Answerkey"+str(i+1)+"\n")
        Question.write("Question Paper"+str(i+1)+"\n")
        QuestionPaper(b)
        ans.close()
        Question.close()
        print("For Answer Key Enter 1:\n")
    c=int(input())
    for i in range(a):
        if(c==1):
            ans=open("Answerkey"+str(i+1)+".txt",'r')
            for x in ans:
                print(x)
            ans.close()
except:
    print("----INPUT IS INVALID----")
