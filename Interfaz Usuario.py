import AlgoritmoGenetico
import os
from os import system,name

#f = open ('holamundo.txt','r')
#print(f.read(11))
#print(f.read())

#f.write('hola mundo')
#f.close()

#Creamos directorios de ser necesario para guardar informacion
if not os.path.exists("ConocimientoLeon"):
	os.mkdir("ConocimientoLeon")

#Variable para majerar las configuraciones del algoritmo
config = AlgoritmoGenetico.ConfiguracionInicial()
def Limpia_Pantalla():
	if name =='nt':
		_ =system('cls')
	else:
		_ = system('clear')

def ValidaEntrada():
	try:
		opcion = int(input())
		return opcion
	except TypeError as e:
		print("Debe ingresar un número entero válido como opción\nOpción: ",end=' ')
		return str('Inf')

def MenuSecundario():
	print("\n¿Qué desea hacer ahora?\n1.-Regresar al menu principal\n2.-Salir\nOpción:",end=' ')
	sys.stdout.flush()
	opcion = int(input())
	while opcion <1 or opcion >2:
		print("Opción no válida. Opción:",end=' ')
		opcion= int(input())

	if opcion == 1:
		MenuPrincipal()
	else:
		return

def BuscaSolucion(generacion,numero):
	f =open("./ConocimientoLeon/UltimaSimulacion.txt","r")
	for i in range(generacion-1):
		for j in range(10):
			chunk = f.read(74)

	for i in range(numero+1):
		chunk = f.read(74)
	print(chunk[19:20])
	print(chunk[26:27])
	print(chunk[34:35])
	print(chunk[44:45])
	print(chunk[52:53])
	print(chunk[61:62])
	return AlgoritmoGenetico.Solucion(int(chunk[19:20]), int(chunk[26:27]), int(chunk[34:35]), int(chunk[44:45]), int(chunk[52:53]), int(chunk[61:62]))
	

def CuentaGeneraciones():
	try:
		generaciones = 0
		f=open("./ConocimientoLeon/UltimaSimulacion.txt","r")
		chunk = f.read(74)
		while chunk !='':
			generaciones+=1
			for i in range(9):
				chunk = f.read(74)
		return generaciones
	except IOError :
		return -1

def ConfiguraPosicionLeon():
	print("\n****** Configuración León ********\n")
	config.boolPosicionesValidas = True
	print("¿Cuantas posiciones de inicio validas tendrá el león\nCantidad:",end=' ')
	cantidad = int(input())
	while cantidad < 1 or cantidad >8:
		if cantidad < 1:
			print("Debe de haber al menos una posición. Cantidad:",end=' ')
		else:
			print("Solo existen 8 posiciones en el sistema. Cantidad:",end=' ')
		cantidad = int(input())
	print("\n")

	for i in range(cantidad):
		print(f"Ingrese la posición de inicio válida {i+1}: ",end=' ')
		val = int(input())
		while (val < 1 or val > 8) or val in config.PosValidas:
			if val < 1 or val > 8:
				print(f"Posición no valida. Posicón {i+1}:",end = ' ')
			else:
				print("La posición ya se ingresó anteriormente. Ingrese otra posición\nPosición:",end=' ')
			val =int(input())

		config.PosValidas.append(val)


def ConfiguraAccionImpala():
	print("\n****** Configuracion Impala ********\n")
	config.bolAccionesProgramadas = True
	bolConfigImpala = int(input())
	while bolConfigImpala <1 or bolConfigImpala > 2:
			print("Valor no valido, ingrese valor:",end= ' ')
			bolConfigImpala= int(input())
	"""
	Configuracion de acciones
	"""		
	if bolConfigImpala == 1:
		config.bolAccionesProgramadas = True
		print("\nLas acciones posibles son: \n1.-Mirar iquierda\n2.-Mirar derecha\n3.-Mirar frente\n4.-Beber agua")
		print("\nIngrese el numero de acciones que tendrá el ciclo:",end = ' ')
		cantidadAcciones = int(input())
		while cantidadAcciones<1:
			print("Debe haber al menos una accion en el ciclo, Cantidad:",end=' ')
			cantidadAcciones = int(input())
		print('\n')
		for i in range(cantidadAcciones):
			print(f"Ingrese la accion {i+1}:",end=' ')
			aci = int(input())
			while aci <1 or aci > 4:
				print("Valor no valido, ingrese valor:",end= ' ')
				aci= int(input())
			config.acciones.append(aci)

