## positional and formating ##

print('I am {} happy {}'.format('very','now'))  # use placeholders

mystring='{} is {}'
name='Anna'
info='a girl'
mystring.format(name,info)
print(mystring.format(name,info))

## reordering values

print('I am {2} happy {0} lalala {1}'.format('now','haha','very'))

## named placeholders
print('{name} is {info}'.format(name=name,info=info))

data={'name':'Anna','info':'a girl'}  # using dictionaries
print('{data[name]} is {data[info]}'.format(data=data))

##exercises:

# Assign the substrings to the variables
wikipedia_article='In computer science, artificial intelligence (AI), sometimes called machine intelligence,\
     is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.'
my_list=[]
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")


# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))

# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))






