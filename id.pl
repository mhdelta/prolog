%Enfermedad Identification Game
%Start with ?- go.

go:- hipotesis(Enfermedad),
    write('Creo que su cultivo padece de: '),
    write(Enfermedad),
    nl.
    undo.

%hipotesis that should be tested
hipotesis(cold):- cold, !.
hipotesis(flu):- flu, !.
hipotesis(ebola):- ebola, !.
hipotesis(measles):- measles, !.
hipotesis(unknown). /* no diagnosis*/

%hipotesis Identification Rules
cold :-
       verificar(headache),
       verificar(runny_nose),
       verificar(sneezing),
       verificar(sore_throat).
flu :-
       verificar(fever),
       verificar(headache),
       verificar(chills),
       verificar(body_ache).
ebola :-
       verificar(headache),
       verificar(rash),
       verificar(nausea),
       verificar(bleeding).
measles :-
       verificar(fever),
       verificar(runny_nose),
       verificar(rash),
       verificar(conjunctivitis).

/* how to ask Preguntas */
ask(Pregunta) :-
    write('Does the patient have the following symptom: '),
    write(Pregunta),
    write('? '),
    read(Respuesta),
    nl,
    ( (Respuesta == yes ; Respuesta == y)
      ->
       assert(yes(Pregunta)) ;
       assert(no(Pregunta)), fail).

:- dynamic yes/1,no/1.

/* How to verificar something */
verificar(S) :- (yes(S) -> true ; (no(S)  -> fail ; ask(S))).

/* undo all yes/no assertions */
undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.