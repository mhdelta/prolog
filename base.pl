
plaga(picudo_negro).
plaga(picudo_rayado_amarillo).
plaga(nematodos).

sintoma().

tratamiento("Realizar una zonificacion de 5 metros de radio para aislar la plata enferma", moko).

tratamiento("", pudricion_acuosa_del_pseudotallo)

enfermedad(moko):- sintoma(marchitamiento), 
					sintoma(amarillamiento),
					sintoma(hojas_secas),
					sintoma(hojas_quebradas), 
					sintoma(hojas_con_franja_amarilla), 
					sintoma(racimos_deformes), 
					sintoma(maduracion_temprana),
					sintoma(lineas_y_puntos_oscuros_en_cormo), 
					sintoma(puntos_oscuros_en_seudotallo),
					sintoma(puntos_rojizos_o_cafe_en_raquis).

enfermedad(mal_De_Panama) :- 
sintoma(marchitamiento),
sintoma(pudricion_semillas),
sintoma(pudricion_raices),
sintoma(pudricion_tallo),
sintoma(pudricion_tuberculos),
sintoma(mancha_marron),
sintoma(necrosis),
sintoma(seudotallo_amarillo),
sintoma(seudotallo_purpura),
sintoma(seudotallo_rojo),
sintoma(amarillamiento).

enfermedad(pudricion_acuosa_del_pseudotallo) :- 
					sintoma(hojas_quemadas),
					sintoma(amarilleamiento), 
					sintoma(hojas_manchadas).

enfermedad(sigatoka_negra):- sintoma(hojas_manchadas), 
					sintoma(hojas_rayadas), sintoma(hojas_secas), 
					sintoma(hojas_negras), sintoma(hojas_muertas).	
					
%% diagnotico(Enfermedad, Tatramiento):- enfermedad(Enfermedad), tratamiento(Tratamiento, Enfermedad).


%% diagnotico(Enfermedad, tatamiento):-member(Sintoma,[marchitamiento,amarillamiento,hojas_secas]),enfermedad(moko).



