:- dynamic
    battery_threshold/1,
    required/2.

has(battery_capacity, X) :- required(battery_capacity, RequiredLevel),
                            battery_threshold(RequiredLevel, Y),
                            (X > Y).

has(battery_capacity, _) :- not(required(battery_capacity, _)).

has(_, _) :- true.
