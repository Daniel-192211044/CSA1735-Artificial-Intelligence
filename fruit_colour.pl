fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).

find_color(Fruit) :-
    fruit(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl.
