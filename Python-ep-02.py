from tkinter import*
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI = Tk() # แสดงหน้าจอ
GUI.title('บันทึกข้อมูลนัดหมายประจำวัน') # ชื่อโปรแกรม
GUI.geometry('500x400') # กำหนดกรอบ

L1 = Label(GUI, text='บันทึกรายสัปดาห์' ,font=('Angsana New' ,15),fg='green')
L1.place(x=30,y=25)
#################
def button2():
    text = ' ประชุมที่บริษัท เวลา 9:00 '
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=95,y=80)
B2 = ttk.Button(FB1,text='นัดหมายวันจันทร์',command=button2)
B2.pack(ipadx=1,ipady=12)
#################
def button3():
    text = ' นัดพบลูกค้าไว้ ตกลงทางการค้า '
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=95,y=150)
B2 = ttk.Button(FB1,text='นัดหมายวันอังคาร',command=button3)
B2.pack(ipadx=12,ipady=12)
#################
def button4():
    text = ' รับประทานอาหาร กับลูกค้าคนสำคัญ '
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=95,y=220)
B2 = ttk.Button(FB1,text='นัดหมายวันพุธ',command=button4)
B2.pack(ipadx=12,ipady=12)
##################
def button5():
    text = ' มีประชุมกับฝ่ายขาย เวลา 13:00 '
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=300,y=80)
B2 = ttk.Button(FB1,text='นัดหมายวันพฤหัสบดี',command=button5)
B2.pack(ipadx=12,ipady=12)
##################
def button6():
    text = ' มีประชุมกับฝ่ายบัญชี เวลา 11:00 '
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=300,y=150)
B2 = ttk.Button(FB1,text='นัดหมายวันศุกร์',command=button6)
B2.pack(ipadx=12,ipady=12)
###################
def button7():
    text = ' กินข้าวกับเพื่อน '
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=300,y=220)
B2 = ttk.Button(FB1,text='นัดหมายวันเสาร์',command=button7)
B2.pack(ipadx=12,ipady=12)
###################
def button8():
    text = ' ไปดูงานงานที่ชลบุรี ช่วงบ่าย'
    messagebox.showinfo('เรามีนัด',text)

FB1 = Frame(GUI)# กระดาน
FB1.place(x=185,y=290)
B2 = ttk.Button(FB1,text='นัดหมายวันอาทิตย์',command=button8)
B2.pack(ipadx=12,ipady=12)
###################
GUI.mainloop()
