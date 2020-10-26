

```python
from sympy import init_session
from sympy.parsing.latex import parse_latex
from IPython.display import Markdown as md
from IPython.display import display
import numpy as np

init_session()

a, b, c, d = symbols('a b c d', real = True)
```

    IPython console for SymPy 1.4 (Python 3.6.8-64-bit) (ground types: gmpy)
    
    These commands were executed:
    >>> from __future__ import division
    >>> from sympy import *
    >>> x, y, z, t = symbols('x y z t')
    >>> k, m, n = symbols('k m n', integer=True)
    >>> f, g, h = symbols('f g h', cls=Function)
    >>> init_printing()
    
    Documentation can be found at https://docs.sympy.org/1.4/
    



```python
def mostrar_ejercicio(ejercicio,solucion,tipo=0) :
    #tipo=0 se pasa el ejercicio y la solucion en formato latex
    if tipo == 0 :
        display(md("#### Ejercicio:"))
        display(md(r"{} $\to$ {}".format(ejercicio, solucion)))
        print("enunciado_latex: " + ejercicio)
        print("solucion_latex: " + solucion)
        return ejercicio, solucion
    elif tipo == 1:
        display(md("#### Ejercicio:"))
        display(md(r"{} $\to$ {}".format(ejercicio, solucion)))
        print("enunciado_latex: " + ejercicio)
        print("solucion_latex: " + solucion)
        return ejercicio, solucion

        
    
```


```python
# Clasificar números

ejercicios=[
            [r'\frac{1}{2}', '\sqrt[3]{-27}'],
            
           ]

display(md("## Clasificar números:"))

for e in ejercicios :
    enunciado_latex = r"""\begin{tabular}{|c |c |c |c |c|}\hline
    &$\mathbb{N}$& $\mathbb{Z}$& $\mathbb{Q}$&$\mathbb{R}$\\ 
    \hline $"""
    enunciado_latex += r"""$&&&&\\ \hline $""".join(e)
    enunciado_latex += r'$ &&&&\\ \hline \end{tabular}'
    solucion_latex = r"""\begin{tabular}{|c |c |c |c |c|}\hline
    &$\mathbb{N}$& $\mathbb{Z}$& $\mathbb{Q}$&$\mathbb{R}$\\ 
    \hline"""
    for ee in e:
        n = parse_latex(ee)
        linea =  n in S.Naturals, ask(Q.integer(n)),ask(Q.rational(n)), n in S.Reals
        lista = []
        lista.append(r"${}$".format(ee))
        [lista.append(str(i)) for i in linea]
        #solucion_latex += r"""${}$&{}&{}&{}&{}\\ \hline """.format(n,linea[0],linea[1],linea[2],linea[3])
        solucion_latex += r""" & """.join(lista)
        solucion_latex += r"""\\ \hline """
        #print(n,lista)
    solucion_latex += r'\end{tabular}'


    #print(enunciado_latex)

    mostrar_ejercicio(enunciado_latex, solucion_latex)  

```


## Clasificar números:



#### Ejercicio:



\begin{tabular}{|c |c |c |c |c|}\hline
    &$\mathbb{N}$& $\mathbb{Z}$& $\mathbb{Q}$&$\mathbb{R}$\\ 
    \hline $\frac{1}{2}$&&&&\\ \hline $\sqrt[3]{-27}$ &&&&\\ \hline \end{tabular} $\to$ \begin{tabular}{|c |c |c |c |c|}\hline
    &$\mathbb{N}$& $\mathbb{Z}$& $\mathbb{Q}$&$\mathbb{R}$\\ 
    \hline$\frac{1}{2}$ & False & False & True & True\\ \hline $\sqrt[3]{-27}$ & False & False & False & False\\ \hline \end{tabular}


    enunciado_latex: \begin{tabular}{|c |c |c |c |c|}\hline
        &$\mathbb{N}$& $\mathbb{Z}$& $\mathbb{Q}$&$\mathbb{R}$\\ 
        \hline $\frac{1}{2}$&&&&\\ \hline $\sqrt[3]{-27}$ &&&&\\ \hline \end{tabular}
    solucion_latex: \begin{tabular}{|c |c |c |c |c|}\hline
        &$\mathbb{N}$& $\mathbb{Z}$& $\mathbb{Q}$&$\mathbb{R}$\\ 
        \hline$\frac{1}{2}$ & False & False & True & True\\ \hline $\sqrt[3]{-27}$ & False & False & False & False\\ \hline \end{tabular}



