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

enfermedad('astigmatismo') <= yes('dolor_cabeza') &\
                              yes('vision_borrosa_general') &\
                              yes('dificultad_noche') &\
                              yes('fatiga_visual')                              

enfermedad('miopia') <= yes('dolor_cabeza') &\
                        yes('vision_borrosa_objetos_lejanos') &\
			                  yes('fatiga_visual') &\
			                  yes('herencia_diabetes') &\
			                  yes('herencia_miopia')

enfermedad('hipermetropia') <= yes('mayor_de_30') &\
                               yes('vision_borrosa_objetos_lejanos') &\
                               yes('vision_borrosa_objetos_cercanos')

enfermedad('hipermetropia') <= yes('menor_de_30') & \
                               yes('vision_borrosa_objetos_lejanos')

enfermedad ('conjuntivitis_infecciosa') <= yes('sensibilidad_luz') & \
                                           yes('ardor') & \
                                           yes('ojos_rojos') & \
                                           yes('lagrimeo') & \
                                           yes('sensacion_objeto_en_el_ojo')& \
                                           yes('pus_amarillo')

enfermedad ('conjuntivitis_infecciosa') <= yes('sensibilidad_luz') & \
                                           yes('ardor') & \
                                           yes('ojos_rojos') & \
                                           yes('lagrimeo') & \
                                           yes('sensacion_objeto_en_el_ojo')& \
                                           yes('pus_verde')

enfermedad('conjuntivitis_alergica') <= yes('sensibilidad_luz') & \
                                        yes('ardor') & \
                                        yes('ojos_rojos') & \
                                        yes('lagrimeo') & \
                                        yes('sensacion_objeto_en_el_ojo') &\
                                        ~yes('pus_amarillo') &\
                                        ~yes('pues_verde') 


enfermedad ('cataratas') <= yes('vision_borrosa_general') & \
                            yes('dificultad_noche') &\
                            yes('ver_doble') &\
                            yes('dificultad_ver_azul_morado') & \
                            yes('colores_destenidos')

enfermedad('cataratas') <=	yes('mayor_de_60') &\
                            yes('diabetes')

enfermedad('cataratas') <=  yes('mayor_de_60') &\
                            yes('herida_ojo')

enfermedad('cataratas') <=  yes('mayor_de_60') &\
                            yes('expuesto_radiacion')

enfermedad('cataratas') <=  yes('mayor_de_60') &\
                            yes('expuesto_rayos_ultravioletas')
                                                      
# enfermedad ('orzuelo') <= ubicacion_orzuelo('en_base_pestana') or \
#                            ubicacion_orzuelo('en_interior_parpado')& \
#                            yes('protuberancia_roja') & \
#                            yes('dolor_general') &\
#                            yes('hinchazon') & \
#                            yes('picazon') &\
#                            yes('lagrimeo') & \
#                            pus('pus_en_protuberancia') or \
#                            yes('sensibilidad_luz') or\
#                            yes('sensacion_objeto_en_el_ojo') & \
#                            yes('resplandor_luces')

enfermedad('chalizion') <= yes('protuberancia_roja') & \
							             yes('no_dolor')

enfermedad('chalizion') <=  yes('sensible_tacto') & \
							              yes('vision_borrosa_general') & \
							              yes('diabetes')

enfermedad('chalizion') <=  yes('sensible_tacto') & \
                            yes('vision_borrosa_general') & \
                            yes('blefaritis')

enfermedad('chalizion') <=  yes('sensible_tacto') & \
                            yes('vision_borrosa_general') & \
                            yes('dermatitis')

enfermedad('presbicia') <= yes('vision_borrosa_objetos_cercanos') & \
							             yes('fatiga_visual') & \
							             yes('dolor_cabeza')

enfermedad('daltonismo') <= yes('dificultad_ver_colores_brillo')

enfermedad('daltonismo') <= yes('dificultad_ver_azul_morado')

enfermedad('daltonismo') <= yes('incapacidad_diferenciar_rojo_verde')

enfermedad('daltonismo') <= yes('incapacidad_diferenciar_azul_amarillo')
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
      print("...Posiblemente padece de la\n", enfermedad(Enfermedad))
      print("----------")
      return 0
    elif end == 38:
      print("...Nuestro sistema no encuentra una posible enfermedad ocular...")

go()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# def menu_dolor():
#   i=0
#   print "POR FAVOR SELECCIONE UNA OPCION"
#   for x in dolor(X):
#     print "[", i ,"]", verificar(x[0])
#     i+=1
  

# borrar_sintomas(dolor)
# print dolor(X)
# menu_dolor()   
# print yes(X)
  # if raw_input() == 1:
# print enfermedad(X)[0][0]  


# pyDatalog.retract_fact("dolor","dolor_cabeza")
# pyDatalog.retract_fact("dolor","dolor_general")
# pyDatalog.retract_fact("dolor","no_dolor")
# pyDatalog.retract_fact("dolor","ardor")



# print enfermedad(X)


# for x in enfermedad(X):
#   if x == ('miopia',):
#     print "good"

# def preguntar(Attr, Val):
#   print Attr, ":", Val, "?"
#   if raw_input() == "y":
#     return True
#   else:
#     return False


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

