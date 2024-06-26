edge(a, b, 1).
edge(a, c, 2).
edge(b, d, 4).
edge(c, d, 1).

best_first_search(Start, Goal, Path) :- bfs([[Start]], Goal, RevPath), reverse(RevPath, Path).

bfs([[Goal | Path] | _], Goal, [Goal | Path]).
bfs([[Node | Path] | Paths], Goal, Sol) :-
    findall([Next, Node | Path], (edge(Node, Next, _), \+ member(Next, [Node | Path])), NewPaths),
    append(Paths, NewPaths, Paths1),
    bfs(Paths1, Goal, Sol).

print_bfs(Start, Goal) :-
    best_first_search(Start, Goal, Path),
    write('Path: '), write(Path), nl.
