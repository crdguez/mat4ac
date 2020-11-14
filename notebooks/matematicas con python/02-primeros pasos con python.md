
## Primeros pasos con Python
### Hola mundo
La celda que tienes a continuación es una instrucción en Python. ¡Ejecútala!:


```python
print("Modifica este texto")
```

    Modifica este texto


### Cálculos y variables
Comenzaremos con algunos cálculos simples y
luego pasaremos a las variables. Las variables son una forma de almacenar
cosas en un programa, y resultan muy útiles.

#### Calculando con Python

Podemos usar Python como una calculadora. Veamos un ejemplo, para multiplicar *52 x 23*:



```python
52*23
```




    1196



Si te fijas, el operador multiplicador en Python es el `*` . También debes tener en cuenta que el separado de decimales ne Python es el punto. Por tanto, para multiplicar *52 x 2,3*:


```python
52*2.3
```




    119.6



En la siguiente tabla tienes los diferentes operadores:

|Operador Python|Operación matemática|
|:-------------:|:------------------:|
|+              |Suma                |
|-              |Resta               |
|*              |Multiplicación      |
|/              |División            |
|**             |Potencia            |

___
**IMPORTANTE:** La jerquía de operaciones en Python es la misma que se sigue en matemátics, por esta razón, deberemos controlar el orden que queramos con el uso de paréntesis. Si tienes que anidar paréntesis, es decir poner un paréntesis dentro de otro paréntesis, en Python usarás siempre paréntesis y no corchetes como utilzarías al escribir matemáticas en un cuaderno.

***

#### Variables 

Las variable en programación representan un lugar para almacenar información como números, texto, listas de números y texto, etc.

**Ejemplo:**


Tenemos guardado en  nuestra hucha: 23 billetes de 5 euros, 15 billetes de 10 euros, 12 monedas de 2 euros, 10 monedas de euo y 20 monedas de 50 centimos. ¿Cuánto dinero tenemos?

Podemos escribir lo siguiente para hacer el cálculo:



```python
23*5+15*10+12*2+10*1+20*0.50
```




    309.0



El mismo cálculo lo podemos hacer usando variables o contenedores de información que reflejen la cantidad de billetes y monedas de cada tipo que hay:


```python
billetes_cinco = 23
billetes_diez = 15
monedas_dos = 12
monedas_uno = 10
monedas_cincuenta = 20
```

Podemos comprobar qué dato contiene cada variable escribiendo el nombre de la variable:


```python
billetes_cinco
```




    23



La operación que hemos escrito antes la podemos reescribir pero haciendo referencia a las variables:


```python
billetes_cinco * 5 + billetes_diez * 10 + monedas_dos * 2 + monedas_uno * 1 + monedas_cincuenta * 0.50
```




    309.0



Incluso podemos crear una variable *dinero* nueva que sea la operación que a su vez contiene variables:


```python
dinero = billetes_cinco * 5 + billetes_diez * 10 + monedas_dos * 2 + monedas_uno * 1 + monedas_cincuenta * 0.50
```

Si ejecutamos:


```python
dinero
```




    309.0



Obtenemos la cantidad de dinero que tenemos. Supongamos ahora que hacemos recuento de billetes y monedas, y nos damos cuenta que la vez anterior hemos contado mal y en realidad tenemos 22 billetes de 5 euros. En lugar de tener que volver a escribir todos los números de la operación podemos hacer lo siguiente:


```python
billetes_cinco = 22
billetes_cinco * 5 + billetes_diez * 10 + monedas_dos * 2 + monedas_uno * 1 + monedas_cincuenta * 0.50
```




    304.0


