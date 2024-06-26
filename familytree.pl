parent(john, mary).
parent(mary, susan).
parent(john, mike).
parent(mike, george).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
print_family_member(Member) :-
    parent(Member, Child),
    write(Member), write(' is a parent of '), write(Child), nl.
print_family_member(Member) :-
    grandparent(Member, GrandChild),
    write(Member), write(' is a grandparent of '), write(GrandChild), nl.
print_family_member(Member) :-
    sibling(Member, Sibling),
    write(Member), write(' is a sibling of '), write(Sibling), nl.
