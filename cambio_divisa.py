
def main():
    print('por favor ingrese la cantidad de cordobsa que desea cambiar a colones')
    x=float(input('Cordobas = '))

    print('Colones = '+cambio(x))

    
def cambio(cor):
    cam = str(cor * 16.68)
    return cam


if __name__ == "__main__":
    main()
