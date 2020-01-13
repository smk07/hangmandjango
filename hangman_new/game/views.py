from django.shortcuts import render,redirect
from django.http import HttpResponse
import ctypes

#Global Variables
ans=''
ques=''
key=''
chances=3
an=0
flag=0
ques2=''
# Create your views here.
def hang(request):
    bye=int(request.POST['playa'])
    if bye==0:
        return render(request,'bye.html')

    elif bye==1:
        global chances
        chances=3
        return render(request,'question.html')
    else:
        ctypes.windll.user32.MessageBoxW(0, "Select Atleast One","Error",0)
        return render(request,'playagain.html')    

        

def play(request):
    global ans
    global ques,ques1
    global chances
    ans=request.POST['answer']
    ques=request.POST['question']
    que=ques
    ques=list(ques)

    if len(ans) == len(que) :
        for i in range(len(ans)):
            j=i
            if ans[i]==que[i] or que[i]=='_':
                continue
            else:
                ctypes.windll.user32.MessageBoxW(0, "Enter Same word","Error",0)
                return render(request,'question.html')
        if j==len(ans)-1:
                return render(request,'entry.html',{'ques1':''.join(ques),'chances':chances})    
    else:
        ctypes.windll.user32.MessageBoxW(0, "Enter same word","Error",0)
        return render(request,'question.html')

def entry(request):
    global chances
    global ans
    global ques,ques1
    global an,flag
    global ques2

    while(chances>0):
        ques2=''
        key=request.POST['entry']
        for i in range(len(ans)):
            if key==ans[i] and ques[i]=='_':
                ques[i]=ans[i]
                flag=1
        
        ques1=''.join(ques)
         
        an=0
        for i in range(len(ques)):
            if ques[i] == '_':
                an=1
                break

        if (key in ques):
            flagy1=1
        else:
            flagy1=0

        if (key in ques2):
            flagy=1
        else:
            flagy=0

            ques2=ques2+""+key
        
        key='\0'
        
        if an==0 :
            ctypes.windll.user32.MessageBoxW(0, f"The answer is {ans}",
                                            "Congratulations,YOU WON :) !!!!",0)
            return redirect('/')

        if flag==0:
            if(flagy==0 and flagy1==0):
                chances=chances-1
                if chances>0:
                    return render(request,'entry.html',{'ques1':ques1,'chances':chances})
            else:
                return render(request,'entry.html',{'ques1':ques1,'chances':chances})
                
        elif flag==1:
            flag=0
             
            return render(request,'entry.html',{'ques1':ques1,'chances':chances})
                


        
    if chances==0:
        ctypes.windll.user32.MessageBoxW(0, "Chances=0. YOU LOST :(", "Better luck next time",0)
        return redirect('/')


def playagain(request):
    return render(request,'playagain.html')    