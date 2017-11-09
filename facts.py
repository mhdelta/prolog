from pyDatalog import pyDatalog
pyDatalog.create_terms('enfermedad, vision, dolor, herencia, afectacion, otros_sintomas, color, edad, patologia, ubicacion_orzuelo, pus')
pyDatalog.create_terms('X, Y')
pyDatalog.create_terms('ask, que_dolor, Attr, Val, preguntar, que_color')
pyDatalog.create_terms('yes, no, sintoma')

+sintoma('dolor_cabeza')
+sintoma('dolor_general')
+sintoma('no_dolor')
+sintoma('ardor')
# 
+sintoma('vision_borrosa_general')
+sintoma('vision_borrosa_objetos_lejanos')
+sintoma('vision_borrosa_objetos_cercanos')
+sintoma('ver_doble')
+sintoma('sensibilidad_luz')
+sintoma('dificultad_noche')
# 
+sintoma('herencia_diabetes')
+sintoma('herencia_miopia')
# 
+sintoma('fatiga_visual')
+sintoma('herida_ojo')
+sintoma('ojos_rojos')
+sintoma('lagrimeo')
+sintoma('sensacion_objeto_en_el_ojo')
+sintoma('herida_ojo')
+sintoma('hinchazon')
+sintoma('picazon')
# 
+sintoma('pus_amarillo')
+sintoma('pus_verde')
+sintoma('pus_en_protuberancia')
# 
+sintoma('dificultad_ver_colores_brillo')
+sintoma('dificultad_ver_azul_morado')
+sintoma('incapacidad_diferenciar_rojo_verde')
+sintoma('incapacidad_diferenciar_azul_amarillo')
+sintoma('resplandor_luces')
+sintoma('colores_destenidos')
# 
+sintoma('diabetes')
+sintoma('blefaritis')
+sintoma('dermatitis')

+ubicacion_orzuelo('en_base_pestana')
+ubicacion_orzuelo('en_interior_parpado')
# 
+sintoma('protuberancia_roja')
+sintoma('expuesto_radiacion')
+sintoma('expuesto_rayos_ultravioletas')
+sintoma('sensible_tacto')
# 
+sintoma('mayor_de_30')
+sintoma('menor_de_30')
+sintoma('mayor_de_60')

# enfermedad('miopia') <= dolor('cabeza') &\
#                         vision('borrosa_objetos_lejanos') &\
# 			                  afectacion('fatiga_visual') &\
# 			                  herencia('diabetes') & \
# 			                  herencia('miopia')

# enfermedad('hipermetropia') <= edad('mayor_de_30')or \
#                                edad('menor_de_30') and \
# 			       				 vision('borrosa_objetos_lejanos') and \
#                                vision('borrosa_objetos_cercanos')

# enfermedad('conjuntivitis_alergica') <= vision('sensibilidad_luz') and \
#                                         dolor('ardor') and \
#                                         afectacion('ojos_rojos') and \
#                                         afectacion('lagrimeo') and \
#                                         afectacion('sensacion_objeto_en_el_ojo')

# enfermedad ('conjuntivitis_infecciosa') <= vision('sensibilidad_luz') and \
#                                            dolor('ardor') and \
#                                            afectacion('ojos_rojos') and \
#                                            afectacion('lagrimeo') and \
#                                            afectacion('sensacion_objeto_en_el_ojo')and \
#                                            (pus('amarillo') or \
#                                            pus('verde'))

# enfermedad ('cataratas') <= vision('borrosa_general') and \
#                             vision('dificultad_noche') and\
#                             vision('ver_doble') and\
#                             color('dificultad_ver_azul_morado') and \
#                             color('colores_destenidos')

# enfermedad('cataratas') <=	edad('mayor_de_60') and\
#                             (patologia('diabetes') or\
#                             afectacion('herida_ojo') or\
#                             otros_sintomas('expuesto_radiacion') or\
#                             otros_sintomas('expuesto_rayos_ultravioletas'))                         
                            
# enfermedad ('orzuelo') <= ubicacion_orzuelo('en_base_pestana') or \
#                            ubicacion_orzuelo('en_interior_parpado')and \
#                            otros_sintomas('protuberancia_roja') and \
#                            dolor('general') and\
#                            afectacion('hinchazon') and \
#                            afectacion('picazon') and\
#                            afectacion('lagrimeo') and \
#                            pus('en_protuberancia') or \
#                            vision('sensibilidad_luz') or\
#                            afectacion('sensacion_objeto_en_el_ojo') and \
#                            color('resplandor_luces')

# enfermedad('chalizion') <= otros_sintomas('protuberancia_roja') and \
# 							dolor('no_dolor')

# enfermedad('chalizion') <=  otros_sintomas('sensible_tacto') and \
# 							vision('borrosa_general') and \
# 							(patologia('diabetes') or \
# 							patologia('blefaritis') or \
# 							patologia('dermatitis'))

# enfermedad('presbicia') <= vision('borrosa_objetos_cercanos') and \
# 							otros_sintomas('fatiga_visual') and \
# 							dolor('cabeza')

# enfermedad('daltonismo') <= color('dificultad_ver_colores_brillo') or \
# 							color('dificultad_ver_azul_morado') or\
# 							color('incapacidad_diferenciar_rojo_verde') or \
# 							color('incapacidad_diferenciar_azul_amarillo')