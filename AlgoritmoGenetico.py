import random
import turtle
from enum import IntEnum
import time

#Generamos la semilla para la generacion de numeros aleatorio
random.seed()

"""
Posibles acciones que hace el impala
"""
class Accion(IntEnum):
	#Ver a algun lado:
	Izquierda = 1
	Derecha = 2
	Frente = 3
	Beber = 4
	Huir = 5

"""
Posibles acciones del leon
"""
class Reaccion(IntEnum):
	Avanzar = 1
	Esconder = 2
	Atacar = 3


"""
Cada individuo de nuestras poblaciones será una instancia de esta clase
La clase tiene como elementos:
	-La posicion en la que iniciaría la caceria el leon
		Valor numérico entre 1 y 8
	-Las reacciones del leon ante cada posible accion del impala (ver derecha, ver izquierda,etc) a excepcion de huir pues siempre que huye el leon ataca
	 	Valor numérico entre 1 y 2 (Enum Reaccion) pues atacar depende de la distancia a la que esté la presa
	-Distancia optima para iniciar el ataque 
		Valor numerico entre 0 y 8
"""
class Solucion:
	def __init__(self,start,izq,der,frente,bebe,atacar):

		#Posicion en la que iniciará el leon de las 8 posibles
		self.pos_inicial = start
		self.react_izquierda = izq
		self.react_derecha = der
		self.react_frente = frente
		self.react_bebe = bebe
		self.atacar = atacar #Numero de cuadros de distancia necesarios para iniciar el ataque
		self. fitness = float("Inf") #Inicializamos el fitnes de la clase con infinito
		self.P = 0 # probabilidad de ser padre