```python
# Conjuntos de números

display(md("## Calcula la Unión y la Intersección de los siguientes conjuntos (da el resultado en forma de intervalo y de desigualdad):"))

ejercicios=[
            [Interval.Ropen(2,10),Interval.open(7,12)],
            
           ]

for e in ejercicios:
    a=Interval.Ropen(2,10)
    b=Interval.open(7,12)
    ejercicio = r"$A="+latex(a)+r"$ y $B="+ latex(b)+r"$"
    solucion = r"$\{x|"+latex(a.union(b).as_relational(x))+r"\}$"
    mostrar_ejercicio(ejercicio,solucion)



```


## Calcula la Unión y la Intersección de los siguientes conjuntos (da el resultado en forma de intervalo y de desigualdad):



#### Ejercicio:



$A=\left[2, 10\right)$ y $B=\left(7, 12\right)$ $\to$ $\{x|2 \leq x \wedge x < 12\}$


    enunciado_latex: $A=\left[2, 10\right)$ y $B=\left(7, 12\right)$
    solucion_latex: $\{x|2 \leq x \wedge x < 12\}$



```python
# Operar potencias

ejercicios=[
            r'\frac{(2^3\cdot3^2\cdot5)^{-4}}{(2^{-2}\cdot3^{-3})^{3}}',
            
           ]

display(md("## Opera las siguientes pontecias:"))

  
#[mostrar_ejercicio(e, latex(simplify(parse_latex(e)))) for e in ejercicios]    

[mostrar_ejercicio("$"+e+"$", "$"+latex(S(parse_latex(r"\frac{"+latex(factorint(simplify(parse_latex(e)).as_numer_denom()[0] , visual=True))+r"}{" +latex(factorint(simplify(parse_latex(e)).as_numer_denom()[1], visual=True))+"}"), evaluate=False))+"$") for e in ejercicios]    



```


## Opera las siguientes pontecias:



#### Ejercicio:



$\frac{(2^3\cdot3^2\cdot5)^{-4}}{(2^{-2}\cdot3^{-3})^{3}}$ $\to$ $\frac{3^{1}}{2^{6} \cdot 5^{4}}$


    enunciado_latex: $\frac{(2^3\cdot3^2\cdot5)^{-4}}{(2^{-2}\cdot3^{-3})^{3}}$
    solucion_latex: $\frac{3^{1}}{2^{6} \cdot 5^{4}}$





    [('$\\frac{(2^3\\cdot3^2\\cdot5)^{-4}}{(2^{-2}\\cdot3^{-3})^{3}}$',
      '$\\frac{3^{1}}{2^{6} \\cdot 5^{4}}$')]




```python
# Operar potencias con variables

ejercicios=[
            r'(\frac{6p^3d^2}{5q})^4\cdot(\frac{20p^2q^3}{24d})^4'
           ]

display(md("## Opera las siguientes pontecias con variables:"))

  
[mostrar_ejercicio("$"+e+"$", "$"+latex(simplify(parse_latex(e)))+"$") for e in ejercicios]    

#[mostrar_ejercicio(e, latex(S(parse_latex(r"\frac{"+latex(factorint(simplify(parse_latex(e)).as_numer_denom()[0] , visual=True))+r"}{" +latex(factorint(simplify(parse_latex(e)).as_numer_denom()[1], visual=True))+"}"), evaluate=False))) for e in ejercicios]    



```


## Opera las siguientes pontecias con variables:



#### Ejercicio:



$(\frac{6p^3d^2}{5q})^4\cdot(\frac{20p^2q^3}{24d})^4$ $\to$ $d^{4} p^{20} q^{8}$


    enunciado_latex: $(\frac{6p^3d^2}{5q})^4\cdot(\frac{20p^2q^3}{24d})^4$
    solucion_latex: $d^{4} p^{20} q^{8}$





    [('$(\\frac{6p^3d^2}{5q})^4\\cdot(\\frac{20p^2q^3}{24d})^4$',
      '$d^{4} p^{20} q^{8}$')]




