def newton_sqrt(num):
    num = float(num)
    output = num / 2
    for i in range(10):
       output = output - ((output**2 - num)/(2*output))
    return output 
