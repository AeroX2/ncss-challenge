#!/usr/bin/python3
from particle import Particle

def load_particles(filename):
	particle_file = open(filename)
	particles = []
	for line in enumerate(particle_file):
		#Check no whitespace
		if len(line[1].strip()) < 1: continue

		#Check length of line
		numbers = line[1].split()
		if len(numbers) > 5:
			raise RuntimeError("Line {} contains too many items".format(line[0]+1))
		elif len(numbers) < 5:
			raise RuntimeError("Line {} contains too few items".format(line[0]+1))

		#Check numbers
		temp_particle = []
		for number in numbers:
			try:
				temp_particle.append(float(number))
			except:
				raise TypeError("Line {} has a non-number".format(line[0]+1))
		if temp_particle[-1] not in [-1,0,1]:
			raise ValueError("Line {} has an invalid charge".format(line[0]+1))

		#Check same position
		for particle in particles:
			if particle[0] == temp_particle[0] and particle[1] == temp_particle[1]:
				raise ValueError("Line {} uses the same position as a previous particle".format(line[0]+1))
		particles.append(temp_particle)
	p = []
	for n in particles:
		p.append(Particle(n[0],n[1],n[2],n[3],n[4]))
	return p

try:
  l = load_particles("particles.txt")
except RuntimeError as e:
  # we check that the following is printed
  # with the correct message for this file
  print("Raised RuntimeError", e)
except TypeError as e:
  # other Exceptions left as an exercise for you!
  print("Raised TypeError", e)
for particle in l:
	particle.disp()
