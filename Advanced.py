print('Hello, welcome to Advanced Calculator')
number_1 = input('Input your 1st number here ')
number_2 = input('Input your 2nd number here ')
method = input('What type of algorithm would you like to use? +, -, *, or /?')
if method is "+":
    result = float(number_1) + float(number_2)
if method is "-":
    result = float(number_1) - float(number_2)
if method is "/":
    result = float(number_1) / float(number_2)
if method is "*":
    result = float(number_1) * float(number_2)
    print(result)

print('Thanks for using Advanced Calculator!')