class Leon:
	def __init__(self,inicio):
		self.pos_inicial = inicio

		#Se inicializa la posicion inicial del leon la cuadricula se considera en base 1 y es de 19x19
		if inicio == 1:
			self.posicion = [1,10]
		elif inicio == 2:
			self.posicion = [1,19]
		elif inicio == 3:
			self.posicion = [10,19]
		elif inicio == 4:
			self.posicion = [19,19]
		elif inicio == 5:
			self.posicion = [19,10]
		elif inicio == 6:
			self.posicion = [19,1]
		elif inicio == 7:
			self.posicion = [10,1]
		elif inicio == 8:
			self.posicion = [1,1]

		self.atacando = False
		self.oculto = False 
		if inicio == 3 or inicio == 7:
			self.ecuador = True
		else:
			self.ecuador = False

	"""
	Debe tomar en cuenta la direccion y posicion del leon 
	EN DESARROLLO
	"""
	#Funcion que solo se llama desde la simulacion
	#DEBE CONSIDERAR LA DIRECCION Y POSICION DE LEON EN DESARROLLO
	def Atacar(self):

		##El impala corre al oeste si el leon viene de 1 2 3 o 4
		if self.pos_inicial == 1:
			if self.ecuador == False:
				#Se pasa del centro
				if self.posicion[0]+2 > 10:
					dif = abs(self.posicion[0]+2 - 10) 
					self.posicion[0]= 10
					self.posicion[1] -= dif 
					#Marcamos que ya paso por el centro del mapa
					self.ecuador = True
				else:
					self.posicion[0]+=2
			else:
				self.posicion[1]-=2

		elif self.pos_inicial == 2:
			if self.ecuador == False:
				if self.posicion[1]-2 < 10:
					dif = abs(self.posicion[1]-2-10)
					self.posicion = [10,10]
					self.posicion[1]-= dif
					self.ecuador = True
				else:
					self.posicion[0]+=2
					self.posicion[1]-=2
			else:
				self.posicion[1]-=2

		elif self.pos_inicial == 3:
			self.posicion[1]-=2

		elif self.pos_inicial == 4:
			if self.ecuador == False:
				#print("Esta avanzando")
				if self.posicion[0]-2 < 10:
					dif = abs(self.posicion[0]-2-10)
					self.posicion = [10,10]
					self.posicion[1]-=dif
					self.ecuador = True
				else:
					self.posicion[0]-=2
					self.posicion[1]-=2
			else:
				self.posicion[1]-=2

		elif self.pos_inicial == 5:
			if self.ecuador == False:
				if self.posicion[0]-2 < 10:
					dif = abs(self.posicion[0]-2 -10)
					self.posicion=[10,10]
					self.posicion[1]+=dif
					self.ecuador = True	
				else:
					self.posicion[0]-=2
			else:
				self.posicion[1]+=2

		elif self.pos_inicial == 6:
			if self.ecuador == False:
				if self.posicion[0]-2 < 10:
					dif  = abs(self.posicion[0]-2-10)
					self.posicion= [10,10]
					self.posicion[1]+=dif
					self.ecuador = True
				else:
					self.posicion[0]-=2
					self.posicion[1]+=2
			else:
				self.posicion[1]+=2

		elif self.pos_inicial == 7:
			self.posicion[1]+=2

		elif self.pos_inicial == 8:
			if self.ecuador == False:
				if self.posicion[0]+2 > 10:
					dif =abs(self.posicion[0]+2 - 10)
					self.posicion=[10,10]
					self.posicion[1] +=dif
					self.ecuador = True	
				else:
					self.posicion[0]+=2
					self.posicion[1]+=2
			else:
				self.posicion[1]+=2

	def Avanzar(self):
		self.oculto =False
		#CODIGO DE PRUEBA AHEAD
		if self.pos_inicial == 1:
			self.posicion[0]+=1

		elif self.pos_inicial == 2:
			self.posicion[0] +=1
			self.posicion[1] -=1

		elif self.pos_inicial == 3:
			self.posicion[1]-=1

		elif self.pos_inicial == 4:
			self.posicion[0]-=1
			self.posicion[1]-=1

		elif self.pos_inicial == 5:
			self.posicion[0]-=1

		elif self.pos_inicial == 6:
			self.posicion[0]-=1
			self.posicion[1]+=1

		elif self.pos_inicial == 7:
			self.posicion[1]+=1

		elif self.pos_inicial == 8:
			self.posicion[0]+=1
			self.posicion[1]+=1



	def Esconder(self):
		self.oculto = True

	#Busca la reaccion correspondiente a la accion y llama a la funcion para realizarlo
	def FindReaccion(self,accion):
		if accion==Reaccion.Avanzar:
			self.Avanzar()
			return'Avanzar'
		elif accion == Reaccion.Esconder:
			self.Esconder()
			return 'Esconder'
			

		#Se define la reaccion segun la accion que haga el impala
	def Reaccion(self,solucion,accion):
		if self.atacando == True:
			self.Atacar()
			#print('Leon inicia Ataque')
			return 'Atacar'
		elif accion == Accion.Izquierda:
			reac =self.FindReaccion(solucion.react_izquierda)
		elif accion == Accion.Derecha:
			 reac =self.FindReaccion(solucion.react_derecha)
		elif accion ==Accion.Frente:
			 reac =self.FindReaccion(solucion.react_frente)
		elif accion == Accion.Beber:
			reac =self.FindReaccion(solucion.react_bebe)
		
		return reac

			
"""
Objeto que representará al impala y las acciones que este realizara
"""
class Impala:

	def __init__(self):
		self.posicion=[10,10]
		self.huyendo = False
		self.direccion = None
		self.alcanzado = False
		self.escapo = False

	#Se seleccionará al azar una de las acciones que puede realizar, sin contar la accion de escapar que esa sera detonada externamente
	#en la simulacion
	def SetAccion(self):
		return random.randint(1,4)

	def SetAccionProgramada(self,t,longitud):
		#Calculamos la accion que le correspode ejecutarse
		t = t%longitud
		return self.acciones_programadas[t]

	# la variable t representa la cantidad de tiempo que ha estado el impala en huida
	def Huir(self,t):
		if self.direccion =="Este":
			self.posicion[1] += t
		else:
			self.posicion[1] -= t


"""
Clase para setear la configuracion inicial de las simulaciones
"""
class ConfiguracionInicial:
	def __init__(self,tipo = 1,prog_acciones=False,prog_posiciones =False,numgeneraciones = 10):
		self.tipo_simulacion =tipo
		self.bolAccionesProgramadas = prog_acciones
		self.boolPosicionesValidas = prog_posiciones
		self.intNumGeneraciones = numgeneraciones
		self.acciones = []
		self.PosValidas = []

	def Reset(self):
		self.tipo_simulacion = 1
		self.bolAccionesProgramadas = False
		self.boolPosicionesValidas = False
		self.intNumGeneraciones = 10
		self.acciones = []
		self.PosValidas = []

