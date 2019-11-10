:- dynamic
    has/2.

model("Bluboo S3") :-
    has(battery_capacity, 8500),
    has(cpu_frequency, 1500).
model("Xiaomi Redmi 5A") :-
    has(battery_capacity, 4500),
    has(cpu_frequency, 1700).
model("HTC Google Pixel") :-
    has(battery_capacity, 2770),
    has(cpu_frequency, 2150).

up_threshold(battery_capacity, large, 8000).
up_threshold(battery_capacity, big, 4000).
up_threshold(battery_capacity, ok, 3000).
up_threshold(cpu_frequency, high, 2000).
down_threshold(cpu_frequency, low, 1600).