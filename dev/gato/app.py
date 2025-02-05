import tablero

def main():
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    g = tablero.juego(dsimbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print(f'Empate')

if __name__ == '__main__':
    main()