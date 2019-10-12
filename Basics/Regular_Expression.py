# DATACAMP exercises
# match string with regular expressions
import re
prog=re.compile('\d{3}-\d{3}-\d{4}')
result=prog.match('123-456-7890')
print(bool(result))

result2=prog.match('0123-456-7890')
print(bool(result2))

# Extracting numerical values from strings
