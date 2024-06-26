bird(eagle).
bird(penguin).
bird(sparrow).
cannot_fly(penguin).

can_fly(Bird) :- bird(Bird), \+ cannot_fly(Bird).

check_bird(Bird) :-
    bird(Bird),
    (can_fly(Bird) -> write(Bird), write(' can fly'); write(Bird), write(' cannot fly')), nl.
check_bird(Bird) :-
    \+ bird(Bird),
    write('Unknown bird: '), write(Bird), nl.
