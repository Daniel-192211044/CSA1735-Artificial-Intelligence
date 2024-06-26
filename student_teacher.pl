teaches(john, math, 101).
teaches(mary, english, 102).
teaches(alice, science, 103).

print_teacher_info(Teacher) :- teaches(Teacher, Subject, Code), write(Teacher), write(' teaches '), write(Subject), write(' with code '), write(Code), nl.
