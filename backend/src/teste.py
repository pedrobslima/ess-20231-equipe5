from typing import Optional

def foo(a: list, b: Optional[str] = None):
    a.append(b)
    if(b != None):
        print(b)
    return a

lista = []

lista = foo(lista)

#print(lista)