def IndividuoValido(individuo):
	#Evitamos bucles infinitos en la funcion objetivo
	if individuo.react_izquierda == Reaccion.Esconder and individuo.react_derecha == Reaccion.Esconder and individuo.react_frente == Reaccion.Esconder and individuo.react_bebe == Reaccion.Esconder:
		#print("Elemenmto con ciclo infinito")
		cambio =random.randint(1,4)
		if cambio == 1:
			individuo.react_izquierda = Reaccion.Avanzar
		elif cambio == 2:
			individuo.react_derecha = Reaccion.Avanzar
		elif cambio == 3:
			individuo.react_frente = Reaccion.Avanzar
		else:
			individuo.react_bebe = Reaccion.Avanzar
	return individuo
"""
Generamos una poblacion inicial de soluciones aleatoriamente
Parametros: None
Returns: list<Soluciones>
Genera una lista de soluciones y returna un list donde cada elemento es una instancia de la clase soluciones
"""
def GeneraPoblacionInicial(restringido = False,posicones = None):
	poblacion0 = []
	for i in range(10): #poblaciones de 10 individuos????
		#Iniciamos al azar las posibles reacciones y valor de ataque
		pos_inicial = random.randint(1,8)
		if restringido == True:
			while pos_inicial not in posicones:
				pos_inicial = random.randint(1,8)
		react_izquierda = random.randint(1,2)
		react_derecha = random.randint(1,2)
		react_frente = random.randint(1,2)
		react_bebe = random.randint(1,2)
		atacar = random.randint(0,8)
		individuo = Solucion(pos_inicial, react_izquierda, react_derecha, react_frente, react_bebe, atacar)


		poblacion0.append(IndividuoValido(individuo))
	return poblacion0.copy()

"""
La seleccion de individuos que serán padres esta dada por el rango del idividuo donde su probabilidad de ser seleccionado es
P=FunObj(individuo)/[len(poblacion)*len(poblacion+1)/2]
esto para evitar la convergencia prematura por superindividuos al normalizar la probabilidad de ser padre
con probabilidad de ser padre >=.4
Primero se ordenan los elementos de acuerdo a su fitnes de menor (mejor) a mayor (peor) y se retornan los 4 primeros elementos
"""
def Seleccion(poblacion):
	mejores = []
	mejores.append(poblacion[0])
	for i in range(1,len(poblacion)):
		#Encontramos su lugar en el arreglo ordenado (Insertion Sort)
		index = 0

		while index < len(mejores) and poblacion[i].fitness > mejores[index].fitness:
			index+=1

		#Insertamos el individuo en la posicion que le corresponde
		if index == len(mejores):
			mejores.append(poblacion[i])
		else:
			mejores.insert(index,poblacion[i])

	#Se calcula la probabilidad de ser padre de los individuos

	#rango = len(mejores)
	#for i in range(rango):
	#	mejores[i].P = (rango-i)/(rang*(rango+1)/2)
	return mejores[0:4].copy()	

def Mutacion(poblacion,restringido = False,posicones = None):
	probabilidad = 0.1
	for i in range(len(poblacion)):
		prov = random.uniform(0,1)
		if prov <= probabilidad:
			changeIndex = random.randint(1,6)	

			if changeIndex ==1:
				poblacion[i].pos_inicial = random.randint(1,8)
				if restringido == True:
					while poblacion[i].pos_inicial not in posicones:
						poblacion[i].pos_inicial = random.randint(1,8)
			elif changeIndex == 2:
				if poblacion[i].react_izquierda == Reaccion.Avanzar:
					poblacion[i].react_izquierda = Reaccion.Esconder
				else:
					poblacion[i].react_izquierda = Reaccion.Avanzar
			elif changeIndex == 3:
				if poblacion[i].react_derecha == Reaccion.Avanzar:
					poblacion[i].react_derecha = Reaccion.Esconder
				else:
					poblacion[i].react_derecha = Reaccion.Avanzar
			elif changeIndex == 4:
				if poblacion[i].react_frente == Reaccion.Avanzar:
					poblacion[i].react_frente =  Reaccion.Esconder
				else:
					poblacion[i].react_frente = Reaccion.Avanzar
			elif changeIndex == 5:
				if poblacion[i].react_bebe == Reaccion.Avanzar:
					poblacion[i].react_bebe = Reaccion.Esconder
				else:
					poblacion[i].react_bebe = Reaccion.Avanzar
			else:
				if poblacion[i].atacar >8 :
					poblacion[i].atacar-=1
				elif poblacion[i].atacar <=0:
					poblacion[i].atacar+=1
				else:
					if random.randint(0,1) == 1:
						poblacion[i].atacar+=1
					else:
						poblacion[i].atacar-=1
			poblacion[i] = IndividuoValido(poblacion[i])
	return poblacion					

