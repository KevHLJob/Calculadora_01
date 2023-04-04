
#variables de los números que seran calculados... 
number1=int(input("Ingresa un número: "))
number2=int(input("Ingrese el segundo número: "))

#inicialización de variable
menu=0

#ciclo while 
#mientras las opciones no sean diferentes o iguales a 
while menu != 6:
    
    # Menu
    print("""
         Menú:   
    1)Suma
    2)Resta
    3)multiplicación
    4)División
    5)Cambiar Valores
    6)Salir
    """)
    
    menu = int(input("Por favor digite el número de la operación: "))
    
    if menu==1:
        print("")
        ope=number1+number2
        print("Resultado es: ", number1,"+",number2,"=",ope)
        
    if menu==2:
        print("")
        ope=number1-number2
        print("Resultado es: ", number1,"-",number2,"=",ope)
        
    if menu==3:
        print("")
        ope=number1*number2
        print("Resultado es: ", number1,"*",number2,"=",ope)
    
    if menu==4:
        print("")
        ope=number1/number2
        print("Resultado es: ", number1,"/",number2,"=",ope)
        
    if menu==5:
        print("")
        number1=int(input("Ingresa un número: "))
        number2=int(input("Ingrese el segundo número: "))
        
    if menu ==6:
        print("")
        print("Calculadora básica creada por: KevDev")    