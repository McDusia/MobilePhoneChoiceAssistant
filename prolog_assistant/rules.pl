:- dynamic
    has/3,
    user_requirement/2.

meets_down_threshold(Model, Feature) :-
    required(Feature, RequiredLevelDesc),
    down_threshold(Feature, RequiredLevelDesc, RequiredLevelValue),
    has(Model, Feature, ModelValue),
    (ModelValue > RequiredLevelValue).


meets_feature_requirements(Model, Feature) :- meets_down_threshold(Model, Feature).
meets_feature_requirements(Model, Feature) :-
    has(Model, Feature, BoolValue),
    required(Feature, BoolValue).
meets_feature_requirements(Model, Feature) :- has(Model, Feature, _), not(required(Feature, _)).

required(battery_capacity, ok) :- user_requirement(battery_life, good).
required(battery_capacity, large) :- user_requirement(battery_life, excellent).

required(cpu_frequency, low) :- user_requirement(cpu_frequency, low).
required(cpu_frequency, high) :- user_requirement(cpu_frequency, high).

required(touch_screen, true) :- user_requirement(touch_screen, yes).
required(nfc, true) :- user_requirement(nfc, yes).
required(water_resistant, true) :- user_requirement(water_resistant, yes).
required(dual_sim, true) :- user_requirement(dual_sim, yes).


is_sufficient(Model) :-
    meets_feature_requirements(Model, cpu_frequency),
    meets_feature_requirements(Model, battery_capacity),
    meets_feature_requirements(Model, storage),
    meets_feature_requirements(Model, touch_screen),
	meets_feature_requirements(Model, nfc),
	meets_feature_requirements(Model, water_resistant),
	meets_feature_requirements(Model, dual_sim).
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