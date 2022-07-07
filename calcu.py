import logging
logging.basicConfig(filename='calc.log', level=logging.INFO)

i = input("Would you like to multiply (m), divide (d), subtract (s), or add (a) ")

x = input("Type a number ")
y = input("Type one more number ")

x = int(x)
y = int(y)


if i == 'a':
    print(x+y)

elif i == "s":
    print(x-y)

elif i == "d":
    print(x/y)

elif i == "m":
    print(x*y)

logging.info(i)