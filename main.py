
#tarea como hacer para validar que un usuario dijite solo numeros enteros
#que el id se dijite con un numero aleatorio con ramdon
#modificar elementos de una lista
#terminar todo



bandas =[]


opcion=None
while (opcion!= 5):
    print('***FESTIVAL ALTAVOZ***')
    print('**********************')
    print('1.Agregar Banda')
    print('2.Ver cartel del festical')
    print('3.Buscar una banda')
    print('2.Modificar banda')
    print('5.Finalizar')
    
    opcion =int(input('dijita una opcion:'))
    
    if opcion==1 :
        banda={}
        #se pide o se llena el objeto de banda
        banda['id']=int(input('Dijite el id:  '))
        banda['nombre']=(input("Dijite el nombre de la banda: "))
        banda['genero']=(input("Dijite genero: "))
        banda['clasificacion']= int(input("Dijite clasificacion: "))
        banda['costo']=float(input("Dijite costo: $"))
        banda['tiempo']= input ("¿Cuanto tiempo dura su actuación?: ")
        
        #como agrego un diccionario a una  lista
        bandas.append(banda)
        print(bandas)
        
    elif opcion==2:
        #muestra los datos de la banda si existe
       # input(f'estas sonlas bandas a tocar{bandas} ')
        
        #recorriendo una lista para imprimir sus elementos
        for bandaAuxiliar in bandas:
            print(f'{bandaAuxiliar['id']}---{bandaAuxiliar['nombre']}')
    elif opcion==3:
       # busca una banda por medio del nombre en una lista
       busquedabanda=input ('que nombre de banda deseas buscar?')
       for bandaAuxiliar in bandas:
           if bandaAuxiliar['nombre']== busquedabanda:
               print(f'la informacion de esta banda es:{busquedabanda} ')
               break
           else:
               print('banda no encontrada')
           
       
       
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        print('opcion invalida.....dijite un valor numerico del 1 al 5')