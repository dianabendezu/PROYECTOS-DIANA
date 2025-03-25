#Elabora un programa para calcular la raíz cúbica de un número que se ingrese
#ENTRADA


#PROCESO
import math #impotando libreria math
varNumero = int(input("Ingresar número: ")) #solicita el ingreso de un número, se convierte en tipo entero, se asigna variable varNumero
#raizCubica = varNúmero**(1/3)
raízCubica = pow(varNumero,(1/3)) #asignación

#SALIDA
print(raízCubica)


