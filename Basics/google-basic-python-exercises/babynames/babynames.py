#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  result=[]
  f=open(filename,'r')
  content=f.read()
  year=re.search(r'Popularity\sin\s(\d{4})',content)

  yearmatch=year.group(1)

  result.append(yearmatch)

  tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>',content)
  
  namerank={}
  for t in tuples:
    (rank,boy,girl)=t
    if boy  not in namerank:
      namerank[boy]=rank
    if girl not in namerank:
      namerank[girl]=rank

  sortname=sorted(namerank.keys())
  for name in sortname:
    result.append(name+ ' '+ namerank[name])

  return result

