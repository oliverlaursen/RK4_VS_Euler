import tkinter as tk

class RK4Euler_Window:
	def __init__(self,width,height):
		self.root=tk.Tk()
		self.root.geometry(f'{width}x{height}')
		self.root.title('RK4 og Euler')

		top=tk.Frame(self.root).pack()
		lefttop=tk.Frame(top,).pack(side=tk.LEFT)
		righttop=tk.Frame(top).pack(side=tk.RIGHT)

		tk.Label(self.root,text='RK4 og Euler i Python').pack()

		tk.Label(lefttop,text='Differentialligning:').pack()
		tk.Label(lefttop,text='Gentagelser (n):').pack()

		self.root.mainloop()




if __name__ == '__main__':
	win=RK4Euler_Window(500,200)