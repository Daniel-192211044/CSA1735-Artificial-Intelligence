move(1, Source, Target, _) :-
    write('Move disk from '), write(Source), write(' to '), write(Target), nl.
move(N, Source, Target, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    move(N1, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(N1, Auxiliary, Target, Source).

% Rule to solve the puzzle
solve_hanoi(N) :- move(N, 'A', 'C', 'B').
