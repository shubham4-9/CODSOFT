from tkinter import *
Questions =["What is the capital of France?","Who is the CEO of Tesla?",
            "The iphone was created by which company?","How many Harry Potter books are there?"]
Options=[["New York","London","Paris","Dublin"],["Jeff Bezos","Elon Musk","Bill Gates","Tony Stark"],["Apple","Intel","Amazon","Microsoft"],["1","4","6","7"]]
Answers=[3,2,1,4]
Score=0
Number_of_Questions=4
Question_No=1
def next():
    global Score,Question_No
    if val1.get()==1:
        selected_option=1
    elif val2.get()==1:
        selected_option=2
    elif val3.get()==1:
        selected_option=3
    elif val4.get()==1:
        selected_option=4
    else:
        selected_option= -1
    if Answers[Question_No-1]==selected_option:
        Score+=1
    Question_No +=1
    if Question_No > Number_of_Questions:
        root.pack_forget()
        score.place(relx=.40,rely=.40)
        score.config(text="Score:"+str(Score),font=("Arial",15))
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        val4.set(0)
        question.config(text = Questions[Question_No-1])
        option1.config(text=Options[Question_No-1][0])
        option2.config(text=Options[Question_No-1][1])
        option3.config(text=Options[Question_No-1][2])
        option4.config(text=Options[Question_No-1][3])
def check(option):
    if(option==1):
        val2.set(0)
        val3.set(0)
        val4.set(0)
    elif(option==2):
        val1.set(0)
        val3.set(0)
        val4.set(0)
    elif(option==3):
        val1.set(0)
        val2.set(0)
        val4.set(0)
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
win=Tk()
win.title("Quiz Game")
root= Frame()
root.pack()
question= Label(root,width=60, font=("Arial",15),text=Questions[0])
question.pack()
val1= IntVar()
val2=IntVar()
val3=IntVar()
val4=IntVar()
option1= Checkbutton(root, variable=val1, text=Options[0][0],command=lambda:check(1))
option1.pack()
option2= Checkbutton(root,variable=val2, text=Options[0][1],command=lambda:check(2))
option2.pack()
option3= Checkbutton(root, variable=val3, text=Options[0][2],command=lambda:check(3))
option3.pack()
option4= Checkbutton(root, variable=val4, text=Options[0][3],command=lambda:check(4))
option4.pack()
next_b= Button(root,text="next",command=next)
next_b.pack()
score= Label(win)
score.place_forget()
win.mainloop()
