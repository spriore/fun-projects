import tkinter as tk
from math import pi, sin, cos, radians
import random, time

class App:
	def __init__(self):
		self.root 	= tk.Tk()
		
		self.l = tk.Frame(self.root)
		self.g = tk.Scale(self.l, label='Gravity', from_ = 1, to = 9.8, resolution = .1, orient=tk.HORIZONTAL)
		self.l1 = tk.Scale(self.l, label='L1', from_ = 1, to = 100, resolution  = 1, orient=tk.HORIZONTAL)
		self.l2 = tk.Scale(self.l, label='L2', from_ = 1, to = 100, resolution  = 1, orient=tk.HORIZONTAL)
		self.m1 = tk.Scale(self.l, label='M1', from_ = 1, to = 100, resolution  = 1, orient=tk.HORIZONTAL)
		self.m2 = tk.Scale(self.l, label='M2', from_ = 1, to = 100, resolution  = 1, orient=tk.HORIZONTAL)
		
		self.c = tk.Canvas(self.root, bg='#ffffff', height = 500, width = 500)
		
		self.l.pack(side=tk.LEFT)
		self.g.pack()
		self.l1.pack()
		self.l2.pack()
		self.m1.pack()
		self.m2.pack()
		self.c.pack(side=tk.RIGHT)
		
		self.setup()
		self.root.after(500, self.update)
		self.root.mainloop()
		
	def setup(self):
		self.o = [250,250]
		self.obj1	= {'l': self.l1.get(), 't': pi/2, 'v': 0.0, 'm': self.m1.get()}
		self.obj2 	= {'l': self.l2.get(), 't': pi, 'v': 0.0, 'm': self.m2.get()}
		
		self.origin = self.c.create_rectangle(
			self.o[0] - 2,
			self.o[1] - 2,
			self.o[0] + 2,
			self.o[1] + 2,
			fill = '#ffffff')
			
		self.line1 = self.c.create_line(
			self.o[0],
			self.o[1],
			self.o[0] + self.obj1['l'] * sin(self.obj1['t']),
			self.o[1] + self.obj1['l'] * cos(self.obj1['t']),
			width = 5)
			
		self.line2 = self.c.create_line(
			self.c.coords(self.line1)[2],
			self.c.coords(self.line1)[3],
			self.c.coords(self.line1)[2] + self.obj2['l'] * sin(self.obj2['t']),
			self.c.coords(self.line1)[3] + self.obj2['l'] * cos(self.obj2['t']),
			width = 5)
			
		self.root.bind('<space>', lambda e: self.update())
	
	def update(self):
		self.run = True
		self.root.bind('<space>', lambda e: self.reset())
		while self.run == True:
			pcoords = self.c.coords(self.line2)
			
			g = self.g.get()
			
			l1 = self.l1.get()
			l2 = self.l2.get()
			
			m1 = self.m1.get()
			m2 = self.m2.get()
			
			t1 = self.obj1['t']
			t2 = self.obj2['t']
			
			t1_v = self.obj1['v']
			t2_v = self.obj2['v']
			
			den 	= 2 * m1 + m2 - m2 * cos(2 * t1 - 2 * t2)
			t1_a 	= (-g * (2 * m1 + m2) * sin(t1) - m2 * g * sin(t1 - 2 * t2)  - 2 * sin(t1 - t2) * m2 * (t2_v * t2_v * l2 + t1_v * t1_v * l1 * cos(t1 - t2))) / (l1 * den)
			t2_a	= (2 * sin(t1 - t2) * ((t1_v * t1_v * l1 * (m1 + m2)) + (g * (m1 + m2) * cos(t1)) + t2_v * t2_v * l2 * m2 * cos(t1 - t2))) / (l2 * den)
			
			self.obj1['v'] = round(self.obj1['v'] + t1_a, 4)
			self.obj2['v'] = round(self.obj2['v'] + t2_a, 4)
			
			self.obj1['t'] = round((self.obj1['t'] + self.obj1['v']) % (2 * pi), 4)
			self.obj2['t'] = round((self.obj2['t'] + self.obj2['v']) % (2 * pi), 4)
			
			self.c.coords(self.line1,
				self.o[0],
				self.o[1],
				self.o[0] + l1 * sin(self.obj1['t']),
				self.o[1] + l1 * cos(self.obj1['t']))
				
			self.c.coords(self.line2,
				self.c.coords(self.line1)[2],
				self.c.coords(self.line1)[3],
				self.c.coords(self.line1)[2] + l2 * sin(self.obj2['t']),
				self.c.coords(self.line1)[3] + l2 * cos(self.obj2['t']))
			
			self.c.create_line(
				pcoords[2],
				pcoords[3],
				self.c.coords(self.line2)[2],
				self.c.coords(self.line2)[3])
						
			self.c.update()
			time.sleep(.050)

	def reset(self):
		self.run = False
		self.c.delete('all')
		self.setup()
	
if __name__ == '__main__':
	app = App()
