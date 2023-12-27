#import library
import inflect

p = inflect.engine()
name = []
#try
try:
    #loop to take input
    while True:
        n = input("Name: ")
    #put inputs in a list
        name.append(n)

#catch error with except
except EOFError:
    pass

#use join() from inflect
my_list = p.join(name)
print("Adieu, adieu, to",my_list)