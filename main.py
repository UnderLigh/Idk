from tkinter import *


root = Tk()
root.title('For FBR')
root.geometry('500x500')
root.resizable(height=False, width=False)

button_num_7 = Button(root, text='7', bg='grey', fg='white', height=3, width=5)
button_num_7.place(x=125, y=150)

button_num_8 = Button(root, text='8', bg='grey', fg='white', height=3, width=5)
button_num_8.place(x=175, y=150)

button_num_9 = Button(root, text='9', bg='grey', fg='white', height=3, width=5)
button_num_9.place(x=225, y=150)

button_num_6 = Button(root, text='6', bg='grey', fg='white', height=3, width=5)
button_num_6.place(x=225, y=210)

button_num_5 = Button(root, text='5', bg='grey', fg='white', height=3, width=5)
button_num_5.place(x=175, y=210)

button_num_4 = Button(root, text='4', bg='grey', fg='white', height=3, width=5)
button_num_4.place(x=125, y=210)

button_num_3 = Button(root, text='3', bg='grey', fg='white', height=3, width=5)
button_num_3.place(x=225, y=270)

button_num_2 = Button(root, text='2', bg='grey', fg='white', height=3, width=5)
button_num_2.place(x=175, y=270)

button_num_1 = Button(root, text='1', bg='grey', fg='white', height=3, width=5)
button_num_1.place(x=125, y=270)

button_num_0 = Button(root, text='0', bg='grey', fg='white', height=3, width=5)
button_num_0.place(x=175, y=330)

button_delete = Button(root, text='delete', bg='black', fg='red', height=3, width=5)
button_delete.place(x=275, y=30)

button_1 = Button(root, text='+/-', bg='blue', fg='white', height=3, width=5)
button_1.place(x=125, y=330)

button_2 = Button(root, text='x', bg='dark blue', fg='white', height=3, width=5)
button_2.place(x=275, y=150)

button_4 = Button(root, text='-', bg='dark blue', fg='white', height=3, width=5)
button_4.place(x=275, y=210)

button_5 = Button(root, text='+', bg='dark blue', fg='white', height=3, width=5)
button_5.place(x=275, y=270)

button_6 = Button(root, text='=', bg='dark blue', fg='white', height=3, width=5)
button_6.place(x=275, y=330)

button_7 = Button(root, text='/', bg='dark blue', fg='white', height=3, width=5)
button_7.place(x=275, y=90)

button_8 = Button(root, text='C', bg='dark blue', fg='white', height=3, width=5)
button_8.place(x=225, y=30)

button_9 = Button(root, text='CE', bg='dark blue', fg='white', height=3, width=5)
button_9.place(x=175, y=30)

button_10 = Button(root, text='%', bg='dark blue', fg='white', height=3, width=5)
button_10.place(x=125, y=30)

button_11 = Button(root, text='Cf', bg='dark blue', fg='white', height=3, width=5)
button_11.place(x=125, y=90)

button_12 = Button(root, text='x**2', bg='dark blue', fg='white', height=3, width=5)
button_12.place(x=175, y=90)

button_13 = Button(root, text='√', bg='dark blue', fg='white', height=3, width=5)
button_13.place(x=225, y=90)

button_13 = Button(root, text=',', bg='0blue', fg='white', height=3, width=5)
button_13.place(x=225, y=330)
root.mainloop()
