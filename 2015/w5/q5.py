#!/bin/env python3

def application(functor, arg, slash):
    if '/' in arg or '\\' in arg:
        arg = '(' + arg + ')'
    arg = slash + arg
    if functor.endswith(arg):
        res = functor[:-len(arg)]
        if '/' in res or '\\' in res:
            return res[1:-1]
        return res

def fwd_app(left, right):
    return application(left, right, '/')

def bwd_app(left, right):
    return application(right, left, '\\')

categories = input("Enter categories: ")
if categories:
    blocks = []
    for i in categories.split():
        blocks.append([])
        blocks[0].append([i])

    for block in enumerate(blocks[:]):
        previous_block = blocks[block[0]-1]
        for cell in enumerate(previous_block[:-1]):
            block[1].append([])
            for block_below in range(block[0]):
                left = blocks[block_below][cell[0]]
                right = blocks[block[0]-block_below-1][block_below+cell[0]+1]
                for left_element in left:
                    for right_element in right:
                        if left_element == "conj":
                            if "\\" in right_element or "/" in right_element:
                                right_element = "("+right_element+")"
                            string = right_element + "\\" + right_element
                            block[1][-1].append(string)
                        else:
                            result = fwd_app(left_element, right_element) or bwd_app(left_element, right_element)
                            if result:
                                block[1][-1].append(result)

    cell_width = 0
    for block in blocks:
        for cell in block:
            for element in cell:
                cell_width = max(len(element)+2,cell_width)

    final_string = ""
    for block in blocks[::-1]:
        final_string += "+"+(("-"*cell_width)+"+")*len(block)+"\n"
        cell_height = 1
        for cell in block:
            cell_height = max(len(cell),cell_height)
        for line in range(1,cell_height+1):
            final_string += "|"
            for cell in block:
                if len(cell) >= line:
                    final_string += " "*(cell_width-len(cell[line-1])-1)+cell[line-1]+" |"
                else:
                    final_string += " "*(cell_width-1)+" |"
            final_string += "\n"
    final_string += "+"+(("-"*cell_width)+"+")*len(blocks[0])
    print(final_string)

