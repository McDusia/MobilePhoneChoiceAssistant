:- dynamic
    battery_threshold/1,
    required/2.

has(battery_capacity, X) :- required(battery_capacity, RequiredLevel),
                            battery_threshold(RequiredLevel, Y),
                            (X > Y).

has(battery_capacity, _) :- required(battery_capacity, _), !, fail.

has(_, _) :- true.
