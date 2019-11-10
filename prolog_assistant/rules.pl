:- dynamic
    battery_threshold/1,
    required/2.

/*
 * whether Value for Key fits under any threshold for Key
 * e.g.:
 *   phone has(battery_capacity, 3900)
 *
 *   required(battery_capacity, not_too_big)
 *   up_threshold(battery_capacity, large, 5000)
 *   up_threshold(battery_capacity, big, 4000)
 *   down_threshold(battery_capacity, not_too_big, 4000)
 *   down_threshold(battery_capacity, small, 2000)
 *   down_threshold(battery_capacity, tiny, 1000)
 * then
 *   max(battery_capacity, not_too_big)
 *   max(battery_capacity, small)
 *   max(battery_capacity, tiny)
 * will be true
 */
max(K, V) :- required(K, RequiredLevel),
             down_threshold(K, RequiredLevel, X),
             (V < X).
min(K, V) :- required(K, RequiredLevel),
             up_threshold(K, RequiredLevel, X),
             (V > X).

% http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse45
has(K, V) :- min(K, V).
has(K, V) :- max(K, V).
has(K, _) :- required(K, _), !, fail.
has(_, _) :- true.

required(battery_capacity, ok) :- required(battery_life, good).

required(battery_capacity, large) :- required(battery_life, excellent).
required(cpu_frequency, low) :- required(battery_life, excellent).
