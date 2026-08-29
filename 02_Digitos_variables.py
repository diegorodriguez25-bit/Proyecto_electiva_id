# Trabajo en clase parte 2 Digitos variables
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Diego Alejandro Rodriguez Araque_ 202114910
nombre= (input("Digite su nombre: "))
edad= int (input ("Digite su edad: "))
temp= float (input ("Digite su temperatura corporal: "))
nota= float (input ("Digite la nota que obtuvo en su capacitación (de 0.0 a 5.0): "))
carnet= (input ("Confirme su carnet (si o no): "))
mayor_edad = edad >= 18
temp_adecuada = temp <= 38.5
cap_aprobada =nota >= 3.0
tiene_carnet = carnet == "Si"
cumple_requisitos = mayor_edad and temp_adecuada and cap_aprobada and tiene_carnet
print('nombre', nombre)
print('edad', mayor_edad)
print('temp', temp_adecuada)
print('nota', cap_aprobada)
print('carnét', tiene_carnet)
print('Cumplimiento de requisitos: ',  cumple_requisitos)
