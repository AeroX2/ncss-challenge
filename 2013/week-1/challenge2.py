# Enter your code for "Costly cake!" here.
import math

cake1_side = float(input("Cake 1 side length (cm): "))
cake1_cost = float(input("Cake 1 cost ($): "))
cake2_side = float(input("Cake 2 side length (cm): "))
cake2_cost = float(input("Cake 2 cost ($): "))

cake1_cost_per_side = cake1_cost / cake1_side ** 2
cake2_cost_per_side = cake2_cost / cake2_side ** 2

print("Cake 1 costs ${:.2f} per cm2 for {} cm2".format(cake1_cost_per_side,cake1_side ** 2))
print("Cake 2 costs ${:.2f} per cm2 for {} cm2".format(cake2_cost_per_side,cake2_side ** 2))

if (cake1_cost_per_side == cake2_cost_per_side):
    print("Get either!")
elif (cake1_cost_per_side > cake2_cost_per_side):
    print("Get cake 2!")
else:
    print("Get cake 1!")