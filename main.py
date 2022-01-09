from tkinter import *
import  math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
#25
SHORT_BREAK_MIN = 5
#5
LONG_BREAK_MIN = 20
#20
i=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt,text="00:00")
    label.config(text="Timer",fg=GREEN)
    check_lb.config(text=" ")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global i
    i+=1
    work_Sec=WORK_MIN*60
    short_break_Sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if i % 2 == 0:
        count_down(short_break_Sec)
        label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_Sec)
        label.config(text="WORK", fg=GREEN)
    if i % 8 == 0:
        count_down(long_break_sec)
        label.config(text="BREAK", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    # if count_sec==0:
    #     count_sec="00"
    if count_sec < 10:
        count_sec=(f"0{count_sec}")
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(i/2)):
            mark+="✔"
            check_lb.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas=Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="tomato.png")

canvas.create_image(100, 111, image=img)
timer_txt=canvas.create_text(100, 129, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1,row=1)

# count_down(5)

label=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

start_bt=Button(text="Start",highlightthickness=0,command=start_timer)
start_bt.grid(column=0,row=2)

reset_bt=Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_bt.grid(column=2,row=2)

check_lb=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,12,"bold"))
check_lb.grid(column=1, row=3)

window.mainloop()
