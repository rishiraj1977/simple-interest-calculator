from tkinter import *
window=Tk()

window.title('SIMPLE INTEREST CALCULATOR')
window.geometry("450x400")
window.configure(bg='black')

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "white", bg = "black", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal_text=Label(window, text="principal", fg = "white", bg = "black", font=("Calibri", 12),bd=1)
principal_text.place(x=20, y=90)

principal=Entry(window, text="", bd=2, width=22)
principal.place(x=150, y=92)

interest_text=Label(window, text="Rate of Interest", fg="white", bg="black",font=("Calibri",12),bd=1)
interest_text.place(x=20, y=140)

interest=Entry(window, text="", bd=2, width=22)
interest.place(x=150, y=142)

time_text=Label(window, text="time", fg="white", bg="black",font=("Calibri",12),bd=1)
time_text.place(x=20, y=190)

time=Entry(window, text="", bd=2, width=22)
time.place(x=150, y=192)

def calculate_interest():
    p=float(principal.get())
    r=float(interest.get())
    t=float(time.get())
    i=(p*r*t)/100
    rate = round(i,2)

    show_label.destroy()
    
    output=Label(result_frame, text="interest"+ str(p)+"at rate of interest"+ str(r)+"for"+ str(t)+"year is it"+ str(rate), fg="white", bg="black",font=("Calibri",12),bd=1)    
    output.place(x=20, y=40)
    output.pack()

button=Button(window,text="Calculate", bg = "cyan", fg="white", font=("Calibri", 8),command=calculate_interest)
button.place(x=20, y=220)

result_frame = LabelFrame(window,text="Result", bg = "white", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

show_label=Label(result_frame,text=" ", bg = "white", font=("Calibri", 12), width=33)
show_label.place(x=20,y=20)
show_label.pack()

window.mainloop()