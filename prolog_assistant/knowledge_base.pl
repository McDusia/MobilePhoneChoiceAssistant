has("Microsoft Kin One", brand, "Microsoft").
has("Microsoft Kin One", battery_capacity, 1240).
has("Microsoft Kin One", display_diagonal, 2.6).
has("Microsoft Kin One", display_width, 320).
has("Microsoft Kin One", display_height, 240).
has("Microsoft Kin One", display_number_of_colors, 16777216).
has("Microsoft Kin One", storage, 4096).
has("Microsoft Kin One", touch_screen, true).
has("Microsoft Kin One", nfc, false).
has("Microsoft Kin One", water_resistant, true).
has("Microsoft Kin One", dual_sim, false).
has("Microsoft Kin One", cpu_frequency, 600).
has("Microsoft Kin One", cpu_n_cores, 1).
has("Microsoft Kin One", gps, true).
has("Microsoft Kin One", agps, true).
has("Microsoft Kin One", glonass, false).
has("Microsoft Kin One", galileo, false).
has("Microsoft Kin One", quick_charge, false).
has("Microsoft Kin One", has_jack, true).
has("Microsoft Kin One", usb_c, false).
has("Microsoft Kin One", sim_type, sim).
has("Microsoft Kin One", back_camera_matrix, 5.0).
has("Microsoft Kin One", front_camera_matrix, 1.0).
has("Microsoft Kin One", price, 612.4).

has("OnePlus One", brand, "OnePlus").
has("OnePlus One", battery_capacity, 3100).
has("OnePlus One", memory, 3072).
has("OnePlus One", display_diagonal, 5.5).
has("OnePlus One", display_width, 1080).
has("OnePlus One", display_height, 1920).
has("OnePlus One", display_number_of_colors, 16777216).
has("OnePlus One", storage, 16384).
has("OnePlus One", touch_screen, true).
has("OnePlus One", nfc, true).
has("OnePlus One", water_resistant, true).
has("OnePlus One", dual_sim, true).
has("OnePlus One", android_version, 4.4).
has("OnePlus One", cpu_frequency, 2500).
has("OnePlus One", cpu_n_cores, 4).
has("OnePlus One", gps, true).
has("OnePlus One", agps, true).
has("OnePlus One", glonass, true).
has("OnePlus One", galileo, false).
has("OnePlus One", quick_charge, false).
has("OnePlus One", has_jack, true).
has("OnePlus One", usb_c, false).
has("OnePlus One", sim_type, sim).
has("OnePlus One", back_camera_matrix, 13.0).
has("OnePlus One", front_camera_matrix, 5.0).
has("OnePlus One", price, 1078.4).

has("Gupp Phreedom", brand, "Gupp").
has("Gupp Phreedom", battery_capacity, 2200).
has("Gupp Phreedom", display_diagonal, 2.5).
has("Gupp Phreedom", display_width, 320).
has("Gupp Phreedom", display_height, 240).
has("Gupp Phreedom", display_number_of_colors, 262144).
has("Gupp Phreedom", touch_screen, false).
has("Gupp Phreedom", nfc, false).
has("Gupp Phreedom", water_resistant, true).
has("Gupp Phreedom", dual_sim, false).
has("Gupp Phreedom", cpu_frequency, 312).
has("Gupp Phreedom", gps, false).
has("Gupp Phreedom", agps, false).
has("Gupp Phreedom", glonass, false).
has("Gupp Phreedom", galileo, false).
has("Gupp Phreedom", quick_charge, true).
has("Gupp Phreedom", has_jack, true).
has("Gupp Phreedom", usb_c, false).
has("Gupp Phreedom", sim_type, sim).
has("Gupp Phreedom", price, 1203.8).

down_threshold(battery_capacity, large, 8000).
down_threshold(battery_capacity, big, 4000).
down_threshold(battery_capacity, ok, 3000).
down_threshold(cpu_frequency, high, 2000).
down_threshold(cpu_frequency, low, 1600).
down_threshold(storage, low, 2000).
down_threshold(storage, high, 3000).
down_threshold(back_camera_matrix, excellent, 4.5).
down_threshold(back_camera_matrix, good, 3.0).
down_threshold(front_camera_matrix, excellent, 3.0).
down_threshold(front_camera_matrix, good, 2.0).
down_threshold(cpu_n_cores, many, 3).
down_threshold(cpu_n_cores, medium_amount, 2).