def SimulacionPasoAPaso():
	Limpia_Pantalla()

	print("\t********* SIMULACION PASO A PASO **********\n")
	print("¿Como desea hacer la simulacion?\n1.-Ingresar una solucion manualmente\n2.-Cargar una solucion\n3.-Menu Principal\nOpcion:",end=' ')
	opcion = ValidaEntrada()
	while opcion == str('Inf') or opcion < 1 or opcion > 3:
		opcion = ValidaEntrada()

	#Simulacion con ingreso manual de datos

	if opcion == 1:
		print("\nLos datos deben ser presentados de la siguente forma:\n\n-Posicion inicial del leon valores entre[1,8] basado en el dibujo del pdf\n-Reaccion que tendra el leon ante las acciones del impala donde\n 1.-Avanzar 2.-Esconderse\n-Distancia minima de cuadros para que el leon inicie el ataque")
		print("\nIngrese la posicion de inicio del leon:",end = ' ')
		inicio = int(input())
		while inicio <1 or inicio > 8:
			print("Posicion inicial no valida, Ingrese posicion inicial:",end= ' ')
			inicio	= int(input())

		print("\nReaccion del leon cuando el impala ve a la izquierda\nReaccion:",end=' ')
		reac_izq = int(input())
		while reac_izq <1 or reac_izq > 2:
			print("Valor no valida, ingrese valor:",end= ' ')
			reac_izq	= int(input())

		print("\nReaccion del leon cuando el impala ve a la derecha\nReaccion:",end=' ')
		reac_der = int(input())
		while reac_der <1 or reac_der > 2:
			print("Valor no valido, ingrese valor:",end= ' ')
			reac_der= int(input())

		print("\nReaccion del leon cuando el impala ve al frente\nReaccion:",end=' ')
		reac_frente = int(input())
		while reac_frente <1 or reac_frente > 2:
			print("Valor no valido, ingrese valor:",end= ' ')
			reac_frente	= int(input())

		print("\nReaccion del leon cuando el impala bebe\nReaccion:",end=' ')
		reac_bebe = int(input())
		while reac_bebe <1 or reac_bebe > 2:
			print("Valor no valido, ingrese valor:",end= ' ')
			reac_bebe= int(input())

		print("\nDistancia necesaria entre leon e impala para iniciar ataque valores entre[0,9]\nDistancia:",end=' ')
		ataca = int(input())
		while ataca <0 or ataca > 9:
			print("Valor no valido, ingrese valor:",end= ' ')
			ataca= int(input())

	elif opcion == 2:
		print("\nLa solucion será cargada de la ultima simulacion por generacion corrida\n")
		numGen = CuentaGeneraciones()
		if numGen == -1:
			print("No hay datos de una sumulacion anterior\nCorra una simulacion por generacion para poder cargar datos\nPresione Enter para regresar al menu principal...")
			input()
			MenuPrincipal()
			return
		print("\n¿A que generacion pertenece la solucion?:",end=' ')
		gener = int(input())
		while gener < 1 or gener > numGen-1:
			print("No existe esa genereracion. Opcion:",end=' ')
			gener=int(input())

		print("¿Que numero de individuo de la generacion es?:",end=' ')
		indinum = int(input())
		while indinum < 0 or indinum > 9:
			print("No existe ese individuo. Opcion:",end=' ')
			indinum=int(input())
		solSelect = BuscaSolucion(gener,indinum)
		inicio = solSelect.pos_inicial
		reac_izq = solSelect.react_izquierda
		reac_der = solSelect.react_derecha
		reac_frente = solSelect.react_frente
		reac_bebe = solSelect.react_bebe
		ataca = solSelect.atacar
		solSelect = None
	else:
		MenuPrincipal()
		return
	solu = AlgoritmoGenetico.Solucion(inicio,reac_izq,reac_der,reac_frente,reac_bebe,ataca)

	"""
	------------------------------------------------------------------------------
	Configuracion de acciones del impala para simulacion paso a paso
	............................................................................--
	"""
	print("\nDesea configurar un ciclo de acciones al impala?\n1.-Si\n2.-No, que sea aleatorio\nOpcion:",end=' ')
	bolConfigImpala = int(input())
	while bolConfigImpala <1 or bolConfigImpala > 2:
			print("Valor no valido, ingrese valor:",end= ' ')
			bolConfigImpala= int(input())
	"""
	Configuracion de acciones
	"""		
	if bolConfigImpala == 1:
		config.bolAccionesProgramadas = True
		print("\nLas acciones posibles son: \n1.-Mirar derecha\n2.-Mirar izquierda\n3.-Mirar frente\n4.-Beber agua")
		print("\nIngrese el numero de acciones que tendrá el ciclo:",end = ' ')
		cantidadAcciones = int(input())
		while cantidadAcciones<1:
			print("Debe haber al menos una accion en el ciclo, Cantidad:",end=' ')
			cantidadAcciones = int(input())
		print('\n')
		for i in range(cantidadAcciones):
			print(f"Ingrese la accion {i+1}:",end=' ')
			aci = int(input())
			while aci <1 or aci > 4:
				print("Valor no valido, ingrese valor:",end= ' ')
				aci= int(input())
			config.acciones.append(aci)

	print("\nDesea pausar la simulacion en cada tiempo?\n1.-Si\n2.-No\nOpcion:",end=' ')
	pasoApaso = int(input())
	while  pasoApaso !=1 and pasoApaso!= 2:
		print("Opción no válida. Opción:",end=' ')
		pasoApaso = int(input())
	print('\nA continuacion se presentará la simulacion con la configuracion antes hecha\nSe abrirá una ventana grafica para ver la simulación.\nSe recomienda ajustar el tamaño de esta ventana y la ventana emergente para que ambas\nsean visibles simultaneamente\nprecione Enter para comenzar...')
	input()
	print("\n\n****************** INICIA SIMULACION ************************\n")
	if pasoApaso ==1:
		AlgoritmoGenetico.CorreSimulacionXSolucion(config,solu,pasoApaso=True)
	else:
		AlgoritmoGenetico.CorreSimulacionXSolucion(config,solu,pasoApaso=False)
	MenuSecundario()

