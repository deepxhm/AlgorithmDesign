import re
import sys

stra = input()
lista = re.findall("\d+", stra)
maxlen=0
maxitem = ""

if (len(lista) ==0):
    print("")
    sys.exit(1)
else:
    lista.reverse()
    for item in lista:
        if len(list(item)) > maxlen:
            maxlen=len(list(item))
            maxitem=item

print(maxitem)
print(maxlen)