## Los atributos no se metieron en un arreglo(Que haria mas facil la codificacion) para aumentar la claridad del codigo
def GeneraHijo(padre,madre,cruce):
	if cruce == 1:
		hijo = Solucion(padre.pos_inicial, madre.react_izquierda, madre.react_derecha, madre.react_frente, madre.react_bebe, madre.atacar)
	elif cruce == 2:
		hijo = Solucion(padre.pos_inicial, padre.react_izquierda, madre.react_derecha, madre.react_frente, madre.react_bebe, madre.atacar)
	elif cruce == 3:
		hijo = Solucion(padre.pos_inicial, padre.react_izquierda, padre.react_derecha, madre.react_frente, madre.react_bebe, madre.atacar)
	elif cruce == 4:
		hijo = Solucion(padre.pos_inicial, padre.react_izquierda, padre.react_derecha, padre.react_frente, madre.react_bebe, madre.atacar)
	elif cruce == 5:
		hijo = Solucion(padre.pos_inicial, padre.react_izquierda, padre.react_derecha, padre.react_frente, padre.react_bebe, madre.atacar)

	return IndividuoValido(hijo)

def Cruza(padres):
	nueva_Generacio = [] 
	for i in range(len(padres)-1):
		for j in range(i+1,len(padres)):
			puntoCruce = random.randint(1,5) #despues de la propiedad n se hace el cruce
			#Se generan los dos hijos a partir del punto de cruce de los padres
			nueva_Generacio.append(GeneraHijo(padres[i],padres[j],puntoCruce))
			nueva_Generacio.append(GeneraHijo(padres[j],padres[i],puntoCruce))
	if len(nueva_Generacio)> 10:
		return nueva_Generacio[0:10].copy()
	else:
		return nueva_Generacio.copy()


def CalculaDistancia(leon,impala):
	distancia  = 0
	#Calculamos la distancia entre el leon y el lugar en que inicia el impala
	if impala.huyendo ==False or leon.ecuador == False:
    	#El leon esta en el este o el oeste la distancia se calcula con el valor y de su posicion. en otro caso se calcula con el valor x
		if leon.pos_inicial == 3 or leon.pos_inicial == 7:
			distancia = abs(leon.posicion[1]-10)
		else:
			distancia  = abs(leon.posicion[0]-10)
		

		if impala.huyendo == True:
			distancia += abs(impala.posicion[1]-10)
			#print("Se suma la distancia del impala al origen")

	else:
		distancia = abs(leon.posicion[1]-impala.posicion[1])
	
	return distancia

#Retorna la direccion en la que huirá el impala
def SetDireccionHuida(pos_inicial):
	if pos_inicial == 5 or pos_inicial == 6 or pos_inicial == 7 or pos_inicial ==8:
		return "Este"
	else:
		return "Oeste"

def FunVisualBORRAR(accion):
	if accion == Accion.Izquierda:
		return 'Izquierda'
	elif accion == Accion.Derecha:
		return'Derecha'
	elif accion ==Accion.Frente:
		return 'Frente'
	elif accion == Accion.Beber:
		return'Beber'

