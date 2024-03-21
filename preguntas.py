preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuál es la función básica para imprimir en la consola en Python?'],
    'alternativas': [['print()', 1], 
                     ['display()', 0], 
                     ['show()', 0], 
                     ['write()', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es el resultado de la expresión "5 + 3 * 2" en Python?'],
    'alternativas': [['16', 0], 
                     ['11', 1], 
                     ['10', 0], 
                     ['13', 0]]},
    
'pregunta_3': {'enunciado':['¿Cómo se llama el método que convierte una cadena a minúsculas en Python?'],
    'alternativas': [['upper()', 0], 
                     ['lower()', 1], 
                     ['capitalize()', 0], 
                     ['casefold()', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Cuál de las siguientes opciones es una forma correcta de abrir un archivo en Python en modo lectura?'],
    'alternativas': [['open("archivo.txt", "r")', 1], 
                     ['open("archivo.txt", "read")', 0], 
                     ['open("archivo.txt", "w")', 0], 
                     ['open("archivo.txt", "write")', 0]]},
    'pregunta_2': {'enunciado':['¿Qué hace el método "append()" en una lista en Python?'],
    'alternativas': [['Añade un elemento al principio de la lista', 0], 
                     ['Añade un elemento al final de la lista', 1], 
                     ['Elimina un elemento de la lista', 0], 
                     ['Ordena la lista en orden ascendente', 0]]},
    
'pregunta_3': {'enunciado':['¿Cuál es la salida de "len("¡Hola!")" en Python?'],
    'alternativas': [['6', 0], 
                     ['5', 1], 
                     ['4', 0], 
                     ['7', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Cuál de los siguientes enfoques es más eficiente para unir múltiples cadenas en Python?'],
    'alternativas': [['Utilizar el operador "+"', 0], 
                     ['Utilizar el método "join()" de cadenas', 1], 
                     ['Utilizar la función "concatenate()"', 0], 
                     ['Utilizar un bucle "for"', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es la diferencia entre una lista y una tupla en Python?'],
    'alternativas': [['Las listas son mutables, las tuplas son inmutables', 1], 
                     ['Las listas pueden contener elementos de diferentes tipos de datos, las tuplas no', 0], 
                     ['Las listas están ordenadas, las tuplas no', 0], 
                     ['Las listas tienen un tamaño fijo, las tuplas no', 0]]},
    
'pregunta_3': {'enunciado':['¿Qué hace el operador "lambda" en Python?'],
    'alternativas': [['Define una función anónima', 1], 
                     ['Realiza operaciones lógicas entre dos valores', 0], 
                     ['Indica un valor nulo', 0], 
                     ['Divide dos números', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}