''''
Программа для создание gui-окон. 

Версия программы расчитана на то, что Вы вручную заполните имя, настройки, параметны, а программа создаст окно, с учётом введённых параметров.

Дальше ТОЛЬКО ВЫ будете с ними работать и редактировать!!!
'''
import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_Main()

	def init_Main(self):
		toolbar	= tk.Frame(bg = '', bd = 2)#### bg- цвет bd - размер(в пикселях)
		toolbar.pack(side = tk.TOP, fill =tk.X)

		open_dialog_button = tk.Button(toolbar, text = 'Создать окно', command = self.open_dialog)
		open_dialog_button.pack(side=tk.LEFT)

		open_dialog_optin = tk.Button(toolbar, text = 'Настройки', command= self.in_option)
		open_dialog_optin.place(x=90, y=0)

		self.tree = ttk.Treeview(self, columns=('Настройки'), height=15)
		self.tree.column('Настройки', width=30, anchor=tk.CENTER)

		self.tree.pack()

	def open_dialog(self):
		nw_child()

	def in_option(self):
		optin_body()

class nw_child(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_nw_child(self.name_var.get)

	# def set_name(self):
	# 	messagebox.showinfo()

	def init_nw_child(self):
		self.title('Создать окно')
		self.geometry('200x200')
		self.resizable(False, False)
		####Переменные
		self.name_var = str()
		self.visota_var = str()
		self.shirina_var = str()
		#Имя
		l1 = tk.Label(self, text='Имя')
		l1.place(x=0, y=0)
		self.entry_name = tk.Entry(self, textvariable=self.name_var)
		self.entry_name.place(x=50, y=0)
		#Высота
		l2 = tk.Label(self, text='Высота')
		l2.place(x=0, y=25)
		self.entry_visota = tk.Entry(self, textvariable=self.visota_var)
		self.entry_visota.place(x=50, y=25)
		#Ширина
		l3 = tk.Label(self, text='Ширина')
		l3.place(x=0, y=50)
		self.entry_shirina = tk.Entry(self, textvariable=self.shirina_var)
		self.entry_shirina.place(x=50, y=50)
		#Комбо бокс
		l4 = tk.Label(self, text='Расположение окна')
		l4.place(x=0, y=100)
		self.vibor = ttk.Combobox(self, width = 15,)
		self.vibor['values'] = ('Toolbar', 'Country Window')
		self.vibor.current(0)
		self.vibor.place(x=0, y=125)
		###Кнопки
		btn_cancel = tk.Button(self, text='Отмена', command=self.destroy)
		btn_cancel.place(x=100, y=170)

		btn_add_ok = tk.Button(self, text='Создать', command=self.set_name)
		btn_add_ok.place(x=0, y=170)

		self.grab_set()
		self.focus_set()




class optin_body(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.nw_child_in_option()

	def nw_child_in_option(self):
			self.title('Настройки')
			self.geometry('200x200')
			self.resizable(False, False)

			self.grab_set()
			self.focus_set()

if __name__ == '__main__':
	root = tk.Tk()
	app = Main(root)
	root.title('Создание GUI для HOI4')
	root.geometry ('640x450')
	tk.Button(command=root.quit, text="Quit").place(x=600, y=2.5)
	root.resizable(False, False)
	root.mainloop()


