def calculate_meeting_time(Ta: float, Tb: float, r: float) -> str:
    if Ta == 0:
        return "{:.2f}".format(abs(Tb))
    elif Tb == 0:
        return "{:.2f}".format(abs(Ta))
    else:
        # Calculate the meeting time using the formula for angular velocity
        return "{:.2f}".format(abs(Ta * Tb / (Tb - Ta)))