```python
# Operar en notación científica

ejercicios=[r'\frac{1000\cdot12000\cdot0.02\cdot0.01}{400\cdot0.00003}',
            
           ]

display(md("## Operar en notación científica:")) 
    
[mostrar_ejercicio("$"+e+"$", "$"+latex(np.format_float_scientific(cancel(parse_latex(e))))+"$") for e in ejercicios]    



```


## Operar en notación científica:



#### Ejercicio:



$\frac{1000\cdot12000\cdot0.02\cdot0.01}{400\cdot0.00003}$ $\to$ $2.e+05$


    enunciado_latex: $\frac{1000\cdot12000\cdot0.02\cdot0.01}{400\cdot0.00003}$
    solucion_latex: $2.e+05$





    [('$\\frac{1000\\cdot12000\\cdot0.02\\cdot0.01}{400\\cdot0.00003}$',
      '$2.e+05$')]




```python
# Simplificar radicales

ejercicios=[r'\sqrt[4]{\frac{25}{9}\sqrt[3]{\frac{9}{25}}}',
            r'4\sqrt{20}-3\sqrt{45}+11\sqrt{125}-20\sqrt{5}',
            r'\sqrt{72}\cdot3\sqrt{8}',
            r'\frac{(3\sqrt{2}+\sqrt{3})^2}{3}',
            r'\sqrt{2\sqrt{2\sqrt{2}}}',
            
           ]

display(md("## Simplificar radicales:"))
  
[mostrar_ejercicio("$"+e+"$", "$"+latex(simplify(parse_latex(e)))+"$") for e in ejercicios] 
            
            



```


## Simplificar radicales:



#### Ejercicio:



$\sqrt[4]{\frac{25}{9}\sqrt[3]{\frac{9}{25}}}$ $\to$ $\frac{3^{\frac{2}{3}} \sqrt[3]{5}}{3}$


    enunciado_latex: $\sqrt[4]{\frac{25}{9}\sqrt[3]{\frac{9}{25}}}$
    solucion_latex: $\frac{3^{\frac{2}{3}} \sqrt[3]{5}}{3}$



#### Ejercicio:



$4\sqrt{20}-3\sqrt{45}+11\sqrt{125}-20\sqrt{5}$ $\to$ $34 \sqrt{5}$


    enunciado_latex: $4\sqrt{20}-3\sqrt{45}+11\sqrt{125}-20\sqrt{5}$
    solucion_latex: $34 \sqrt{5}$



#### Ejercicio:



$\sqrt{72}\cdot3\sqrt{8}$ $\to$ $72$


    enunciado_latex: $\sqrt{72}\cdot3\sqrt{8}$
    solucion_latex: $72$



#### Ejercicio:



$\frac{(3\sqrt{2}+\sqrt{3})^2}{3}$ $\to$ $2 \sqrt{6} + 7$


    enunciado_latex: $\frac{(3\sqrt{2}+\sqrt{3})^2}{3}$
    solucion_latex: $2 \sqrt{6} + 7$



#### Ejercicio:



$\sqrt{2\sqrt{2\sqrt{2}}}$ $\to$ $2^{\frac{7}{8}}$


    enunciado_latex: $\sqrt{2\sqrt{2\sqrt{2}}}$
    solucion_latex: $2^{\frac{7}{8}}$





    [('$\\sqrt[4]{\\frac{25}{9}\\sqrt[3]{\\frac{9}{25}}}$',
      '$\\frac{3^{\\frac{2}{3}} \\sqrt[3]{5}}{3}$'),
     ('$4\\sqrt{20}-3\\sqrt{45}+11\\sqrt{125}-20\\sqrt{5}$', '$34 \\sqrt{5}$'),
     ('$\\sqrt{72}\\cdot3\\sqrt{8}$', '$72$'),
     ('$\\frac{(3\\sqrt{2}+\\sqrt{3})^2}{3}$', '$2 \\sqrt{6} + 7$'),
     ('$\\sqrt{2\\sqrt{2\\sqrt{2}}}$', '$2^{\\frac{7}{8}}$')]




```python
# Racionalizar radicales

ejercicios=[r'\frac{10}{2\sqrt{3}-\sqrt{2}}',
            r'\frac{\sqrt{45}+\sqrt{180}}{\sqrt{176}+4\sqrt{44}}'
           ]
display(md("## Racionalizar denominadores:"))
  
[mostrar_ejercicio("$"+e+"$", "$"+latex(radsimp(parse_latex(e)))+"$") for e in ejercicios]    



```


