planet('Mercury', 'small', '0.39 AU').
planet('Venus', 'medium', '0.72 AU').
planet('Earth', 'medium', '1 AU').
planet('Mars', 'small', '1.52 AU').

print_planet_info(Name) :- planet(Name, Size, Distance), write(Name), write(' is '), write(Size), write(' and is '), write(Distance), nl.
