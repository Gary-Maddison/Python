total_km = 0
target = 30

for day in range(1, 8):
    daily_total = float(input(f"How many KM's did you run on day {day}: "))
    total_km += daily_total

goal = target - total_km

if goal <= 0:
    print(
        f"You ran {total_km} km's this weeek. You hit your weekly goal of {target}")
else:
    print(
        f"You ran {total_km} km's this weeek. You were {goal}km's away from your goal of {target}.")
