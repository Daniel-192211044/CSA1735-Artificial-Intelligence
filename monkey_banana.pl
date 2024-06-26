initial_state(state(at_door, on_floor, at_window, has_not)).
goal_state(state(_, _, _, has)).
move(state(at_door, on_floor, at_window, has_not),
     grasp,
     state(at_window, on_floor, at_window, has)).

solve(State, Moves) :- goal_state(State), Moves = [].
solve(State, [Move | Moves]) :- move(State, Move, NextState), solve(NextState, Moves).
print_solution :- initial_state(InitialState), solve(InitialState, Moves), write('Solution: '), write(Moves), nl.
