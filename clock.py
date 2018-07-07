# Determines angle between clock seconds hand and minutes hand given the time

def angle():

    time = str(input(print("Time (hh:mm) without pm or am -- ")))
    time = time.split(":")

    hours = int(time[0])
    minutes = int(time[1])

    hours = hours
    minutes = minutes

    hoursHandPassed = minutes / 60
    hours = hours + (5 * hoursHandPassed)

    print(6*((hours * 5)-minutes))

angle()
