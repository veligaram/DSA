#find the point where maximum intervals overlap

def max_guests(arrive, depart):
    timeline = []
    for time in arrive:
        timeline.append((time, 1))
    for time in depart:
        timeline.append((time, -1))

    timeline.sort()
    max_guests_count = 0
    current_guests = 0
    max_time = 0

    for event in timeline:
        time, action = event
        current_guests += action
        if current_guests > max_guests_count:
            max_guests_count = current_guests
            max_time = time

    return max_time

arrive = [1, 2, 9, 5, 5]
depart = [4, 5, 12, 9, 12]
print("Time with maximum guests:", max_guests(arrive, depart))
