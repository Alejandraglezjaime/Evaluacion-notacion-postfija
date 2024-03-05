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


# ************** GENERACION DE CODIGO INTERMEDIO *******************

def evalua_postfija(posfija):
    pila=[]
    
    cod_int = []
    cont = 1
    
    for e in posfija:
        if es_operador(e):
            op2 = pila.pop()
            op1 = pila.pop()
            if e=='+':
                #resultado = float(op1)+float(op2)
                resultado='t'+str(cont)+"="+op1+'+'+op2+';'
                #cod_int.append(resultado)
            elif e=='-':
                #resultado = float(op1)-float(op2)
                resultado='t'+str(cont)+"="+op1+'-'+op2+';'
            elif e=='/':
                #resultado = float(op1)/float(op2)
                resultado='t'+str(cont)+"="+op1+'/'+op2+';'
            elif e=='*':
                #resultado = float(op1)*float(op2)
                resultado='t'+str(cont)+"="+op1+'*'+op2+';'
            cod_int.append(resultado)
            pila.append('t'+str(cont))
            
            cont = cont+1
        else:
            pila.append(e)
    return cod_int
            
    
print(evalua_postfija(b))

    
    
    