## Racionalizar denominadores:



#### Ejercicio:



$\frac{10}{2\sqrt{3}-\sqrt{2}}$ $\to$ $\sqrt{2} + 2 \sqrt{3}$


    enunciado_latex: $\frac{10}{2\sqrt{3}-\sqrt{2}}$
    solucion_latex: $\sqrt{2} + 2 \sqrt{3}$



#### Ejercicio:



$\frac{\sqrt{45}+\sqrt{180}}{\sqrt{176}+4\sqrt{44}}$ $\to$ $\frac{3 \sqrt{55}}{44}$


    enunciado_latex: $\frac{\sqrt{45}+\sqrt{180}}{\sqrt{176}+4\sqrt{44}}$
    solucion_latex: $\frac{3 \sqrt{55}}{44}$





    [('$\\frac{10}{2\\sqrt{3}-\\sqrt{2}}$', '$\\sqrt{2} + 2 \\sqrt{3}$'),
     ('$\\frac{\\sqrt{45}+\\sqrt{180}}{\\sqrt{176}+4\\sqrt{44}}$',
      '$\\frac{3 \\sqrt{55}}{44}$')]




```python
# Definición de logaritmo

ejercicios=[[r'\log_3{27}','log(27,3)'],
            [r'\log_3{1/81}','log(1/81,3)'],
            [r'\log_9 3',r'log(3,9)'],
            [r'\log_{1/3}{1/81}','log(1/81,1/3)'],
            [r'\log_5{\sqrt{125}}','log(sqrt(125),5)'],
            
            
           ]
display(md("## Definición de Logaritmo:"))

[mostrar_ejercicio("$"+e[0]+"$","$"+latex(simplify(S(e[1])))+"$") for e in ejercicios]



```


## Definición de Logaritmo:



#### Ejercicio:



$\log_3{27}$ $\to$ $3$


    enunciado_latex: $\log_3{27}$
    solucion_latex: $3$



#### Ejercicio:



$\log_3{1/81}$ $\to$ $-4$


    enunciado_latex: $\log_3{1/81}$
    solucion_latex: $-4$



#### Ejercicio:



$\log_9 3$ $\to$ $\frac{1}{2}$


    enunciado_latex: $\log_9 3$
    solucion_latex: $\frac{1}{2}$



#### Ejercicio:



$\log_{1/3}{1/81}$ $\to$ $4$


    enunciado_latex: $\log_{1/3}{1/81}$
    solucion_latex: $4$



#### Ejercicio:



$\log_5{\sqrt{125}}$ $\to$ $\frac{3}{2}$


    enunciado_latex: $\log_5{\sqrt{125}}$
    solucion_latex: $\frac{3}{2}$





    [('$\\log_3{27}$', '$3$'),
     ('$\\log_3{1/81}$', '$-4$'),
     ('$\\log_9 3$', '$\\frac{1}{2}$'),
     ('$\\log_{1/3}{1/81}$', '$4$'),
     ('$\\log_5{\\sqrt{125}}$', '$\\frac{3}{2}$')]




```python
# Definición de logaritmo

ejercicios=[[r'\log_3{27}','log(27,3)'],
            [r'\log_3{1/81}','log(1/81,3)'],
            [r'\log_9 3',r'log(3,9)'],
            [r'\log_{1/3}{1/81}','log(1/81,1/3)'],
            [r'\log_5{\sqrt{125}}','log(sqrt(125),5)'],
            
            
           ]
display(md("## Definición de Logaritmo:"))

[mostrar_ejercicio("$"+e[0]+"$","$"+latex(simplify(S(e[1])))+"$") for e in ejercicios]



```


## Definición de Logaritmo:



#### Ejercicio:



$\log_3{27}$ $\to$ $3$


    enunciado_latex: $\log_3{27}$
    solucion_latex: $3$



#### Ejercicio:



$\log_3{1/81}$ $\to$ $-4$


    enunciado_latex: $\log_3{1/81}$
    solucion_latex: $-4$



#### Ejercicio:



$\log_9 3$ $\to$ $\frac{1}{2}$


    enunciado_latex: $\log_9 3$
    solucion_latex: $\frac{1}{2}$



#### Ejercicio:



