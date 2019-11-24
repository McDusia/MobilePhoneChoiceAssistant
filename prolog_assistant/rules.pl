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

/**
 * User requirements translated to requirements for models.
 */
required(battery_capacity, ok) :- user_requirement(battery_life, good).
required(battery_capacity, large) :- user_requirement(battery_life, excellent).
required(cpu_frequency, low) :- user_requirement(cpu_frequency, low).
required(cpu_frequency, high) :- user_requirement(cpu_frequency, high).
<<<<<<< HEAD

=======
required(touch_screen, true) :- user_requirement(touch_screen, yes).
required(nfc, true) :- user_requirement(nfc, yes).
required(water_resistant, true) :- user_requirement(water_resistant, yes).
required(dual_sim, true) :- user_requirement(dual_sim, yes).
required(back_camera_matrix, excellent) :- user_requirement(back_camera_matrix, excellent).
required(back_camera_matrix, good) :- user_requirement(back_camera_matrix, good).
required(front_camera_matrix, excellent) :- user_requirement(front_camera_matrix, excellent).
required(front_camera_matrix, good) :- user_requirement(front_camera_matrix, good).
required(cpu_n_cores, many) :- user_requirement(cpu_n_cores, many).
required(cpu_n_cores, medium_amount) :- user_requirement(cpu_n_cores, medium_amount).

% TODO: this returns the same model multiple times
model(Model) :-
    meets_feature_requirements(Model, cpu_frequency),

    meets_feature_requirements(Model, battery_capacity).

    meets_feature_requirements(Model, battery_capacity),
    meets_feature_requirements(Model, storage),
    meets_feature_requirements(Model, touch_screen),
	meets_feature_requirements(Model, nfc),
	meets_feature_requirements(Model, water_resistant),
	meets_feature_requirements(Model, dual_sim),
    meets_feature_requirements(Model, cpu_n_cores),
	meets_feature_requirements(Model, back_camera_matrix),
    meets_feature_requirements(Model, front_camera_matrix).
    /**meets_feature_requirements(Model, display_diagonal),
    meets_feature_requirements(Model, display_width),
    meets_feature_requirements(Model, display_height),
    meets_feature_requirements(Model, display_number_of_colors),
     meets_feature_requirements(Model, storage),
     meets_feature_requirements(Model, android_version),
     meets_feature_requirements(Model, cpu_n_cores),
     meets_feature_requirements(Model, back_camera_matrix),
     meets_feature_requirements(Model, front_camera_matrix),
     meets_feature_requirements(Model, front_camera_matrix).

**/