"""
Nuestra fucion objetivo correra la solucion i en una simulacion de la caceria para descubrir el minimo de cuadros 
que hubo entre el impala y el leon con los parametros de la solucion i
"""
def FuncionObjetivo(solucion,visualizar,progImpala =False,longitud=None,acciones =None,pasoApaso=False):
	#Creaomos a nuestras criaturas
	find_loop = 0
	leon = Leon(solucion.pos_inicial)
	if visualizar == True:
		print(f'LeonPosInicial: ({leon.posicion[0]},{leon.posicion[1]})')

	impala = Impala()
	if acciones !=None:
		impala.acciones_programadas = acciones
	t = 0 #tiempo de accion
	t_huida = 0
	def abrevadero():
			t3.color("aqua")
			t3.penup()
			t3.goto(-70,10)
			t3.pendown()
			t3.begin_fill()
			t3.goto(70,10)
			t3.goto(70,70)
			t3.goto(-70,70)
			t3.end_fill()
			t3.color("white")

	def limpia():
		t3.goto(-301,285)
		t3.color("white")
		t3.begin_fill()
		t3.goto(-301,245)
		t3.goto(-191,245)
		t3.goto(-191,195)
		t3.goto(10,195)
		t3.goto(10,285)
		t3.goto(-301,285)
		t3.end_fill()
		t3.color("black")
		

	def cuadricula():
		t3.color("black")
		t3.penup()
		t3.goto(-190,190)
		t3.setheading(0)
		t3.pd()
		t3.goto(190,190)
		t3.goto(190,170)
		t3.setheading(180)
		for i in range(9):
			t3.forward(380)
			t3.left(90)
			t3.backward(20)
			t3.forward(40)
			t3.left(90)
			t3.forward(380)
			t3.right(90)
			t3.backward(20)
			t3.forward(40)
			t3.right(90)
		t3.forward(380)
		t3.left(90)
		t3.backward(20)
		t3.pu()
		t3.goto(-170,190)
		t3.pd()
		t3.setheading(270)
		for i in range(9):
			t3.forward(380)
			t3.left(90)
			t3.forward(20)
			t3.left(90)
			t3.forward(380)
			t3.right(90)
			t3.forward(20)
			t3.right(90)
		t3.pu()
		t3.goto(220,260)
		t3.write("León:", font=("Arial",12,"normal"))
		t1.goto(220,240)
		#t3.goto(240,230)
		t3.goto(245,230)
		t3.write("Visible", font=("Arial",12,"normal"))
		t1.shape("./Imagenes/lion.gif")
		t1.stamp()
		#t1.goto(220,220)
		t1.goto(220, 190)
		t1.color("green")
		t1.shape("./Imagenes/lion_escondido.gif")
		t1.stamp()
		#t3.goto(240,210)
		t3.goto(240,190)
		t3.write("Escondido", font=("Arial",12,"normal"))
		#t3.goto(220,180)
		t3.goto(220, 140)
		t3.write("Impala:", font=("Arial",12,"normal"))
		#t2.goto(220,160)
		t2.goto(220, 120)
		t2.stamp()
		#t2.goto(220,140)
		t2.goto(220,80)
		t2.color("blue")
		t2.shape("./Imagenes/impala_bebiendo.gif")
		t2.stamp()
		t2.shape("./Imagenes/impala.gif")
		t2.goto(0,0)
		t3.goto(245,115)
		t3.write("Normal", font=("Arial",12,"normal"))
		t3.goto(245,75)
		t3.write("Bebiendo", font=("Arial",12,"normal"))
		t3.goto(245, 35)
		t3.write("Vista", font=("Arial",12,"normal"))
		t3.goto(220, 35)
		t3.shape("./Imagenes/direccion.gif")
		t3.stamp()
		t3.penup()

		t3.goto(-320,260)
		t3.write("T:", font=("Arial",12,"normal"))
		
		t3.goto(-320,220)
		t3.write("Acción Impala:", font=("Arial",12,"normal"))
		
		t3.goto(-320,200)
		t3.write("Reacción León:", font=("Arial",12,"normal"))
		

