
#Importación de funciones
from operator import truediv
import math as m

#Validación de datos por medio de funciones

def validarEntero(numero): 
    while not numero.isdigit():
        numero=input("Error, debe ingresar un numero  ")
    return int(numero)

def validarReal(text):
     
    while  True:
        numero=input("\n "+text)
        try:
            numero =float(numero)
            return numero        
    
        except ValueError:
            print("Error, debe ingresar un numero  ")

#Calcula e imprime el volumen del tanque
def volumenTanque(longitud,diametro):
   
    volumen=((m.pi*(diametro**2))/4)*longitud
    print("\n\n El volumen es: " + str(volumen))
    return volumen

#Calcula e imprime el volumen del líquido
def volumenLiquido(altura,diametro,longitud):
    razon=(altura/diametro)
    #Imprime en pantalla
    print ("\nLa razon es: "+ str(razon))
    fraccion=0
    eleccion=validarEntero(input("\nIngrese 0 si posee la tabla 6.5 del manual del ingeniero químico\nIngrese 1 si no cuenta con la tabla 6.5 del manual del ingeniero químico:\n "))
    if eleccion==0:
        fraccion=interpolacion(razon)
    elif eleccion==1:
        fraccion= fVolumen(altura,diametro)
    else:
        exit

    volumenLi=(fraccion)*volumenTanque(longitud,diametro)
    print("\n\n El volumen del liquido es: " + str(volumenLi))

def interpolacion(x):
    
    x1=validarReal("Ingrese un valor menor a la razon H/D="+str(x)+", según la tabla 6.5: ")
    y1=validarReal("Ingrese un valor menor a la fraccion de volumen de la razon H/D="+str(x)+": ")
    x2=validarReal("Ingrese un valor mayor a la razon H/D="+str(x)+", según la tabla 6.5: ")
    y2=validarReal("Ingrese un valor mayor a la fraccion de volumen de la razon H/D="+str(x)+": ")
    y=(((y2*x)-(y1*x)-(y2*x1)+(y1*x1))/(x2-x1))+y1   
    print("\n El valor de la fraccion de volumen es: " +str(y))
    return y


def fVolumen(altura,diametro):
    
    
    
    angulo=m.degrees(m.acos(1-((2*altura)/diametro)))
    print("\nEl angulo es: "+ str(angulo))
    x=(angulo/180)
    print("x es igual a: "+str(x))
    y=(m.sin(m.acos(1-((2*altura)/diametro))))
    print("y es igual a: "+str(y))
    z=(m.cos(m.acos(1-((2*altura)/diametro))))
    print("z es igual a: "+str(z))
  
    fraccion=x-((y*z)/m.pi)
    print("\nEl valor de la fraccion volumen es: "+ str(fraccion))
    return fraccion



   

       


