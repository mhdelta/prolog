from pyDatalog import pyDatalog
pyDatalog.create_terms('enfermedad, vision, dolor, herencia, afectacion, otros_sintomas, color, edad, patologia, ubicacion_orzuelo, pus')
pyDatalog.create_terms('X, Y')
pyDatalog.create_terms('ask, que_dolor, Attr, Val, preguntar, que_color')
pyDatalog.create_terms('yes, no, sintoma')

+sintoma('Presenta dolores de cabeza')
+sintoma('Presenta dolor en la zona afectada')
+sintoma('No presenta dolor')
+sintoma('presenta ardor en la zona afectada')
# 
+sintoma('su vision es borrosa en general')
+sintoma('su vision es borrosa al ver objetos lejanos')
+sintoma('su vision es borrosa al ver objetos cercanos')
+sintoma('ve doble')
+sintoma('Presenta sensibilidad a la luz')
+sintoma('Se le dificulta ver de noche')
# 
+sintoma('Tiene familiares que padezcan diabetes')
+sintoma('Tiene familiares que padezcan miopia')
# 
+sintoma('Presenta fatiga visual')
+sintoma('ha tenido alguna herida en el ojo recientemente')
+sintoma('Tiene los ojos rojos')
+sintoma('Tiene la sensacion de tener un objeto en el ojo')
+sintoma('La zona afectada esta hinchada')
+sintoma('Tiene picazon en la zona afectada')
+sintoma('Presenta lagrimeo')
# 
+sintoma('De la zona afectada sale pus amarillo')
+sintoma('De la zona afectada sale pus verde')
+sintoma('Tiene pus en la protuberancia')
# 
+sintoma('se le dificulta ver los colores y el brillo')
+sintoma('Se le dificulta diferenciar el azul del morado')
+sintoma('Es incapaz de diferenciar el rojo y el verde')
+sintoma('Es incapaz de diferenciar el azul y el amarillo')
+sintoma('Percibe resplandor y luces anormales')
+sintoma('ve los colores destenidos')
# 
+sintoma('Padece diabetes')
+sintoma('Padece blefaritis')
+sintoma('Padece dermatitis')

+ubicacion_orzuelo('en_base_pestana')
+ubicacion_orzuelo('en_interior_parpado')
# 
+sintoma('Tiene una protuberancia roja en el ojo')
+sintoma('Esta expuesto a radiacion constantemente')
+sintoma('Esta expuesto a rayos ultravioletas constantemente')
+sintoma('La zona afectada es sensible al tacto')
# 
+sintoma('Es mayor de 30 anios')
+sintoma('Es menor de 30 anios')
+sintoma('Es mayor de 60 anios')