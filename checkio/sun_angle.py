"""
Every true traveler must know how to do 3 things: fix the fire, find the water
and extract useful information from the nature around him. Programming won't
help you with the fire and water, but when it comes to the information
extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time
of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds
to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means
that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle
is 180 degrees. If the input will be the time of the night (before 6:00 AM or
after 6:00 PM), your function should return - "I don't see the sun!".
"""


"""MY"""
def sun_angle(t):
    hours, minutes = map(int, t.split(':'))
    if hours < 6 or hours > 18 or (hours == 18 and minutes):
        return "I don't see the sun!"
    return 0.25 * ((hours - 6) * 60 + minutes)


assert sun_angle("12:15") == 93.75


"""1"""
# def sun_angle(time):
#     hours = int(time[:2]) + int(time[3:]) / 60
#     if (hours < 6) or (hours > 18):
#         return "I don't see the sun!"
#     else:
#         return (hours - 6)/12 * 180


"""2"""
# from datetime import datetime
# from scipy.interpolate import interp1d
#
# solutions = {'06:00': 0, '12:00': 90, '18:00': 180}
# stamp = lambda time: datetime.strptime(time, '%H:%M').timestamp()
# line = interp1d([*map(stamp, solutions)], [*solutions.values()])
#
# def sun_angle(time):
#     try: return line(stamp(time))[()]
#     except ValueError: return "I don't see the sun!"
