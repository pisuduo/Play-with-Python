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



