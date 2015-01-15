#!/usr/bin/python3
class Ball:
	x,y = 0,0
	def __init__(self, x,y):
		self.x = float(x)
		self.y = float(y)

class Line:
	label = ""
	x1,y1,x2,y2 = 0,0,0,0
	gradient,intercept = 0,0
	def __init__(self,label,x1,y1,x2,y2):
		self.label = label
		if x1 < x2:
			self.x1 = float(x1)
			self.y1 = float(y1)
			self.x2 = float(x2)
			self.y2 = float(y2)
		else:
			self.x1 = float(x2)
			self.y1 = float(y2)
			self.x2 = float(x1)
			self.y2 = float(y1)
		self.gradient = (self.y2 - self.y1) / (self.x2 - self.x1)
		self.intercept = self.gradient * -self.x1 + self.y1
	
	def disp(self):
		print(self.x1,self.y1,self.x2,self.y2,self.gradient,self.intercept)

	def calc_y(self, x):
		return self.gradient * x + self.intercept

marble_file = open("marble-run.txt").readlines()
ball = Ball(marble_file[0].split()[0],marble_file[0].split()[1])
lines = []
for line in marble_file[1:]:
	line = line.split()
	lines.append(Line(line[0],line[1],line[2],line[3],line[4]))

while ball.y > 0:
	max_line = Line("asdfghjkllllop",0,0,1,0)
	for line in lines:
		if ball.x >= line.x1 and ball.x <= line.x2 and ball.y > line.calc_y(ball.x):
			max_line = line if line.calc_y(ball.x) > max_line.calc_y(ball.x) else max_line
	if max_line.gradient > 0:
		ball.x = max_line.x1
		ball.y = max_line.y1
	else:
		ball.x = max_line.x2
		ball.y = max_line.y2
	if max_line.label != "asdfghjkllllop":
		print(max_line.label,end=" ")
print("GROUND")
