def adding(a,b):
    print(f"Adding two numbers{a}and {b}")
    return a+b

def substract(a,b):
    print(f"Substract two numbers{a} and {b}")
    return a-b

def multiply(a,b):
    print(f"Multiply two numbers {a} and {b}")
    return a*b
def divide(a,b):
    print(f"Divide two numbers {a} and {b}")
    return a/b

age=adding(20,21)     
height=substract(18,20)
weight=multiply(10,2)
iq=divide(20,2)
print("age:{age},height:{height},weight:{weight},iq:{iq}")
print("Here is the puzzle")
what = adding(age, substract(height, multiply(weight, divide(iq,))))   
print("That becomes: ", what, "Can you do it by hand?")