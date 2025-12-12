# working on creating functions

def temp(celsius):
    fahrenheit  = (celsius * 9/5) + 32
    return fahrenheit

result = temp(29)
print(result)

def temp(fahrenheit):
    return (fahrenheit - 32) * 5/9
 
result = temp(84.2)
print(result)