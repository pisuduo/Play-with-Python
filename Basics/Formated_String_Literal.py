## literally formatting ##
field1='sexiest job'
field2='data is produced daily'
field3='Individuals'
fact1=21
fact2=2500000000000000000
fact3=72.41415415151
fact4=1.09

print(f"Data science is considered {field1!r} in the {fact1:d}st century")  ## !r: allow to contain quotes :d: allow to contain digits

print(f"About {fact2:e} of {field2} in the world")                          ## :e: exponential

print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")  ## :.nf: allow n decimals

#-------------inline operations and functions---------------------#
number1=120
number2=7
string1='httpswww.datacamp.com'
list_links=['www.aaa.com','www.bbb.com','www.ccc.com','www.ddd.com']

# Include both variables and the result of dividing them 
print(f"{number1:d} tweets were downloaded in {number2:d} minutes indicating a speed of {number1/number2:.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")         ##escape sequences are not allowed; different quotes need to be used for the f-string and the strings inside .replace().

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:.2f}% of the posts contain links")   ## f strings allow inline operations and functions

a=f"Only {len(list_links)*100/120:.2f}% of the posts contain links"
print(a)
print(type(a))
#-----------------datetime----------------------------------------#
import datetime
east={'date':datetime.datetime(2007,4,20,0,0),'price':1232443}
west={'date':datetime.datetime(2006,5,26,0,0),'price':1432673}

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")  ##To format the date, use the specifiers %m, %d and %Y.

## use quotes in keys of dictionary!!
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")







