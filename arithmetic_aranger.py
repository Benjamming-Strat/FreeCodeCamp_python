import re
import numpy as np

def arithmetic_arranger(arr,solve = False):


    first = ""
    second=""
    lines = ""
    sumx = ""
    string=""

    if len(arr) > 5:
        return "Error: Too many problems."


  
    for i in arr:
        #searches for chars that are not in the pattern used
        if (re.search("[^\s0-9.+-]", i)):
            #seearches for division or multiplication sign
            if (re.search("[/]",i) or re.search("[*]",i)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        
        first_number = i.split(" ")[0]
        operator = i.split(" ")[1]
        second_number = i.split(" ")[2]
        length = max(len(first_number),len(second_number)) +2
        
        
        
        if len(first_number)>4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        #calculation 
        if operator=="+":
            sum = int(first_number) + int(second_number)
        elif operator=="-":
            sum = int(first_number) - int(second_number)
        

        #string adjusment
        top = str(first_number).rjust(length)
        bottom = operator + second_number.rjust(length-1)
        res = str(sum).rjust(length)
        
        

        if i != arr[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += "_" * (length) + "    "
            sumx += str(res) + "    "

        else:
            first += top
            second += bottom
            lines += ("_" * length )
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n"  + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string

        
        
        
        

print(arithmetic_arranger(["2 * 3568", "1 + 3", "9999 + 9999"], True))