#----------------Creacion de criaturas y pantalla en Turtle--------------------------------------------------------------------------------------
	if visualizar == True:
		can = turtle.Screen()
		can.bgpic("./Imagenes/pasto_agua.gif")
		#can.bgcolor("")
		can.screensize(1000,400)

		turtle.register_shape("./Imagenes/lion.gif")
		turtle.register_shape("./Imagenes/lion_escondido.gif")
		turtle.register_shape("./Imagenes/impala.gif")
		turtle.register_shape("./Imagenes/impala_der.gif")
		turtle.register_shape("./Imagenes/impala_izq.gif")
		turtle.register_shape("./Imagenes/impala_bebiendo.gif")
		turtle.register_shape("./Imagenes/impala_frente.gif")
		turtle.register_shape("./Imagenes/direccion.gif")

		t1 = turtle.Turtle() #Leon
		t2 = turtle.Turtle() #Impala
		t3 = turtle.Turtle() #Abrevadero
		t3.ht()
		t1.shape("./Imagenes/lion.gif")
		t1.color("red")
		t1.penup()
		t2.shape("./Imagenes/impala.gif")
		t2.color("green")
		t2.penup()
		t3.speed(0)
		cuadricula()
#-------------------------------------------------------------------------------------------------------------------------------------

	#Corre la simulacion de la caceria
	while impala.alcanzado == False and impala.escapo == False:
		if visualizar == True:
			print(f"\nTiempo {t}\n")
			t3.color("black")
			t3.goto(-300,260)
			t3.write(str(t), font=("Arial",12,"normal"))

		if impala.huyendo == False:
			#Cada criatura hace su accion
			if progImpala == True:
				accion=impala.SetAccionProgramada(t,longitud)
			else:
				accion = impala.SetAccion()

			reaccion = leon.Reaccion(solucion,accion)
			if visualizar == True:
				impAction = FunVisualBORRAR(accion)
				print(f'Accion Impala: {impAction}')
				print(f'Reaccion Leon: {reaccion}')

			if reaccion == 'Atacar':
				impala.huyendo = True
			#Calculamos el fitness del tiempo t
			fitness = CalculaDistancia(leon,impala)

			if visualizar == True:
				print(f'fitness en tiempo {t}:{fitness}')

			if solucion.fitness > fitness:
				solucion.fitness = fitness
			
			#Evaluamos el estado de el tiempo t
			#Evaluamos si es necesario empezar el ataque o la huida
			if fitness == solucion.atacar:
				leon.atacando  =True				
				impala.direccion=SetDireccionHuida(leon.pos_inicial)
				if visualizar == True:
					t3.goto(0,-240)
					t3.write(f"León inicia ataque en tiempo {t+1}", font=("Arial",12,"normal"),align='center')
				
			if fitness < 3 and leon.atacando == False:
				impala.huyendo = True
				leon.atacando = True
				if visualizar == True:
					print("El leon esta muy cerca, impala huye!!")
					t3.goto(0,-220)
					t3.write("El leon esta muy cerca, impala huye!!", font=("Arial",12,"normal"),align='center')


				impala.direccion=SetDireccionHuida(leon.pos_inicial)
			#Evaluamos si el impala puede ver al leon
			else:

				#El impala voltea a la izquierda y ve al leon
				if accion == Accion.Izquierda and (leon.pos_inicial == 6 or leon.pos_inicial == 7 or leon.pos_inicial == 8) and leon.oculto == False:
					impala.huyendo = True
					leon.atacando = True

					if visualizar == True:
						print("Impala ve al leon, inicia huida!!!")
						t3.goto(0,-220)
						t3.write("Impala ve al leon, inicia huida!!!", font=("Arial",12,"normal"),align='center')

				#El impala voltea a la derecha y ve al leon
				elif accion == Accion.Derecha and (leon.pos_inicial == 2 or leon.pos_inicial == 3 or leon.pos_inicial == 4) and leon.oculto == False:
					impala.huyendo = True
					leon.atacando = True

					if visualizar == True:
						print("Impala ve al leon, inicia huida!!!")
						t3.goto(0,-220)
						t3.write("Impala ve al leon, inicia huida!!!", font=("Arial",12,"normal"),align='center')

				#El impala voltea al frente y ve al leon
				elif accion == Accion.Frente and (leon.pos_inicial == 1 or leon.pos_inicial == 2 or leon.pos_inicial == 8) and leon.oculto == False:
					impala.huyendo = True
					leon.atacando = True
					
					if visualizar == True:
						print("Impala ve al leon, inicia huida!!!")
						t3.goto(0,-220)
						t3.write("Impala ve al leon, inicia huida!!!", font=("Arial",12,"normal"),align='center')

			if visualizar == True:
				t3.goto(-190,220)
				t3.write(impAction, font=("Arial",12,"normal"))
				t3.goto(-190,200)
				t3.write(reaccion, font=("Arial",12,"normal"))

			##El leon alcanzo al impala
			if leon.posicion == impala.posicion:
				solucion.fitness = 0
				impala.alcanzado = True
				if visualizar == True:
					print("El leon alcanzo al impala")
		else:
			impala.atacando = True
			leon.atacando = True
			t_huida+=1
			#Ambos estan en carrera
			impala.Huir(t_huida)
			leon.Atacar()
			if visualizar == True:
				print('Leon ataca')
				print(f'Imapla huye a {t_huida} cuadros/t')
				t3.goto(-190,220)
				t3.write(f'Imapla huye a {t_huida} cuadros/t', font=("Arial",12,"normal"))
				t3.goto(-190,200)
				t3.write(reaccion, font=("Arial",12,"normal"))

			#Actualizamos el fitness de la solucion de ser necesario
			fitness = CalculaDistancia(leon,impala)
			if visualizar == True:
				print(f'fitness en tiempo {t}:{fitness}')
			if solucion.fitness > fitness:
				solucion.fitness = fitness	

			##El leon alcanzo al impala
			if leon.posicion == impala.posicion:
				solucion.fitness = 0
				impala.alcanzado = True
				if visualizar == True:
					print("El leon alcanzo al impala")
					endmsg="El leon alcanzo al impala"
			#El impala escapo pues avanza mas rapido que el leon
			elif t_huida > 2:
				if visualizar == True:
					print("El impala logra escapar pues ya corre mas rapido que el leon")
					endmsg="Impala escapa, corre mas rapido que leon"
				impala.escapo = True

		if visualizar == True:
			print(f'PosLeon ({leon.posicion[0]},{leon.posicion[1]})')
			print(f'PosImpala ({impala.posicion[0]},{impala.posicion[1]})')
		#Pasamos al tiempo t+1
		t+=1
		if t>100:
			print("\nLa configuracion de acciones del impala creo un ciclo infinito, pues el leon nunca avanza\nSe termina la simulacion")
			return
