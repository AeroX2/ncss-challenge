import csv

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
					return self.score + preference[1]
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
		if (self.places > 0):
			self.places -= 1
			self.students.append(student1)
			return None
		else:
			for student2 in self.students:
				if (student1.get_score(self.code) > student2.get_score(self.code)):
					self.students[self.students.index(student2)] = student1
					return student2
				elif (student1.get_score(self.code) == student2.get_score(self.code)):
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
				return "%0.2f" % min(scores)
			return "-"
						
students = []
degrees = []
nope = []

student_properties = []
degree_properties = []

for line in csv.DictReader(open("students.csv"), dialect="unix"):
	student_properties.append(line)
for line in csv.DictReader(open("degrees.csv"), dialect="unix"):
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
for degree in degrees:
	print(",".join([str(degree.code),degree.name,degree.institution,degree.get_lowest_score(),"Y" if degree.places > 0 else "N"]))

print("\nname,score,offer")
output = []
for degree in degrees:
	for student in degree.students:
		output.append([student,degree]) 

for student in nope:
	output.append([student,None])

for i in sorted(output,key=lambda x:-float(x[0].score)):
	if (i[1] != None):
		print(",".join([i[0].name, "%0.2f" % i[0].score, str(i[1].code)]))
	else:
		print(",".join([i[0].name, "%0.2f" % i[0].score, "-"]))
