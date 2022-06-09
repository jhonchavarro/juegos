#juego del ahorcado
#@jhonchavarro
"""
explicacion
1.elegir aleatoriamente una palabra de una lista de palabras.
2.mostrar el dibujo de una horca.
3.mostrar un guion baja por cada letra de la palabra.
4.pedir al ususario que introduzca una letra:si no es una unica letra indicalo.si ya se ha dicho indicarlo.
5.COmprobar si esa letra esta contenida en la palabra elegida
6.si esta:volver a mostrar el dibujo de la horca como la ultima vez. sustituir el guion correspondiente por la letra dicha.
7.si no esta:mostrar el dibujo de la horca al que se añade una parte.
8. si se fallan 6 veces:se completa el dibujo del ahorcado.
9.si se acierta todas las letras de la palabra:GANO!
"""
import random
import os
palabras=["COLOMBIA","ECUADOR","VENEZUELA","BRASIL","ARGENTINA","PERU","CHILE","BOLIVIA","PARAGUAY","URUGUAY","GUYANA","SURINAM"]
palabra=random.choice(palabras)

fallo0="""
    !===N
        N
        N
        N
=========
"""
fallo1="""
     !===N
     o   N
         N
         N
 =========
"""
fallo2="""
     !===N
    _o   N
         N
         N
 =========
"""
fallo3="""
     !===N
     _O_ N
        N
        N
=========
"""
fallo4="""
    !===N
   _O_  N
    |   N
        N
=========
"""
fallo5="""
    !===N
   _O_  N
    |   N
   /    N
=========
"""
fallo6="""
    !===N
    _o_ N
     |  N
    / \ N
=========
"""
letras_correctas=""#letras correctas dichas por el usuario
letras_todas=""#todas las letras dichas por el usuario
fallos=0

while True:
  os.system("cls")
  print("********************")
  print("**JUEGO DEL AHORCADO**")
  print("********************")
  if fallos == 0:
    print(fallo0)
  elif fallos == 1:
    print(fallo1)
  elif fallos == 2:
    print(fallo2)
  elif fallos == 3:
    print(fallo3)
  elif fallos == 4:
    print(fallo4)
  elif fallos == 5:
    print(fallo5)
  elif fallos == 6:
    print(fallo6)

  print()

  #mostramos las palabras acertadas y guiones bajo en las no acertadas 
  resultados =""

  for letra in palabras:
    if letra in letras_correctas:
      resultados += letra
    else:
      resultados += "_"
  print("    {}".format(resultados))
  print()
  print()
  #comprobamos si se ha acertado la palabra o se han terminado los intentos.
  if resultados == palabras:
    print("***has ganado***")
    break
  if fallos>5:
    print("la palabras es:",palabra)
    print("***has perdido***")
    break 
  #bucle para que el usuario teclee una letra que cumpla los requisitos
  while True:
    letra_usuario_sin_formato=input("dime una letra:")
    letra_usuario=letra_usuario_sin_formato.upper()
    if len(letra_usuario)<1 or len(letra_usuario)>1:
      print("introduce una letra")
    elif letra_usuario in letras_todas: 
      print("esa letra ya la has dicho")
    elif not letra_usuario.isalpha():
      print("introduce una letra")
    else:
      letras_todas += letra_usuario
      break
  #comprobamos si la letra dicha por el usuario esta en la palabra
  if letra_usuario not in palabra:
    fallos +=1
  else: 
    letras_correctas += letra_usuario