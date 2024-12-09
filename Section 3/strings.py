myString = "abecedar"

# Reverse index:

print(myString[-1] == 'r')

print(myString, "The 5th characted in reverse", myString[-5])

mySlicedString = myString[2:6:2]

print(mySlicedString)

print("test endline \ntest")

myOtherString = "abcdeghijklmnopqrstuvwxyz"

print(myOtherString[3:])

print(myOtherString[3:-3:2])

print(myOtherString[:10]) # UP TO 10 BUT NOT INCLUDING IT

print(myOtherString[::2]) # every other

print(myOtherString[::-1]) # reverse

text = "Am completat certificarea in python"
print(text.split())

print("This is a string {0} {0} {0} {1} {0}".format("INDEXED", "ABC"))

result = 100 / 777

print('Result is {r:1.3f}'.format(r=result))

myList = [1, 1, 1, 1, 2, 2, 3]
print(set(myList))

print(set('test'))
