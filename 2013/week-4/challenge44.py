import csv
import sys

class Student:
	def __init__(self, properties):
		self.name = properties["name"]
		self.score = float(properties["score"])
		self.current_preference = 0
		self.preferences = []
		
		for i in properties["preferences"].split(";"):
			i = i.split("+")
			i[0] = int(i[0])
			try:
				i[1] = float(i[1])
			except:
				pass
			self.preferences.append(i)

	def __str__(self):
		return self.name + str(self.score)

	def __eq__(self,other):
		if (other != None):
			return self.__dict__ == other.__dict__

	def get_score(self, code):
		try:
			for preference in self.preferences:
				if (code == preference[0]):
					if (self.score + preference[1] < 99.95):
						return self.score + preference[1]
					else:
						return 99.95
		except IndexError:
			pass
		return self.score

	def get_name(self):
		return self.name

	def check_degree(self, degree):
		if (self.preferences[self.current_preference][0] == degree.get_code()):
			return True
		return False

	def increase_preference(self):
		if (self.current_preference < len(self.preferences)-1):
			self.current_preference += 1
		else:
			return -1

class Degree:
	def __init__(self, properties):
		self.code = int(properties["code"])
		self.places = int(properties["places"])
		self.name = properties["name"]
		self.institution = properties["institution"]
		self.students = []

	def add_student(self, student1):
		#print("Student " + student.name)
		#print("Degree " + self.name)
		#print("Places " + str(self.places))
		#print(self.students)
		if (self.places > 0):
			self.places -= 1
			self.students.append(student1)
			#print("Made it by places")
			return None		
		else:
			for student2 in self.students:
				#if (student1.get_score(self.code) == 99.95):
				#	student_lowest = self.get_lowest_student()
				#	self.students[self.students.index(student_lowest)] = student1
				#	return student_lowest
				if (student1.get_score(self.code) > student2.get_score(self.code)):
					#print("Made by score")
					self.students[self.students.index(student2)] = student1
					return student2
				elif (student1.get_score(self.code) == student2.get_score(self.code)):
					#print("Made by name")
					if (sorted([student2.get_name(), student1.get_name()])[0] == student1.get_name()):
						self.students[self.students.index(student2)] = student1
						return student2
			return student1
	
	def get_code(self):
		return self.code
	
	def get_lowest_score(self):
		scores = []
		for student in self.students:
			scores.append(student.get_score(self.code))
		if (scores):
			return min(scores)
		return 0

	def get_lowest_student(self):
		if (self.students):
			return min(self.students, key=lambda x:x.get_score(self.code))
		
		
students = []
degrees = []
nope = []

student_properties = []
degree_properties = []

def removew(d):
    return   {k.strip():removew(v)
             if isinstance(v, dict)
             else v.strip()
             for k, v in d.items()}

for line in csv.DictReader(open("students.csv"), lineterminator="\n"):
	#line = removew(line)
	student_properties.append(line)
for line in csv.DictReader(open("degrees.csv"), lineterminator="\n"):
	#line = removew(line)
	degree_properties.append(line)

for properties in degree_properties:
	degrees.append(Degree(properties))

for properties in student_properties:
	students.append(Student(properties))

append_array = []
remove_array = []

while (students):
	for student in students:
		for degree in degrees:
			if (student.check_degree(degree)):
				student_didnt_make_it = degree.add_student(student)
				if (student_didnt_make_it == student):
					if (student.increase_preference() == -1):
						remove_array.append(student)
						nope.append(student)
				elif (student_didnt_make_it == None):
					remove_array.append(student)
					break
				else:
					append_array.append(student_didnt_make_it)
					remove_array.append(student)
					break

		for i in remove_array:
			students.remove(i)

		for i in append_array:
			students.append(i)

		append_array = []
		remove_array = []


print("code,name,institution,cutoff,vacancies")
for degree in sorted(degrees, key=lambda x:x.code):
	print(",".join([str(degree.code),degree.name,degree.institution,
		"-" if len(degree.students) < 1 else "%0.2f" % degree.get_lowest_score(),
		"Y" if degree.places > 0 else "N"]))

print("\nname,score,offer")
output = []
for degree in degrees:
	for student in degree.students:
		output.append([student,degree]) 

for student in nope:
	output.append([student,None])

for i in sorted(output,key=lambda x:(-float(x[0].score),x[0].name)):
	#for i in sorted(output,key=lambda x:-float(x[0].score)):
	if (i[1] != None):
		print(",".join([i[0].name, "%0.2f" % i[0].score, str(i[1].code)]))
	else:
		print(",".join([i[0].name, "%0.2f" % i[0].score, "-"]))
