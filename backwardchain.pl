fact(a).
fact(b).

rule(c) :- fact(a), fact(b).

backward_chaining(Goal) :- fact(Goal).
backward_chaining(Goal) :- rule(Goal), \+ fact(Goal), assert(fact(Goal)).

run_backward_chaining(Goal) :-
    backward_chaining(Goal),
    write('Goal '), write(Goal), write(' is achievable'), nl.
run_backward_chaining(_) :-
    write('Goal is not achievable'), nl.

print_all_facts :-
    fact(Fact),
    write('Fact: '), write(Fact), nl, fail.
print_all_facts.
