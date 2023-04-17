import random

def eliminate_illegal_string(string):
    """{structure multispan + cover glass} are infeasible designs
       eliminate illegal design strings 1={A,B,C}, 2=C & 1={D,E,F}, 2={A,B}"""
    if string[1] == 'C' and string[0] in ['A','B','C']:  # infeasible multi-tunnel X glass
        bit = random.choice([0,1]) 
        options = {0: ['D', 'E', 'F'], 1:['A', 'B']}
        replace = random.choice(options[bit])
        new_string = string[:bit] + replace + string[bit+1:]
        return new_string

    if string[1] in ['A','B'] and string[0] in ['D','E','F']: # not consider Venlo X foil
        bit = random.choice([0,1]) 
        options = {0: ['A', 'B', 'C'], 1:['C']}
        replace = random.choice(options[bit])
        new_string = string[:bit] + replace + string[bit+1:]
        return new_string

    else:
        return string