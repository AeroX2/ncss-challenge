#!/bin/env python3

def pprint(arg1):
    return recurse(arg1, "", 0)

def recurse(arg1, string, spacing):
    if isinstance(arg1, list):
        if len(arg1) > 1:
            output = recurse(arg1[0],string,spacing+1)
            string = "["+output+",\n" 
            for i in arg1[1:]:
                output = recurse(i,string,spacing+1)
                string += (spacing+1)*" " + output + ",\n"
            string += spacing*" "+"]"
            return string
        elif len(arg1) == 1:
            return "["+recurse(arg1[0],string,spacing+1)+"]"
        else:
            return repr(arg1)
    else:
        return repr(arg1)

#print(pprint(['one', "two", 3]))
#print(pprint(['one', 'two', [1, 2]])) 
#print(pprint(["one", 'two']))
#print(pprint(['one', 'two', 'three', [1, 2, 3], 'four', [], 'five', [['six']]]))
#print(pprint([[[[], []], [[], []]], [[[], []], [[], []]]]))
#print(pprint([[[['one', 'two']]]]))
#print(pprint([[[[['one', 'two']]]]]))
#print(pprint([1, [[2,[3,4], 5]]]).replace("\n","\\n"))
#print("[[[[],\n   [],\n  ],\n  [[],\n   [],\n  ],\n ],\n [[[],\n   [],\n  ],\n  [[],\n   [],\n  ],\n ],\n]")