#--------------------------------------------------------------------------------------------------------------------------------------------
		## Simulacion de la carrera en Turtle
#--------------------------------------------------------------------------------------------------------------------------------------------
		
			
		 #Comentar para ver sin abrevadero
		if visualizar == True:
			#Calculo de Posiciones:
			step = 20
			limite = step * 10

			#Accion del Impala ( es para que el Impala voltee la cabeza cuando no avanza )
			if(impala.huyendo == False):
				if(accion == Accion.Izquierda):
					t2.color("green")
					t2.setheading(180)
					t2.shape("./Imagenes/impala_izq.gif")
				elif(accion == Accion.Derecha):
					t2.color("green")
					t2.setheading(0)
					t2.shape("./Imagenes/impala_der.gif")
				elif(accion == Accion.Beber):
					t2.color("blue")
					t2.setheading(90)	
					t2.shape("./Imagenes/impala_bebiendo.gif")	
				elif(accion == Accion.Frente):
					t2.color("green")
					t2.setheading(90)	
					t2.shape("./Imagenes/impala_frente.gif")
			else:
				t2.color("green")
				t2.shape("./Imagenes/impala.gif")

			#Posicion del Impala
			for i in range(1,20):
				if(impala.posicion[0] == 10 and impala.posicion[1] == i):
					# Solo Coordenadas en x
					if (i > 10):
						t2.setheading(0)
						t2.shape("./Imagenes/impala_der.gif")
						t2.setx( 0 + ( (i-10) * step ))
					elif (i < 10):
						t2.setheading(180)
						t2.shape("./Imagenes/impala_izq.gif")
						t2.setx( -limite + ( i * step ))

			if reaccion =="Esconder":
				t1.shape("./Imagenes/lion_escondido.gif")
			else:
				t1.shape("./Imagenes/lion.gif")
			#Posicion del Leon
			for h in range(1,20):
				for l in range(1,20):
					if(leon.posicion[0] == h and leon.posicion[1] == l):
						# Coordenadas en x
						if ( l <= 10):
							t1.setx( -limite + (l*step))
						elif( l > 10):
							t1.setx(0 + ( (l-10) * step ))
						
						# Coordenadas en y
						if( h <= 10):
							t1.sety( limite - ( h * step) )
						elif (h > 10):
							t1.sety ( -1 * ( (h-10) * step ))


		

		#print('Coordenadas Leon: ', t1.pos())
		#print('Coordenadas Impala: ',t2.pos())

		#Controlar la velocidad de las pantallas de Turtle (escoger solo una)
		 #aumentar o decrementar el valor
		#input("Presione Enter para continuar...")

		#Pruebas click
		if visualizar == True:
			can.delay(100)
			if pasoApaso == True:
				print("Enter para pasar a la siguiente iteración...")
				input()
			if impala.alcanzado == False and impala.escapo == False:
				limpia()
	if visualizar == True:
		t3.color("black")
		t3.goto(0,240)
		t3.write(endmsg, font=("Arial",12,"normal"),align="center")
		time.sleep(5)
		can.bye()

