/* Enfermedad.pro
  Enfermedad identification game.  

    start with ?- go.     */

go :- hipotesis(Enfermedad),
      write('Su cultivo padece de : '),
      write(Enfermedad),
      nl,
      write('Su tratamiento más básico consiste en:'),
      diagnosticar(Enfermedad),
      undo.



/* hypotheses to be tested */
hipotesis(mal_de_panama)   :- mal_de_panama, !.
hipotesis(moko)     :- moko, !.
hipotesis(pudricion_acuosa_del_pseudotallo) :- pudricion_acuosa_del_pseudotallo, !.
hipotesis(sigatoka_negra) :- sigatoka_negra, !.
hipotesis(picudos) :- picudos, !.
hipotesis(nematodos) :- nematodos, !.
hipotesis(unknown).             /* no diagnosis */

/* Enfermedad identification rules */
mal_de_panama :- sintomas_mal_leves, !.
mal_de_panama :- verificar(seudotallo_amarillo),
                 verificar(amarillamiento).

moko :-   sintomas_moko_leves,
          verificar(hojas_secas),
          verificar(hojas_quebradas), 
          verificar(mancha_marron), 
          verificar(hojas_con_franja_amarilla).

pudricion_acuosa_del_pseudotallo :- verificar(hojas_quemadas),
                                    verificar(amarillamiento),
                                    verificar(hojas_manchadas).

sigatoka_negra :- verificar(hojas_negras), !.
sigatoka_negra :- verificar(hojas_manchadas),
                  verificar(hojas_secas),
                  verificar(hojas_manchadas).

picudos :- verificar(perforaciones), !. 
picudos :- verificar(planta_debil), 
          verificar(amarillamiento), !.
picudos :- verificar(poco_crecimiento), 
          verificar(tallos_delgados).

nematodos :- verificar(amarillamiento),
             verificar(menor_numero_de_hojas), !.
nematodos:- verificar(mala_calidad_del_racimo), !.
nematodos:- verificar(poco_crecimiento), !. 

/* classification rules */
sintomas_mal_leves :-verificar(necrosis), !. 
sintomas_mal_leves :-verificar(marchitamiento).
sintomas_mal_leves :-verificar(pudricion_semillas).
sintomas_mal_leves :-verificar(pudricion_raices).
sintomas_mal_leves :-verificar(pudricion_tallo).
sintomas_mal_leves :- verificar(seudotallo_purpura).
sintomas_mal_leves :- verificar(seudotallo_rojo).
sintomas_mal_leves :-verificar(pudricion_tuberculos). 
   

sintomas_moko_leves :-verificar(marchitamiento).
sintomas_moko_leves :-verificar(amarillamiento). 
sintomas_moko_leves :-verificar(racimos_deformes), !.
sintomas_moko_leves :-verificar(maduracion_temprana), !.
sintomas_moko_leves :-verificar(lineas_y_puntos_oscuros_en_cormo). 
sintomas_moko_leves :-verificar(puntos_oscuros_en_seudotallo).
sintomas_moko_leves :-verificar(puntos_rojizos_o_cafe_en_raquis).          

tratamiento("Realizar una zonificacion de 5 metros de radio para aislar la plata enferma", moko).
tratamiento("Realizar deshojes con hojas secas y destruir las plantas en estado avanzado de infección", pudricion_acuosa_del_pseudotallo).
tratamiento("Tomar medidas cuarentenarias y eliminar plantas enfermas", mal_de_panama).
tratamiento("Realizar: despunte, cirugia, daslamine y deshoje", sigatoka_negra).

tratamiento("Introducir insectos que la atacan, como: tijeretas y hormigas", picudos).
tratamiento("Desinfectar el suelo con calor y usar hongos como Paecilomyces lillacinus y Fusarium sp", nematodos). 

diagnosticar(X) :- tratamiento(Y,X), write(Y).

          
/* how to ask Preguntas */
ask(Pregunta) :-
    write('Su cultivo tiene el siguiente sintoma: '),
    write(Pregunta),
    write('? '),
    read(Respuesta),
    nl,
    ( (Respuesta == yes ; Respuesta == y)
      ->
       assert(yes(Pregunta)) ;
       assert(no(Pregunta)), fail).

/* How to verificar something */
verificar(S) :-
   (yes(S) 
    ->
    true ;
    (no(S)
     ->
     fail ;
     ask(S))).

:- dynamic yes/1,no/1.
/* undo all yes/no assertions */
undo :- retract(yes(_)),fail. 
undo :- retract(no(_)),fail.
undo.