#!/usr/bin/python3
from particle import Particle

particle_file = open("particles.txt").read().strip().split("\n")
iterations = int(particle_file[0])
particles = []
for particle in particle_file[1:]:
	line = particle.split()
	particles.append([Particle(*map(float, line[:-2])),float(line[-2]),float(line[-1])])
	
#init = True
for iteration in range(iterations):
	temp_string = ""
	for particle_list in particles:
		particle = particle_list[0]

		#same-left,other-left,same-right,other-right
		#same-up,other-up,same-down,other-down
		ax = [0.0,0.0,0.0,0.0]
		ay = [0.0,0.0,0.0,0.0]
		for other_particle_list in particles:
			other_particle = other_particle_list[0]
			if other_particle == particle: continue

			tempx,tempy = -2,-2
			if other_particle.x < particle.x: tempx = 0
			elif other_particle.x > particle.x: tempx = 2
		
			if other_particle.y < particle.y: tempy = 0
			elif other_particle.y > particle.y: tempy = 2

			if other_particle.q != particle.q: 
				tempx += 1
				tempy += 1
			if tempx > -1: ax[tempx] += 1
			if tempy > -1: ay[tempy] += 1

		#Moving
		particle_list[1] = ((ax[0] + ax[3]) - (ax[2] + ax[1])) / 10.0
		particle_list[2] = ((ay[0] + ay[3]) - (ay[2] + ay[1])) / 10.0

	for particle_list in particles:
		particle = particle_list[0]

		#Update
		particle.vx += particle_list[1]
		particle.vy += particle_list[2]
		particle.move()

		#Bounding check
		if particle.x >= 300:
			particle.x = 300
			particle.vx *= -1
		elif particle.x <= -300:
			particle.x = -300
			particle.vx *= -1
		if particle.y >= 200:
			particle.y = 200
			particle.vy *= -1
		elif particle.y <= -200:
			particle.y = -200
			particle.vy *= -1

		temp_string += "%0.1f,%0.1f," % (particle.x,particle.y)
	print(temp_string.strip(","))
