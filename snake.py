import tkinter as tk
from random import randrange
from numpy import linspace as linear

class Application:
	def __init__( self ):
		self.self.scale 		= 13 # No of columns and rows in the grid
		self.b_dim 		= 40 # Size of each square
		self.c_dim 		= self.self.scale * self.b_dim
		self.bound 		= self.c_dim - self.b_dim
		self.center 	= int( self.self.scale / 2 ) * self.b_dim
		self.win_con	= self.self.scale**2 - 1
		self.run 		= False
		
		self.root 	= tk.Tk()
		self.l 		= tk.Label(self.root, anchor = 'n', fg = '#000000', text = 'Press spacebar to start.')	
		self.c 		= tk.Canvas(self.root, bg = '#444444', width = self.c_dim, height = self.c_dim)
		self.l.pack()
		self.c.pack()
			
		
		self.root.bind('<space>', 	lambda e: self.start_game())
		self.root.bind('<Left>', 	lambda e: self.new_dir([-1,0]))
		self.root.bind('<Right>', 	lambda e: self.new_dir([1,0]))
		self.root.bind('<Up>', 		lambda e: self.new_dir([0,-1]))
		self.root.bind('<Down>', 	lambda e: self.new_dir([0,1]))
		
		self.root.mainloop()
		
	def start_game( self ):
		if self.run == False:
			self.run 	= True
			self.count 	= 0
			self.speed 	= linear(100, 50, -(50 / self.win_con))
			
			self.l['text'] = 'Score: 0/' + str(self.win_con)
			
			self.snake_init()
			self.food_init()
			self.update()
		
	def snake_init( self ):
		self.head 		= [self.center,self.center]
		self.body 		= [self.self.scale_init( self.head )]
		self.body_pos	= [self.head]
		self.dir 		= [0,1]
	
	def update( self ):
		self.head = [x + (y * self.b_dim) for x, y in zip( self.head, self.dir )]
		
		if not ( 0 <= self.head[0] <= self.bound ) or not ( 0 <= self.head[1] <= self.bound ) or self.head in self.body_pos:
			
			self.reset( 'lose' )
		
		else:
			self.body.insert( 0, self.self.scale_init( self.head ) )
			self.body_pos.insert( 0, self.head )
			
			if self.head == self.f_pos:
				self.c.delete( self.food )
				self.count += 1
				self.l['text'] = 'Score: ' + str(self.count) + '/' + str(self.win_con)
				
				if self.count != self.win_con:
					self.food_init()
				else:
					self.reset( 'win' )
			else:
				self.c.delete( self.body.pop() )
				self.body_pos.pop()

			if self.run == True:
				self.c.after( int(self.speed[self.count]), self.update )
			
	def new_dir( self, vector ):
		if self.dir != [ -x for x in vector ]:
			self.dir = vector

	def scale_init( self, pos ):	
		self.scale = self.c.create_rectangle( 
			pos[0], 
			pos[1], 
			pos[0] + self.b_dim, 
			pos[1] + self.b_dim, 
			fill = '#ffffff')
		return self.scale
			
	def food_init( self ):
		while True:
			loc = [randrange(0, self.bound, self.b_dim), randrange(0, self.bound, self.b_dim)]
			if not loc in self.body_pos:
				self.f_pos 	= loc
				self.food 	= self.c.create_rectangle(
					self.f_pos[0], 
					self.f_pos[1], 
					self.f_pos[0] + self.b_dim, 
					self.f_pos[1] + self.b_dim, 
					fill = '#871719')
				break
				
	def clear( self ):
		self.c.delete( self.food )
		while len( self.body ) > 0:
			self.c.delete( self.body.pop() )
	
	def reset( self, condition ):
		self.run = False
		self.clear()
		if condition == 'win':
			self.l['text'] = 'You Win! Press spacebar to play again.' 
		else:
			self.l['text'] = 'Score: ' + str( self.count ) + ' Press spacebar to play again.' 
		
if __name__ == "__main__":
	app = Application()
