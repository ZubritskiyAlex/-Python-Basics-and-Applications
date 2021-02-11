"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза."""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"cat"
    match_object = re.findall(pattern, line)
    if len(match_object) > 1:
        print(line)


"""Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
"""
import re
import sys
pattern = r'(z.{3}z)'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)
        
        
""" Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿". """


import re
import sys
pattern = r'.*\\.*'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)
        
 

"""Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)."""


import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\b(\w+)\1\b", line) is not None:
        print(line)
        
        
"""Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки."""

import re
import sys
for line in sys.stdin:
    line = line.rstrip()
    template = r'human'
    replTemplate = r'computer'
    subTmp = re.sub(template, replTemplate ,line)
    print(subTmp)
    
    
   
  """ Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh"."""

import sys
import re

for line in sys.stdin:
    line = re.sub(r"\ba+\b", "argh", line.rstrip(), 1, flags=re.IGNORECASE)
    print(line)
    
"""Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w."""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    fixed = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
    print(fixed)



"""Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w."""
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    fixed = re.sub(r"(\w)(\1)+", r"\1", line)
    print(fixed)
    
    
    
    
