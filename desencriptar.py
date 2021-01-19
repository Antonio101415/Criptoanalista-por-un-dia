
import sys, random

LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def main():
    mensaje=input("Introduce la cadena cifrada: ")
    llave = 'EVUDOGPANJWYBIFHQMLÑTSKRXCZ'
    Modo = 'decrypt' # Decir si queremos encrypt o decrypt

    checkValidKey(llave)

    if Modo == 'decrypt':
        translated = encryptMessage(llave, mensaje)
    elif Modo == 'decrypt':
        translated = decryptMessage(llave, mensaje)
    print('Se ha usado la llave: %s' % (llave))
    print('El resultado de la  %sed  es :' % (Modo))
    print(translated)


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('Hay un error en la cadena de la key o valor introducido no compatible.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'descrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # Para realizar el encriptado podemos usar la misma llave solo debemos
        # Cambiar la nueva key para intercambiar la cadena de las letras
        charsA, charsB = charsB, charsA

    # En este bucle recorremos todo el mensaje
    for symbol in message:
        if symbol.upper() in charsA:
            # Encriptamos o desincriptamos el mensaje
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Añadimos la traduccion al simbolo si no esta en letras
            translated += symbol

    return translated

main()