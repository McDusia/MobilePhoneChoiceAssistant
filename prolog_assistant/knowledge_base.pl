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