$\log_{1/3}{1/81}$ $\to$ $4$


    enunciado_latex: $\log_{1/3}{1/81}$
    solucion_latex: $4$



#### Ejercicio:



$\log_5{\sqrt{125}}$ $\to$ $\frac{3}{2}$


    enunciado_latex: $\log_5{\sqrt{125}}$
    solucion_latex: $\frac{3}{2}$





    [('$\\log_3{27}$', '$3$'),
     ('$\\log_3{1/81}$', '$-4$'),
     ('$\\log_9 3$', '$\\frac{1}{2}$'),
     ('$\\log_{1/3}{1/81}$', '$4$'),
     ('$\\log_5{\\sqrt{125}}$', '$\\frac{3}{2}$')]




```python
# Definición de logaritmo

ejercicios=[[r'\log_3 \frac{1}{9} -  \log_5 0.2 +\log_6 \frac{1}{36} - \log_2 0.5',
             'log(1/9,3)-log(0.2,5)+log(1/36,6)-log(0.5,2)'], 
            [r'2\log_4 16 +  log_2 32 - 3log_7 49',
            r'2*log(16,4)+log(32,2)-3*log(49,7)']
           ]
display(md("## Definición de Logaritmo y operaciones:"))
    
[mostrar_ejercicio("$"+e[0]+"$","$"+e[0]+ r"= ("+r" )+( ".join([latex(S(i).evalf(2)) for i in S(e[1], evaluate=False).args])+r")="+latex(simplify(S(e[1])).evalf(2))+"$") for e in ejercicios]   

```


## Definición de Logaritmo y operaciones:



#### Ejercicio:



$\log_3 \frac{1}{9} -  \log_5 0.2 +\log_6 \frac{1}{36} - \log_2 0.5$ $\to$ $\log_3 \frac{1}{9} -  \log_5 0.2 +\log_6 \frac{1}{36} - \log_2 0.5= (-2.0 )+( 1.0 )+( -2.0 )+( 1.0)=-2.0$


    enunciado_latex: $\log_3 \frac{1}{9} -  \log_5 0.2 +\log_6 \frac{1}{36} - \log_2 0.5$
    solucion_latex: $\log_3 \frac{1}{9} -  \log_5 0.2 +\log_6 \frac{1}{36} - \log_2 0.5= (-2.0 )+( 1.0 )+( -2.0 )+( 1.0)=-2.0$



#### Ejercicio:



$2\log_4 16 +  log_2 32 - 3log_7 49$ $\to$ $2\log_4 16 +  log_2 32 - 3log_7 49= (4.0 )+( 5.0 )+( -6.0)=3.0$


    enunciado_latex: $2\log_4 16 +  log_2 32 - 3log_7 49$
    solucion_latex: $2\log_4 16 +  log_2 32 - 3log_7 49= (4.0 )+( 5.0 )+( -6.0)=3.0$





    [('$\\log_3 \\frac{1}{9} -  \\log_5 0.2 +\\log_6 \\frac{1}{36} - \\log_2 0.5$',
      '$\\log_3 \\frac{1}{9} -  \\log_5 0.2 +\\log_6 \\frac{1}{36} - \\log_2 0.5= (-2.0 )+( 1.0 )+( -2.0 )+( 1.0)=-2.0$'),
     ('$2\\log_4 16 +  log_2 32 - 3log_7 49$',
      '$2\\log_4 16 +  log_2 32 - 3log_7 49= (4.0 )+( 5.0 )+( -6.0)=3.0$')]




```python
# Propiedades de los logaritmos - combinar

ejercicios=[[r'\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9',
             'log(10,2)+2*log(3,2)-log(5,2)-log(9,2)'],
            

            
           ]
display(md("## Propiedades de los logaritmos - combinar"))

    
[mostrar_ejercicio("$"+e[0]+"$","$"+e[0]+r"="+latex(logcombine(S(e[1])))+r"="+latex(simplify(S(e[1])))+"$") for e in ejercicios]
    



```


## Propiedades de los logaritmos - combinar



#### Ejercicio:



