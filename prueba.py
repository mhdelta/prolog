from pyDatalog import pyDatalog
import sys

pyDatalog.create_terms('X, verificar, yes, Daltonismo, no, ask, hipotesis, Enfermedad, Posible_enfermedad')

+yes('')
+no('')
+hipotesis('')

def verificar(S):
	if(yes(S)):
		return True
	else:
		if(no(S)):
			return False
		else:
			if(ask(S)):
				return True
			else:
				return False

def ask(pregunta):
	print "Padece del sintoma ", pregunta, "?"
	respuesta = raw_input()
	if ((respuesta == "yes") or (respuesta == 'y')):
		+yes(pregunta)
		return True 
	else:
		+no(pregunta)
		return False

def Diag():
	print "============================="
	print hipotesis(Posible_enfermedad)
	sys.exit("Programa terminado con exito")

if(verificar('Percepcion nula del color') or verificar('Percepcion parcial del color')):
	+hipotesis('Daltonismo')
	Diag()


if(verificar('Vision oscurecida o gris') and verificar('Dolor de cabeza')):
	+hipotesis('Glaucoma')
	Diag()

