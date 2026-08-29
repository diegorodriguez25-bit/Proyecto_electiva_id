# Trabajo en clase parte 3 Digitos variables
# Diego Alejandro Rodriguez Araque_ 202114910
# Apuntes parte de digitos variables con limites
# Online Python compiler (interpreter) to run Python online.
nota= float(input ("Nota:"))
if nota < 0 or nota>5:
    print ("Nota no valida")
elif nota < 3:
    print("Insuficiente")
elif nota <4:
    print ("Basico")
elif nota < 4.6:
    print ("Alto")
else:
    print("Superior") 