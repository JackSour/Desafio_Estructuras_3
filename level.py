def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 2:
        if n_pregunta <= 2:
            level = 'basicas'
        elif n_pregunta <= 4:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 3:
        if n_pregunta <= 3:
            level = 'basicas'
        elif n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    else:
        raise ValueError("La cantidad de preguntas por nivel debe ser 1, 2 o 3.")
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # basicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias