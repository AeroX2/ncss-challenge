#!/usr/bin/python3
import math
class Particle:
	def __init__(self, x,y,vx,vy,q):
		self.x = x;
		self.y = y;
		self.q = q;
		self.vx = vx;
		self.vy = vy;

	def disp(self):
		print("position = (%d, %d)" % (self.x,self.y))
		print("velocity = (%d, %d)" % (self.vx,self.vy))
		print("charge = " + str(self.q))

	def distance(self,ox,oy):
		return math.sqrt((ox - self.x) ** 2 + (oy - self.y) ** 2)
		
	def move(self):
		self.x += self.vx
		self.y += self.vy

p = Particle(5, 4, 1, -2, -1)
print(p)
p.disp()
p.move()
p.disp()
d = p.distance(10, 5)
print(d)

