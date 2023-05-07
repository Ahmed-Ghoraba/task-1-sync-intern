from tkinter import *
import datetime
import time
import winsound
#Libraries Imported
actual_time = datetime.datetime.now()
cur_time = actual_time.strftime("%H:%M:%S")
#ALARM FUNCTION
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            break
#GET ALARM TIME 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
 
window = Tk()
window.title("Alarm Clock")
window.geometry("540x600")
window.config(bg="#FFFFFF")
window.resizable(width=False,height=False)
 
time_format=Label(window, text= "Please enter your desired time in 24hour format", fg="blue",bg="#DDDDDD",font=("Arial",15)).place(x=40,y=220)
addTime = Label(window,text = "Hour         Min          Sec",font=60,fg="white",bg="black").place(x = 320)
setYourAlarm = Label(window,text = "SCHEDULE AN ALARM",fg="white",bg="blue",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=40)


hour = StringVar()
min = StringVar()
sec = StringVar()

 
hourTime = Entry(window,textvariable = hour,bg = "#DDDDDD",width = 4,font=(20)).place(x=320,y=40)
minTime = Entry(window,textvariable = min,bg = "#DDDDDD",width = 4,font=(20)).place(x=380,y=40)
secTime = Entry(window,textvariable = sec,bg = "#DDDDDD",width = 4,font=(20)).place(x=440,y=40)
submit = Button(window,text = "Set",fg="Black",bg="#DDDDDD",width = 15,command = get_alarm_time,font=(20)).place(x =150,y=80)
 
window.mainloop()

