# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:24:06 2024

@author: gonza
"""

a=[1,2,3,4,5,6]
a.append(9)
print(a)
a.pop()
print(a)

def es_operador(cad):
    return cad in '*+-/<=>=%'

b=["1","2","*","3","4","*","+"]

def evalua_postfija(posfija):
    pila=[]
    
    for e in posfija:
        if es_operador(e):
            op2 = pila.pop()
            op1 = pila.pop()
            if e=='+':
                resultado = float(op1)+float(op2)
            elif e=='-':
                resultado = float(op1)-float(op2)
            elif e=='/':
                resultado = float(op1)/float(op2)
            elif e=='*':
                resultado = float(op1)*float(op2)
            pila.append(resultado)
        else: #no es operador por lo tanto es operando 
            pila.append(e)
    return pila[0]
    
print(evalua_postfija(b))

    
    
    