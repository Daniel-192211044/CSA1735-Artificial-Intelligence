diet(diabetes, 'Low sugar diet').
diet(hypertension, 'Low sodium diet').
diet(obesity, 'Low fat diet').

suggest_diet(Disease) :-
    diet(Disease, Diet),
    write('For '), write(Disease), write(', the diet is: '), write(Diet), nl.
