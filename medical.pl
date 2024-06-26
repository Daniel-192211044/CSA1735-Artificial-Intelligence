symptom(fever, flu).
symptom(cough, flu).
symptom(sore_throat, cold).
symptom(runny_nose, cold).
diagnose(Disease) :-
    symptom(Symptom, Disease),
    write('Does the patient have '), write(Symptom), write('? (yes/no) '),
    read(yes).
print_all_diagnoses :-
    symptom(Symptom, Disease),
    write(Symptom), write(' is a symptom of '), write(Disease), nl, fail.
print_all_diagnoses.