def MenuConfiguracion():
	print("\n¿Que deseas configurar?\n1.-Posiciones validas para el leon\n2.-Programar ciclo de acciones del impala\nOpcion:",end=' ')
	opcion = int(input())
	while opcion < 0 or opcion >2:
		print("Opcion no valida. Opcion:",end=' ')
		opcion = int(input())

	return opcion

def SimulacionPorGeneracion():
	Limpia_Pantalla()
	print("********** SIMULACION DE ALGORITMO GENETICO **********\n")
	print("Ingrese la cantidad máxima de generaciones a crear:\nMaximo:",end=' ')
	maxi = int(input())
	while maxi < 1:
		print("Debe de generarse al menos una generacion\nMaximo:",end=' ')
		maxi=int(input())
	config.intNumGeneraciones = maxi

	print("\nDesea hacer alguna configuracion para la simulacion?\n1.-Si\n2.-No, que sea todo aleatorio\n3.-Regresar al menu principal\nOpcion:",end=' ')

	ifconfig = int(input())
	while ifconfig < 1 or ifconfig >3:
		print("Opcion no valida\nOpcion:",end=' ')
		ifconfig =int(input())

	if ifconfig == 1:
		opcion = MenuConfiguracion()

		if opcion == 1:
			ConfiguraPosicionLeon()
			print("\nDeseas configurar el ciclo de acciones del impala?\n1.-Si\n2.-No, que todo sea aleatorio\nOpcion:",end= ' ')
			tmb = int(input())
			while tmb <1 or tmb>2:
				print("Ingrese una opcion valida. Opcion:",end=' ')
				tmb = int(input())
			if tmb == 1:
				ConfiguraAccionImpala()

		else:
			ConfiguraAccionImpala()
			print("\nDeseas configurar las posiciones de inicio del leon?\n1.-Si\n2.-No, que todo sea aleatorio\nOpcion:",end= ' ')
			tmb = int(input())
			while tmb <1 or tmb>2:
				print("Ingrese una opcion valida. Opcion:",end=' ')
				tmb = int(input())
			if tmb == 1:
				ConfiguraPosicionLeon()
		
	elif ifconfig == 3:
		MenuPrincipal()
		return
	
	print("\n\nA continuacio Se muestra la informacion por cada individuo de cada generacion de la siguente manera:\n\n-Posicion Inicial del leon\n-Reacciones del leon cuando el impala voltea a un lado con valores:\n  1.-Leon avanza ; 2.-Leon se esconde\n-La cantidad de cuadros de distancia entre leon y presa para empezar el ataque\n-Fitness representa cuantos cuadros de distancia minimos hubo\n entre el leon y el impala durante la simulacion de la solucion\n\nPresione Enter para comenzar...")
	input()
	print("\n\n****************** INICIA SIMULACION ************************\n")
	AlgoritmoGenetico.ConvergenciaXGeneracion(restringido = config.boolPosicionesValidas, posicones = config.PosValidas)

	##Antes del menu segundario debe estar la opcion de guardar y ver simulacion AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
	print("\n¿Que desea hacer ahora?\n1.-Regresar al menu principal\n2.-Correr una solucion particular\n3.-Guardar simulacion\n4.-Salir\nOpcion:",end=' ')
	opcion = int(input())
	while opcion <1 or opcion >4:
		print("Opcion no valida. Opcion:",end=' ')
		opcion= int(input())

	if opcion == 1:
		MenuPrincipal()
		#Guardar simulacion
	elif opcion == 2:
		numGen = CuentaGeneraciones()
		print("\n¿A que generacion pertenece la solucion?:",end=' ')
		gener = int(input())
		while gener < 1 or gener > numGen-1:
			print("No existe esa genereracion. Opcion:",end=' ')
			gener=int(input())

		print("¿Que numero de individuo de la generacion es?:",end=' ')
		indinum = int(input())
		while indinum < 0 and indinum > 9:
			print("No existe ese individuo. Opcion:",end=' ')
			indinum=int(input())
		solu = BuscaSolucion(gener,indinum)
		print("\nDesea pausar la simulacion en cada tiempo?\n1.-Si\n2.-No\nOpcion:",end=' ')
		pasoApaso = int(input())
		while  pasoApaso !=1 and pasoApaso!= 2:
			print("Opción no válida. Opción:",end=' ')
			pasoApaso = int(input())
		print('\nA continuacion se presentará la simulacion con la configuracion antes hecha\nSe abrirá una ventana grafica para ver la simulación.\nSe recomienda ajustar el tamaño de esta ventana y la ventana emergente para que ambas\nsean visibles simultaneamente\nprecione Enter para comenzar...')
		input()
		print("\n\n****************** INICIA SIMULACION ************************\n")
		if pasoApaso ==1:
			AlgoritmoGenetico.CorreSimulacionXSolucion(config,solu,pasoApaso=True)
		else:
			AlgoritmoGenetico.CorreSimulacionXSolucion(config,solu,pasoApaso=False)
		MenuSecundario()
		return

	elif opcion == 3:
		#Conseguimos la direccion del archivo
		pathname = os.path.abspath("Interfaz Usuario.py") 
		pathname = pathname[0:len(pathname)-19] 
		print("\nIngrese el nombre del archivo: ",end=' ')
		nombre = input()
		f = open("./ConocimientoLeon/UltimaSimulacion.txt","r")
		i = 0
		f2 = open(pathname+"/ConocimientoLeon/"+nombre+".txt","w")
		chunk = f.read(74)
		while chunk != '':
			f2.write(f"Generacion {i}:\n\n")
			for k in range(9):
				f2.write(chunk)
				chunk = f.read(74)
			i+=1
			f2.write('\n')
			chunk = f.read(74)
		f2.close()
		f.close()
		os.startfile(pathname+"\\ConocimientoLeon\\"+ nombre +".txt")
		print("\nEl archivo se guardo en:\n"+pathname +'ConocimientoLeon\n')
		print("\nQue desea hacer ahora?\n1.-Correr simulacion de una solucion\n2.-Salir\nOpcion:",end=' ')
		ultimaaccion = int(input())
		while ultimaaccion !=1 and ultimaaccion != 2:
			print("Opcion no valida. Opcion:",end=' ')
			ultimaaccion=int(input())

		if ultimaaccion ==1:
			numGen = CuentaGeneraciones()
			print("\n¿A que generacion pertenece la solucion?:",end=' ')
			gener = int(input())
			while gener < 1 or gener > numGen-1:
				print("No existe esa genereracion. Opcion:",end=' ')
				gener=int(input())

			print("¿Que numero de individuo de la generacion es?:",end=' ')
			indinum = int(input())
			while indinum < 0 or indinum > 9:
				print("No existe ese individuo. Opcion:",end=' ')
				indinum=int(input())
			solu  = BuscaSolucion(gener,indinum)
			print("\nDesea pausar la simulacion en cada tiempo?\n1.-Si\n2.-No\nOpcion:",end=' ')
			pasoApaso = int(input())
			while  pasoApaso !=1 and pasoApaso!= 2:
				print("Opción no válida. Opción:",end=' ')
				pasoApaso = int(input())
			print('\nA continuacion se presentará la simulacion con la configuracion antes hecha\nSe abrirá una ventana grafica para ver la simulación.\nSe recomienda ajustar el tamaño de esta ventana y la ventana emergente para que ambas\nsean visibles simultaneamente\nprecione Enter para comenzar...')
			input()
			print("\n\n****************** INICIA SIMULACION ************************\n")
			if pasoApaso ==1:
				AlgoritmoGenetico.CorreSimulacionXSolucion(config,solu,pasoApaso=True)
			else:
				AlgoritmoGenetico.CorreSimulacionXSolucion(config,solu,pasoApaso=False)

			MenuSecundario()
			return
		else:
			return
	else:
		return



def MenuPrincipal():
	Limpia_Pantalla()
	config.Reset()
	print("*NOTA: por favor todos los valores que sean ingresados sean numeros enteros validos para asegurar el buen \nfuncionamiento del programa :)\n")
	print('\n\t********** CACERÍA DEL LEÓN Y EL IMPALA **********\n\n')
	print("La simulación se hace a través de algoritmos genéticos\n")
	print("Tipo de simulación\n1.-Paso a Paso\n2.-Por generaciones\n3.-Salir\nOpción:",end = ' ')

	opcion = ValidaEntrada()
	while opcion == str('Inf') or opcion < 1 or opcion > 3:
		opcion = ValidaEntrada()

	#Paso a paso
	if opcion == 1:
		SimulacionPasoAPaso()
	elif opcion == 2:
		SimulacionPorGeneracion()
	else:
		return
	

MenuPrincipal()