$\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9$ $\to$ $\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9=\log{\left(\frac{3^{\frac{2}{\log{\left(2 \right)}}}}{9^{\frac{1}{\log{\left(2 \right)}}}} \right)} + 1=1$


    enunciado_latex: $\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9$
    solucion_latex: $\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9=\log{\left(\frac{3^{\frac{2}{\log{\left(2 \right)}}}}{9^{\frac{1}{\log{\left(2 \right)}}}} \right)} + 1=1$





    [('$\\log_2 10 + 2\\log_2 3 - \\log_2 5 - \\log_2 9$',
      '$\\log_2 10 + 2\\log_2 3 - \\log_2 5 - \\log_2 9=\\log{\\left(\\frac{3^{\\frac{2}{\\log{\\left(2 \\right)}}}}{9^{\\frac{1}{\\log{\\left(2 \\right)}}}} \\right)} + 1=1$')]




```python
# Propiedades de los logaritmos - expandir

ejercicios=[[r'\log (x\cdot y)','log(x*y)', 1.3, 0.8],
            [r'\log (x\cdot \sqrt{y})','log(x*sqrt(y))', 1.3, 0.8],
            [r'\log (\frac{y}{x^2})','log(y/(x**2))', 1.3, 0.8],
            [r'\log (\sqrt{\frac{x}{y}})','log(sqrt(x/y))', 1.3, 0.8],
            [r'\log (\frac{8\cdot x^2}{\sqrt{y}})','log((8*x**2)/sqrt(y))', 1.5, -0.6],
            

            
           ]
display(md("## Propiedades de los logaritmos - expandir"))

    
[mostrar_ejercicio("Sabiendo que $\log x={}$ y $\log y={}$,calcula $".format(e[2],e[3])+e[0]+"$",
                   "$"+e[0]+r"="+latex(expand_log(S(e[1]),force=True))+r"="+latex(expand_log(S(e[1]),force=True).subs(log(x),UnevaluatedExpr(e[2])).subs(log(y),UnevaluatedExpr(e[3])))+"="+latex(expand_log(S(e[1]),force=True).subs(log(x),e[2]).subs(log(y),e[3]))+"$") for e in ejercicios]
    



```


## Propiedades de los logaritmos - expandir



#### Ejercicio:



Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (x\cdot y)$ $\to$ $\log (x\cdot y)=\log{\left(x \right)} + \log{\left(y \right)}=0.8 + 1.3=2.1$


    enunciado_latex: Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (x\cdot y)$
    solucion_latex: $\log (x\cdot y)=\log{\left(x \right)} + \log{\left(y \right)}=0.8 + 1.3=2.1$



#### Ejercicio:



Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (x\cdot \sqrt{y})$ $\to$ $\log (x\cdot \sqrt{y})=\log{\left(x \right)} + \frac{\log{\left(y \right)}}{2}=\frac{0.8}{2} + 1.3=1.7$


    enunciado_latex: Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (x\cdot \sqrt{y})$
    solucion_latex: $\log (x\cdot \sqrt{y})=\log{\left(x \right)} + \frac{\log{\left(y \right)}}{2}=\frac{0.8}{2} + 1.3=1.7$



#### Ejercicio:



Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (\frac{y}{x^2})$ $\to$ $\log (\frac{y}{x^2})=- 2 \log{\left(x \right)} + \log{\left(y \right)}=0.8 - 2 \cdot 1.3=-1.8$


    enunciado_latex: Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (\frac{y}{x^2})$
    solucion_latex: $\log (\frac{y}{x^2})=- 2 \log{\left(x \right)} + \log{\left(y \right)}=0.8 - 2 \cdot 1.3=-1.8$



#### Ejercicio:



Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (\sqrt{\frac{x}{y}})$ $\to$ $\log (\sqrt{\frac{x}{y}})=\frac{\log{\left(x \right)}}{2} - \frac{\log{\left(y \right)}}{2}=- \frac{0.8}{2} + \frac{1.3}{2}=0.25$


    enunciado_latex: Sabiendo que $\log x=1.3$ y $\log y=0.8$,calcula $\log (\sqrt{\frac{x}{y}})$
    solucion_latex: $\log (\sqrt{\frac{x}{y}})=\frac{\log{\left(x \right)}}{2} - \frac{\log{\left(y \right)}}{2}=- \frac{0.8}{2} + \frac{1.3}{2}=0.25$



#### Ejercicio:



