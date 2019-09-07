#### трирешетки подряд означают что данный элемент несовместим с системой вкладок, он должен быть внутри  а не снаружи, как показано в самом начале
from tkinter import *
#lib dropdowninput
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
#перемотка
from tkinter import scrolledtext
from tkinter import messagebox

from tkinter.ttk import Progressbar
from tkinter import ttk

from tkinter import Menu

#Загрузка файла
from os import path
from tkinter import filedialog

#Загрузка информации  пути файла(ов) в переменную, и отображение ее в поле txtscroll
def clickedBtnImport():
    #С указанием типа файла
    #file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    #Узнать имя каталога
    #dir = filedialog.askdirectory()
    #С указанием начального директория
    #file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
    file = filedialog.askopenfilename()
    #мультивыбор
    #files = filedialog.askopenfilenames()
    #Вывод в поле
    txtscroll.delete(1.0, END)
    txtscroll.insert(INSERT, file)

#from input to text
def clickedBtn():
    res = "Привет {}".format(txt.get() + combo.get())
    res2 = selected.get()
    lbl.configure(text=res)
    lbl2.configure(text=res2)

#Очистка поля/переменной txtScroll
def clickedBtnClear():
    txtscroll.delete(1.0, END)

#Всплывающее окно
def clickedBtnInfo():
    messagebox.showinfo('Заголовок', 'Текст Инфо')
    #messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
    #messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке
    ##С выбором диалога
    #res = messagebox.askyesnocancel('Заголовок', 'Текст')
    #res = messagebox.askquestion('Заголовок', 'Текст')
    #res = messagebox.askyesno('Заголовок', 'Текст')
    #res = messagebox.askokcancel('Заголовок', 'Текст')
    #res = messagebox.askretrycancel('Заголовок', 'Текст')

window = Tk()
#Заголовок окна
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x600')
#Вкладки
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
lbl1 = Label(tab1, text='Вкладка 1', padx=5, pady=5)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Вкладка 2', padx=5, pady=5)
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
#Меню
menu = Menu(window)
new_item = Menu(menu) #, tearoff=0
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Открыть', command=clickedBtnImport)
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
#dropdownlistAndInput
combo = Combobox(window, width=10)
combo['values'] = (0,1, 2, 3, 4, 5, "Текст")
combo.current(0)  # установите вариант по умолчанию
#combo.get()
###combo.grid(column=0, row=0)
#button
btn = Button(window, command=clickedBtn, text="Клик", bg="white", fg="black")
###btn.grid(column=1, row=0)
#button2
btnClear = Button(window, command=clickedBtnClear, text="ClearTxtScroll", bg="white", fg="gray")
###btnClear.grid(column=3, row=0)
#btnInfo
btnInfo = Button(window, command=clickedBtnInfo, text="Info", bg="white", fg="gray")
###btnInfo.grid(column=4, row=0)
#btnImport
btnImport = Button(window, command=clickedBtnImport, text="Import", bg="white", fg="gray")
###btnImport.grid(column=4, row=0)
#checkbox
# можно так
##chk_state = IntVar()
##chk_state.set(0) # False
##chk_state.set(1) # True
# а можно так переменная типа tkinter BooleanVar()
chk_state = BooleanVar()
chk_state.set(True)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state)
###chk.grid(column=2, row=0)
#radio
selected = IntVar()
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
###rad1.grid(column=0, row=1)
###rad2.grid(column=1, row=1)
###rad3.grid(column=2, row=1)
#input
txt = Entry(window, width=10) #, state='disabled'
###txt.grid(column=0, row=2)
txt.focus()
#text
lbl = Label(window, text="Привет", font=("Arial Bold", 18))
###lbl.grid(column=0, row=3)
#text2
lbl2 = Label(window, text="Number", font=("Arial Bold", 18))
###lbl2.grid(column=0, row=4)
#scrolled window
txtscroll = scrolledtext.ScrolledText(window, width=10, height=10)
txtscroll.insert(INSERT, 'Текстовое поле')
###txtscroll.grid(column=0, row=5)

#spin поле ввода с возможностью выбора значения из интервала, с стрелочками
var = IntVar()
var.set(50)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
#Выбор из определенных значений
#spin = Spinbox(window, values=(3, 8, 11), width=5)
#Значение по умолчанию
###spin.grid(column=0, row=6)

#Стилизованный прогресс бар
#Настройка стиля
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
#Последним параметром указан стиль
bar = Progressbar(window, length=100, style='black.Horizontal.TProgressbar')
bar['value'] = 70 #в %
###bar.grid(column=0, row=7)

# must be end
window.mainloop()
