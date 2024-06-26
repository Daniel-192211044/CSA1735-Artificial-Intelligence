person('Alice', '1990-01-01').
person('Bob', '1985-05-12').
person('Carol', '2000-07-22').
print_all :- person(Name, DOB), write(Name), write(' was born on '), write(DOB), nl, fail.
print_all.