"""
----------------------------------------------------------------------------------------------------------------------------------------
Codigo para Convergencia por generaciones
----------------------------------------------------------------------------------------------------------------------------------------
"""
def ConvergenciaXGeneracion(restringido = False,posicones = None):
	a = GeneraPoblacionInicial(restringido = restringido,posicones = posicones)

	#Archivo donde se guardara la ultima simulacion del algoritmo
	f = open("./ConocimientoLeon/UltimaSimulacion.txt","w")
	for j in range(10):
		total_fitness = 0
		print(f"\nGeneracion {j+1}:\n")

		## Iteracion del algoritmo genetico
		for i in range(len(a)):
			print(f'Solucion {i}: inicio:{a[i].pos_inicial}; izq:{a[i].react_izquierda}; der: {a[i].react_derecha}; frente:{a[i].react_frente}; bebe:{a[i].react_bebe}; ataca:{a[i].atacar};',end= ' ')
			f.write(f'Solucion {i}: inicio:{a[i].pos_inicial}; izq:{a[i].react_izquierda}; der: {a[i].react_derecha}; frente:{a[i].react_frente}; bebe:{a[i].react_bebe}; ataca:{a[i].atacar};')

			FuncionObjetivo(a[i],False)
			mini = a[i].fitness
			FuncionObjetivo(a[i],False)
			if mini > a[i].fitness:
				a[i].fitness = mini
			print(f'fitness:{a[i].fitness}')
			f.write(f' fitness:{a[i].fitness}')
			f.write('\n')
			total_fitness +=a[i].fitness

		#print("Acabo el primer ciclo")
		if total_fitness != 0:
			padres = Seleccion(a)
			a = Cruza(padres)
			a = Mutacion(a,restringido = restringido,posicones = posicones)
		else:
			print("\nLa generacion convergio con fitness 0")
			break

	f.close()

"""
---------------------------------------------------------------------------------------------------------------
Codigo parra mostrar el funcionamiento de la simulacion de una solucion
----------------------------------------------------------------------------------------------------------------
"""
def CorreSimulacionXSolucion(configuracion,sol,pasoApaso):
	print(f'Solucion: inicio:{sol.pos_inicial}; izq:{sol.react_izquierda}; der: {sol.react_derecha}; frente:{sol.react_frente}; bebe:{sol.react_bebe}; ataca:{sol.atacar}')
	if configuracion.bolAccionesProgramadas == True:
		FuncionObjetivo(sol,True,progImpala = True,longitud=len(configuracion.acciones),acciones = configuracion.acciones,pasoApaso=pasoApaso)
	else:
		FuncionObjetivo(sol,visualizar=True,pasoApaso=pasoApaso)

"""
-------------------------------------------------------------------------------------------------------------------------------------
Corre una de las funciones siguientes
--------------------------------------------------------------------------------------------------------------------------------------
"""
# Comenta la funcion que no quieres que se ejecute
sol = Solucion(5,1,1,1,1,3)
con = ConfiguracionInicial()
#CorreSimulacionXSolucion(con,sol)
#ConvergenciaXGeneracion()