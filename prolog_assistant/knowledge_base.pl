:- dynamic
    has/2.

model("Bluboo S3") :- has(battery_capacity, 8500).
model("Xiaomi Redmi 5A") :- has(battery_capacity, 3000).
model("HTC Google Pixel") :- has(battery_capacity, 2770).

battery_threshold(excellent, 6999).
battery_threshold(good, 2999).
battery_threshold(irrelevant, 0).