Sabiendo que $\log x=1.5$ y $\log y=-0.6$,calcula $\log (\frac{8\cdot x^2}{\sqrt{y}})$ $\to$ $\log (\frac{8\cdot x^2}{\sqrt{y}})=2 \log{\left(x \right)} - \frac{\log{\left(y \right)}}{2} + 3 \log{\left(2 \right)}=3 \log{\left(2 \right)} - \frac{-0.6}{2} + 2 \cdot 1.5=3 \log{\left(2 \right)} + 3.3$


    enunciado_latex: Sabiendo que $\log x=1.5$ y $\log y=-0.6$,calcula $\log (\frac{8\cdot x^2}{\sqrt{y}})$
    solucion_latex: $\log (\frac{8\cdot x^2}{\sqrt{y}})=2 \log{\left(x \right)} - \frac{\log{\left(y \right)}}{2} + 3 \log{\left(2 \right)}=3 \log{\left(2 \right)} - \frac{-0.6}{2} + 2 \cdot 1.5=3 \log{\left(2 \right)} + 3.3$





    [('Sabiendo que $\\log x=1.3$ y $\\log y=0.8$,calcula $\\log (x\\cdot y)$',
      '$\\log (x\\cdot y)=\\log{\\left(x \\right)} + \\log{\\left(y \\right)}=0.8 + 1.3=2.1$'),
     ('Sabiendo que $\\log x=1.3$ y $\\log y=0.8$,calcula $\\log (x\\cdot \\sqrt{y})$',
      '$\\log (x\\cdot \\sqrt{y})=\\log{\\left(x \\right)} + \\frac{\\log{\\left(y \\right)}}{2}=\\frac{0.8}{2} + 1.3=1.7$'),
     ('Sabiendo que $\\log x=1.3$ y $\\log y=0.8$,calcula $\\log (\\frac{y}{x^2})$',
      '$\\log (\\frac{y}{x^2})=- 2 \\log{\\left(x \\right)} + \\log{\\left(y \\right)}=0.8 - 2 \\cdot 1.3=-1.8$'),
     ('Sabiendo que $\\log x=1.3$ y $\\log y=0.8$,calcula $\\log (\\sqrt{\\frac{x}{y}})$',
      '$\\log (\\sqrt{\\frac{x}{y}})=\\frac{\\log{\\left(x \\right)}}{2} - \\frac{\\log{\\left(y \\right)}}{2}=- \\frac{0.8}{2} + \\frac{1.3}{2}=0.25$'),
     ('Sabiendo que $\\log x=1.5$ y $\\log y=-0.6$,calcula $\\log (\\frac{8\\cdot x^2}{\\sqrt{y}})$',
      '$\\log (\\frac{8\\cdot x^2}{\\sqrt{y}})=2 \\log{\\left(x \\right)} - \\frac{\\log{\\left(y \\right)}}{2} + 3 \\log{\\left(2 \\right)}=3 \\log{\\left(2 \\right)} - \\frac{-0.6}{2} + 2 \\cdot 1.5=3 \\log{\\left(2 \\right)} + 3.3$')]




```python
expand_log(log(x*y),force=True)
UnevaluatedExpr(log(x,2))
S('log(x,2)', evaluate=False)
```




$\displaystyle \frac{\log{\left(x \right)}}{\log{\left(2 \right)}}$




```python
# Propiedades de los logaritmos

ejercicios=[[r'\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9',
             'log(10,2)+2*log(3,2)-log(5,2)-log(9,2)'],

            
           ]
display(md("## Propiedades de los logaritmos"))
  
for e in ejercicios :
    display(md("#### Ejercicio:"))
    ejercicio = e[0]
    solucion = simplify(S(e[1]))
    display(md(r"${} \to {}$".format(ejercicio, solucion)))
    print("enunciado_latex: " + ejercicio)
    print("solucion_latex: " + latex(solucion))
    
[mostrar_ejercicio("$"+e[0]+"$","$"+latex(simplify(S(e[1])))+"$") for e in ejercicios]
    



```


## Propiedades de los logaritmos



#### Ejercicio:



$\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9 \to 1$


    enunciado_latex: \log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9
    solucion_latex: 1



#### Ejercicio:



$\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9$ $\to$ $1$


    enunciado_latex: $\log_2 10 + 2\log_2 3 - \log_2 5 - \log_2 9$
    solucion_latex: $1$





    [('$\\log_2 10 + 2\\log_2 3 - \\log_2 5 - \\log_2 9$', '$1$')]


