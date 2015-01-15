# Enter your code for "Optimus SUBlime" here.
#!/usr/bin/python3

ingredients_file = [line.rstrip() for line in open("preferences.txt").readlines()]
ingredients_score = {}

sandwiches = [line.rstrip() for line in open("sandwiches.txt").readlines()]
sandwiches_scores = {}

for ingredient_score in ingredients_file:
	ingredient = ingredient_score.split(",")[0]
	score = int(ingredient_score.split(",")[1])
	ingredients_score[ingredient] = score

for sandwich in sandwiches:
	temp_score = 0
	for ingredient in sandwich.split(","):
		if (ingredient in ingredients_score):
			temp_score += ingredients_score[ingredient]
	sandwiches_scores[sandwich] = temp_score

if (len(sandwiches) > 0):
  [print(i) for i in (sorted(sorted(sorted(sandwiches_scores), key=lambda x: -len(x.split(","))), key=lambda x: -sandwiches_scores[x]))]
else:
  print("devo :(")
