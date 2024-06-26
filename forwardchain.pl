fact(a).
fact(b).

rule(c) :- fact(a), fact(b).

forward_chaining(NewFact) :- rule(NewFact), \+ fact(NewFact), assert(fact(NewFact)), write('New fact derived: '), write(NewFact), nl.
forward_chaining(_).

run_forward_chaining :-
    repeat,
    forward_chaining(_),
    \+ rule(_),
    !.

print_all_facts :-
    fact(Fact),
    write('Fact: '), write(Fact), nl, fail.
print_all_facts.
