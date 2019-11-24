has("Bluboo S3", battery_capacity, 8500).
has("Bluboo S3", cpu_frequency, 1500).
has("Xiaomi Redmi 5A", battery_capacity, 4500).
has("Xiaomi Redmi 5A", cpu_frequency, 1700).
has("HTC Google Pixel", battery_capacity, 10).
has("HTC Google Pixel", cpu_frequency, 2150).
has("Samsung Galaxy S10", battery_capacity, 10).
has("Samsung Galaxy S10", cpu_frequency, 0).

up_threshold(battery_capacity, large, 8000).
up_threshold(battery_capacity, big, 4000).
up_threshold(battery_capacity, ok, 3000).
up_threshold(cpu_frequency, high, 2000).
down_threshold(cpu_frequency, low, 1600).

has("Bluboo S3", storage, 3096).
has("Bluboo S3", touch_screen, true).
has("Bluboo S3", nfc, true).
has("Bluboo S3", water_resistant, true).
has("Bluboo S3", dual_sim, false).
has("Bluboo S3", back_camera_matrix, 5.0).
has("Bluboo S3", front_camera_matrix, 7.0).
has("Bluboo S3", cpu_n_cores, 3).

has("Xiaomi Redmi 5A", brand, "Xiaomi").
has("Xiaomi Redmi 5A", battery_capacity, 4500).
has("Xiaomi Redmi 5A", cpu_frequency, 1700).
has("Xiaomi Redmi 5A", storage, 2700).
has("Xiaomi Redmi 5A", touch_screen, true).
has("Xiaomi Redmi 5A", nfc, false).
has("Xiaomi Redmi 5A", water_resistant, true).
has("Xiaomi Redmi 5A", dual_sim, false).
has("Xiaomi Redmi 5A", back_camera_matrix, 4.0).
has("Xiaomi Redmi 5A", front_camera_matrix, 3.0).
has("Xiaomi Redmi 5A", cpu_n_cores, 2).

has("HTC Google Pixel", brand, "Google").
has("HTC Google Pixel", battery_capacity, 10).
has("HTC Google Pixel", cpu_frequency, 2150).
has("HTC Google Pixel", storage, 5700).
has("HTC Google Pixel", touch_screen, true).
has("HTC Google Pixel", nfc, false).
has("HTC Google Pixel", water_resistant, true).
has("HTC Google Pixel", dual_sim, false).
has("HTC Google Pixel", back_camera_matrix, 4.0).
has("HTC Google Pixel", front_camera_matrix, 8.0).
has("HTC Google Pixel", cpu_n_cores, 2).

has("Samsung Galaxy S10", brand, "Samsung").
has("Samsung Galaxy S10", battery_capacity, 10).
has("Samsung Galaxy S10", cpu_frequency, 0).
has("Samsung Galaxy S10", storage, 2000).
has("Samsung Galaxy S10", touch_screen, true).
has("Samsung Galaxy S10", nfc, true).
has("Samsung Galaxy S10", water_resistant, false).
has("Samsung Galaxy S10", dual_sim, false).
has("Samsung Galaxy S10", back_camera_matrix, 5.0).
has("Samsung Galaxy S10", front_camera_matrix, 2.0).
has("Samsung Galaxy S10", cpu_n_cores, 2).

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

