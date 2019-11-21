:- dynamic
    has/3,
    user_requirement/2.

max(Model, Feature) :-
    required(Feature, RequiredLevel),
    down_threshold(Feature, RequiredLevel, X),
    has(Model, Feature, V),
    (V < X).
min(Model, Feature) :-
    required(Feature, RequiredLevel),
    up_threshold(Feature, RequiredLevel, X),
    has(Model, Feature, V),
    (V > X).

meets_feature_requirements(Model, Feature) :- min(Model, Feature).
meets_feature_requirements(Model, Feature) :- max(Model, Feature).
meets_feature_requirements(Model, Feature) :-
    has(Model, _, _),
    required(Feature, _), !, fail.
meets_feature_requirements(Model, _) :- has(Model, _, _).

required(battery_capacity, ok) :- user_requirement(battery_life, good).
required(battery_capacity, large) :- user_requirement(battery_life, excellent).

required(cpu_frequency, low) :- user_requirement(cpu_frequency, low).
required(cpu_frequency, high) :- user_requirement(cpu_frequency, high).


% TODO: this returns the same model multiple times
model(Model) :-
    meets_feature_requirements(Model, cpu_frequency).
%    meets_feature_requirements(Model, battery_capacity).