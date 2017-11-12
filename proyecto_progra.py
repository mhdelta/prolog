#!/usr/bin/env python3
from pyDatalog import pyDatalog
import sys
import facts
#//=================================================================================================
                    # BASE DEL CONOCIMIENTO
pyDatalog.create_terms('Enfermedad, enfermedad, yes, dolor, herencia, afectacion, otros_sintomas, color, edad, patologia, ubicacion_orzuelo, pus')
pyDatalog.create_terms('X, Y')
pyDatalog.create_terms('ask, que_dolor, Attr, Val, preguntar, que_color')
pyDatalog.create_terms('yes, no, sintoma')
+yes('')
+no('')



enfermedad('astigmatismo') <= yes('Presenta dolores de cabeza') &\
                              yes('su vision es borrosa en general') &\
                              yes('Se le dificulta ver de noche') &\
                              yes('Presenta fatiga visual')                              

enfermedad('miopia') <= yes('Presenta dolores de cabeza') &\
                        yes('su vision es borrosa al ver objetos lejanos') &\
                              yes('Presenta fatiga visual') &\
                              yes('Tiene familiares que padezcan diabetes') &\
                              yes('Tiene familiares que padezcan miopia')

enfermedad('hipermetropia') <= yes('Es mayor de 30 anios') &\
                               yes('su vision es borrosa al ver objetos lejanos') &\
                               yes('su vision es borrosa al ver objetos cercanos')

enfermedad('hipermetropia') <= yes('Es menor de 30 anios') & \
                               yes('su vision es borrosa al ver objetos lejanos')

enfermedad ('conjuntivitis_infecciosa') <= yes('Presenta sensibilidad a la luz') & \
                                           yes('presenta ardor en la zona afectada') & \
                                           yes('Tiene los ojos rojos') & \
                                           yes('Presenta lagrimeo') & \
                                           yes('Tiene la sensacion de tener un objeto en el ojo')& \
                                           yes('De la zona afectada sale pus amarillo')

enfermedad ('conjuntivitis_infecciosa') <= yes('Presenta sensibilidad a la luz') & \
                                           yes('presenta ardor en la zona afectada') & \
                                           yes('Tiene los ojos rojos') & \
                                           yes('Presenta lagrimeo') & \
                                           yes('Tiene la sensacion de tener un objeto en el ojo')& \
                                           yes('De la zona afectada sale pus verde')

enfermedad('conjuntivitis_alergica') <= yes('Presenta sensibilidad a la luz') & \
                                        yes('presenta ardor en la zona afectada') & \
                                        yes('Tiene los ojos rojos')  & \
                                        yes('Tiene la sensacion de tener un objeto en el ojo') &\
                                        ~yes('De la zona afectada sale pus amarillo') &\
                                        ~yes('De la zona afectada sale pus verde') 


enfermedad ('cataratas') <= yes('su vision es borrosa en general') & \
                            yes('Se le dificulta ver de noche') &\
                            yes('ve doble') &\
                            yes('Es incapaz de diferenciar el rojo y el verde') & \
                            yes('ve los colores destenidos')

enfermedad('cataratas') <=    yes('Es mayor de 60 anios') &\
                            yes('Padece diabetes')

enfermedad('cataratas') <=  yes('Es mayor de 60 anios') &\
                            yes('ha tenido alguna herida en el ojo recientemente')

enfermedad('cataratas') <=  yes('Es mayor de 60 anios') &\
                            yes('Esta expuesto a radiacion constantemente')

enfermedad('cataratas') <=  yes('Es mayor de 60 anios') &\
                            yes('Esta expuesto a rayos ultravioletas constantemente')
                                                      
enfermedad ('orzuelo') <=  yes('protuberancia_roja') & \
                           yes('Presenta dolor en la zona afectada') &\
                           yes('La zona afectada esta hinchada') & \
                           yes('Tiene picazon en la zona afectada') &\
                           yes('Presenta lagrimeo') & \
                           yes('Tiene pus en la protuberancia') or \
                           yes('Presenta sensibilidad a la luz') or\
                           yes('Tiene la sensacion de tener un objeto en el ojo')

enfermedad('chalizion') <= yes('Tiene una protuberancia roja en el ojo') & \
                                         yes('No presenta dolor')

enfermedad('chalizion') <=  yes('La zona afectada es sensible al tacto') & \
                                          yes('su vision es borrosa en general') & \
                                          yes('Padece diabetes')

enfermedad('chalizion') <=  yes('La zona afectada es sensible al tacto') & \
                            yes('su vision es borrosa en general') & \
                            yes('Padece blefaritis')

enfermedad('chalizion') <=  yes('La zona afectada es sensible al tacto') & \
                            yes('su vision es borrosa en general') & \
                            yes('Padece dermatitis')

enfermedad('presbicia') <= yes('su vision es borrosa al ver objetos cercanos') & \
                                         yes('Presenta fatiga visual') & \
                                         yes('Presenta dolores de cabeza')

enfermedad('daltonismo') <= yes('se le dificulta ver los colores y el brillo')

enfermedad('daltonismo') <= yes('Se le dificulta diferenciar el azul del morado')

enfermedad('daltonismo') <= yes('Es incapaz de diferenciar el rojo y el verde')

enfermedad('daltonismo') <= yes('Es incapaz de diferenciar el azul y el amarillo')

#ASK -> BUILDING EXPERT SYSTEMS IN PROLOG

def verificar(S):
  if(yes(S)):
    return str(yes(S))
  else:
    if(no(S)):
      return False
    else:
      if(ask(S)==True):
        return str(yes(S))
      else:
        return False

def ask(pregunta):
  print(pregunta, "?")
  respuesta = input()
  if ((respuesta == "yes") or (respuesta == 'y')):
    +yes(pregunta)
    return True 
  else:
    +no(pregunta)
    return False

def borrar_sintomas(sintoma):
  for i in sintoma(X):
    pyDatalog.retract_fact(str(sintoma),str(i[0]))    


def go():
  end = 0
  print("..Escriba y si su situacion coincide con la siguiente descripcion..")
  for i in sintoma(X):
    verificar(i[0])
    end = end + 1
    if(len_(enfermedad(X))>0):
      print( "...Posiblemente padece de la\n", enfermedad(Enfermedad))
      print( "----------")
      return 0
    elif end == 38:
      print("...Nuestro sistema no encuentra una posible enfermedad ocular...")
go()





