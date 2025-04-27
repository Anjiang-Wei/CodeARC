def calculate_time_to_complete_distance(v0: float, slope: float, dTot: float) -> int:
    from math import sin, atan

    GRAVITY_ACC = 9.81 * 3.6 * 60.0  # gravity acceleration
    DRAG = 60.0 * 0.3 / 3.6          # force applied by air on the cyclist
    DELTA_T = 1.0 / 60.0             # in minutes
    D_WATTS = 0.5                    # power loss in Watts / minute
    G_THRUST = 60 * 3.6 * 3.6        # acceleration due to biker's power
    MASS = 80                        # biker's MASS
    WATTS0 = 225                     # initial biker's power

    t = 0.0          # time in minutes
    d = 0.0          # distance traveled in km
    v = v0           # initial speed km/h
    gamma = 0.0      # acceleration in km/h/minute
    watts = WATTS0   # biker's power

    slopeGravityAcc = -GRAVITY_ACC * sin(atan(slope / 100.0))

    while d <= dTot:
        t += DELTA_T
        # new power
        watts -= D_WATTS * DELTA_T  # tiredness
        # earth gravity due to slope and DRAG due to air resistance
        gamma = slopeGravityAcc - DRAG * abs(v) * abs(v) / MASS
        # acceleration due to biker's power
        if watts > 0.0 and v > 0.0:
            gamma += G_THRUST * watts / (v * MASS)
        # acceleration too small -> acc = 0
        if abs(gamma) <= 1e-5:
            gamma = 0.0
        else:
            v += gamma * DELTA_T
        # new distance
        d += v * DELTA_T / 60.0  # v in km/h, DELTA_T in minutes
        # speed too slow, John stops
        if v - 3.0 <= 1e-2:
            return -1

    return round(t)

