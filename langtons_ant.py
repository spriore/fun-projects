import tkinter as tk
from random import randint
from time import sleep

class App:
	def __init__(self):
		self.root = tk.Tk()
		self.root.attributes("-fullscreen", True) 
		
		screen_width 	= self.root.winfo_screenwidth() - 20
		screen_height 	= self.root.winfo_screenheight() - 20
		self.box 		= 10 # self.box size in px
		self.xscale		= int(screen_width / self.box )
		self.yscale 	= int(screen_height / self.box )
		
		self.c = tk.Canvas(self.root, height= screen_height, width= screen_width)
		self.c.pack()
		
		self.setup()
		
		self.root.bind('<space>', lambda e: self.reset())

		self.root.after(500, self.update)
		self.root.mainloop()
		
	def setup(self):
		self.grid = [[0 for y in range(self.yscale)] for x in range(self.xscale)]
		
		for x in range(self.xscale):
			for y in range(self.yscale):
				self.grid[x][y] = self.c.create_rectangle(
					x*self.box+10, 
					y*self.box+10, 
					(x+1)*self.box+10, 
					(y+1)*self.box+10, 
					fill='#ffffff')
		
		self.ant_coord 	= [round(self.xscale/2),round(self.yscale/2)]
		self.ant_dir	= [1,0]
		self.ant 		= self.c.create_rectangle( 
			self.ant_coord[0] * self.box + 10, 
			self.ant_coord[1] * self.box + 10,
			(self.ant_coord[0] + 1) * self.box + 10, 
			(self.ant_coord[1] + 1) * self.box + 10,
			fill = '#871719')
		
	def update(self):
		self.run = True
		while self.run == True:
			pos		= self.grid[self.ant_coord[0]][self.ant_coord[1]]
			state 	= self.c.itemcget(pos, 'fill')

			if state == '#ffffff':
				self.c.itemconfig(pos, fill='#0f52ba')
				self.ant_dir = [-self.ant_dir[1], self.ant_dir[0]]
			elif state == '#000000':
				self.c.itemconfig(pos, fill='#ffffff')
				self.ant_dir = [self.ant_dir[1], -self.ant_dir[0]]
			else:
				self.c.itemconfig(pos, fill='#000000')
				
			self.ant_coord = [x + y for x, y in zip(self.ant_coord, self.ant_dir)]
			
			if self.ant_coord[0] < 0:
				self.ant_coord[0] = self.xscale-1
			elif self.ant_coord[0] >= self.xscale:
				self.ant_coord[0] = 0
			
			if self.ant_coord[1] < 0:
				self.ant_coord[1] = self.yscale-1
			elif self.ant_coord[1] >= self.yscale:
				self.ant_coord[1] = 0
			
			self.c.coords(self.ant,
				self.ant_coord[0] * self.box + 10, 
				self.ant_coord[1] * self.box + 10,
				(self.ant_coord[0] + 1) * self.box + 10, 
				(self.ant_coord[1] + 1) * self.box + 10)
			
			self.c.update()
			# sleep(.005)
		
	def reset(self):
		self.root.attributes("-fullscreen", False)
		self.run = False
		
if __name__ == '__main__':
	app = App()
