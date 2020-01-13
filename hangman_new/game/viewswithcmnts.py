from django.shortcuts import render,redirect
from django.http import HttpResponse
#import time
from django.contrib import messages
#import tkinter.messagebox
import ctypes  # An included library with Python install.   

#Global Variables
ans=''
ques=''
key=''
chances=10
an=0
flag=0

# Create your views here.
def hang(request):
    bye=str(request.POST['playa'])
    if (bye[0]=='Y' or bye[0]=='y'):
        global chances
        chances=10
        return render(request,'question.html')
    else:
        return render(request,'bye.html')

def play(request):
    global ans
    global ques,ques1
    global chances
    ans=request.POST['answer']
    ques=request.POST['question']
    ques=list(ques)
    return render(request,'entry.html',{'ques1':''.join(ques),'chances':chances})


def entry(request):
    global chances
    global ans
    global ques,ques1
    global an,flag

    while(chances>0):
        key=request.POST['entry']
        #ques=str(ques)
        #flag=0
        #ans=str(ans)
        for i in range(len(ans)):
            if key==ans[i] and ques[i]=='_':
                ques[i]=ans[i]
                flag=1 
        print(ques,ans)
        key='\0'
        ques1=''.join(ques) 
        an=0
        print(flag)
        for i in range(len(ques)):
            if ques[i] == '_':
                an=1
                break

        if an==0 :
            ctypes.windll.user32.MessageBoxW(0, f"The answer is {ans}",
                                            "Congratulations,YOU WON!!!!",0)
            return redirect('/')

        if flag==0 :
            chances=chances-1
            return render(request,'entry.html',{'ques1':ques1,'chances':chances})

        elif flag==1:
            flag=0
             
            return render(request,'entry.html',{'ques1':ques1,'chances':chances})
                


        
    if chances==0:
        #msg=messages.info(request,"Better luck next time")
        #tkinter.messagebox.showinfo("title", "Better luck next time")
        ctypes.windll.user32.MessageBoxW(0, "YOU LOST", "Better luck next time",0)
        return redirect('/')


def playagain(request):
    return render(request,'playagain.html')    