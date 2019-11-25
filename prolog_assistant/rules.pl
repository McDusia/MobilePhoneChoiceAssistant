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
    has(Model, Feature, BoolValue),
    required(Feature, BoolValue).
meets_feature_requirements(Model, Feature) :- has(Model, Feature, _), not(required(Feature, _)).
meets_feature_requirements(Model, Feature) :- not(has(Model, Feature, _)), not(required(Feature, _)).


/**
 * User requirements translated to requirements for models.
 */
required(battery_capacity, ok) :- user_requirement(battery_life, good).
required(battery_capacity, large) :- user_requirement(battery_life, excellent).
required(cpu_frequency, low) :- user_requirement(cpu_frequency, low).
required(cpu_frequency, high) :- user_requirement(cpu_frequency, high).

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


/**
 * Phone for business - requirements
 */
required(nfc, true) :- user_requirement(phone_for_business, yes).
required(dual_sim, true) :- user_requirement(phone_for_business, yes).
required(very_big_screen, true) :- user_requirement(phone_for_business, yes).
required(battery_capacity, large) :- user_requirement(phone_for_business, yes).

/**
 * Phone for trips - requirements
 */
required(gps, true) :- user_requirement(phone_for_trips, yes).
required(water_resistant, true) :- user_requirement(phone_for_trips, yes).
required(price, cheap) :- user_requirement(phone_for_trips, yes).
required(back_camera_matrix, good) :- user_requirement(phone_for_trips, yes).

/**
 * Phone for teenager
 */
required(gps, true) :- user_requirement(phone_for_teenager, yes).
required(water_resistant, true) :- user_requirement(phone_for_teenager, yes).
required(price, medium) :- user_requirement(phone_for_teenager, yes).
required(back_camera_matrix, good) :- user_requirement(phone_for_teenager, yes).
required(front_camera_matrix, good) :- user_requirement(phone_for_teenager, yes).
required(battery_capacity, big) :- user_requirement(phone_for_teenager, yes).
required(touch_screen, true) :- user_requirement(phone_for_teenager, yes).

/**
 * Phone to listening to music
 */
required(storage, high) :- user_requirement(phone_to_listening_to_music, yes).
required(has_jack, true) :- user_requirement(phone_to_listening_to_music, yes).

/**
 * Phone to social media
 */
required(cpu_frequency, high) :- user_requirement(phone_for_social_media, yes).
required(front_camera_matrix, good) :- user_requirement(phone_for_social_media, yes).
required(back_camera_matrix, good) :- user_requirement(phone_for_social_media, yes).
required(touch_screen, true) :- user_requirement(phone_for_social_media, yes).
required(big_screen, true) :- user_requirement(phone_for_social_media, yes).

/**
 * Phone to make photos
 */
required(back_camera_matrix, excellent) :- user_requirement(phone_to_make_photos, yes).
required(storage, high) :- user_requirement(phone_to_make_photos, yes).

/**
 * Phone to play games
 */
required(storage, high) :- user_requirement(phone_to_play_games, yes).
required(big_screen, true) :- user_requirement(phone_to_play_games, yes).
required(cpu_frequency, high) :- user_requirement(phone_to_play_games, yes).
required(cpu_n_cores, medium_amount) :- user_requirement(phone_to_play_games, yes).
required(display_number_of_colors, many) :- user_requirement(phone_to_play_games, yes).

required(very_big_screen, true) :- user_requirement(very_big_screen, yes).
required(big_screen, true) :- user_requirement(big_screen, yes).

required(display_diagonal, great) :- required(very_big_screen, true).
required(display_width, great) :- required(very_big_screen, true).
required(display_height, great) :- required(very_big_screen, true).
required(display_diagonal, medium) :- required(big_screen, true).
required(display_width, medium) :- required(big_screen, true).
required(display_height, medium) :- required(big_screen, true).


is_sufficient(Model) :-
    meets_feature_requirements(Model, cpu_frequency),

    meets_feature_requirements(Model, battery_capacity).

    meets_feature_requirements(Model, battery_capacity),
    meets_feature_requirements(Model, storage),
    meets_feature_requirements(Model, touch_screen),
	meets_feature_requirements(Model, nfc),
	meets_feature_requirements(Model, water_resistant),
	meets_feature_requirements(Model, dual_sim),
	meets_feature_requirements(Model, gps),
    meets_feature_requirements(Model, cpu_n_cores),
	meets_feature_requirements(Model, back_camera_matrix),
    meets_feature_requirements(Model, front_camera_matrix),
    meets_feature_requirements(Model, display_diagonal),
    meets_feature_requirements(Model, display_width),
    meets_feature_requirements(Model, display_height),
    meets_feature_requirements(Model, has_jack),
   meets_feature_requirements(Model, display_number_of_colors),
   meets_feature_requirements(Model, price).
 /**
     meets_feature_requirements(Model, android_version),

**/

