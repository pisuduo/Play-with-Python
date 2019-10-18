d={'abc':1,
"bcd":2,
"sfh":3}

l=['abc',2,'dfb',4,'sf',5]
l2=[4,2,5,6,3]
l3=['o','one','on','onne']
string='fooocuos'
s={'one','two','three'}
s2={'one','four','five'}

##---------------- Dictionary operations-----------
d.keys()
d.values()
d.items()
for key, value in d.items():
    print(f'{key},{value:d}')
    print('{},{}'.format(key,value))

d['eee']=100
d.pop('eee') #return the value with key 'eee' and delete that from dictionary

d.popitem()  ## similar with list with pop()
del d['abc'] ## delete item with given key
d.get('bcd') ## get value with given key

##-------------- list operations-------------------
l[-1]
l[::-1]
l[-2:] ## last two items


## change the original list:
l2.sort() 
l.pop()
l
l.extend(l2) ## add l2 at end
l2+l3        ## same
l.append('a')
l.insert(1,'one') ## insert at position 1
l.remove('one')  ## remove the first occurance of value
l.reverse() ## reverse the list

## do not change the original list:
sorted(l2)
sorted(l3,key=len,reverse=True) 
reversed(l) ## not change original list, return an iterator 
for x in reversed(l):
    print(x)
l
len(l)
' '.join(map(str,l))

##--------------------SET operations----------------------
s|s2  ## union
s&s2  ## intersection
s-s2  ## diff
s<s2  ## < > <= >= inclusion relations

s.update(s2)  ## update a set with a union of s2 and itself
s.add('six')
s.remove('six') ## remove, if not exist, keyerror
s.discard('three')  ## remove, if not exist, do nothing
s.pop()
len(s)

##------------------String operations----------------------
string.startswith('f')
string.endswith('d')
string.count('o') 
len(string)
string.index('cu')

## doesn't change original string
string.upper() 
string.strip('s')
string.strip('f')
string.split('ooo',maxsplit=2)
string.zfill(12) # parameter is the total length after filled
string.join(['a','b'])
string.swapcase() ## swap lower and upper case
string.capitalize()

