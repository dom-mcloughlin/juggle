import os

HAND_RADIUS = 1
GRAVITY = 10
TIMESTEP = 0.1

BALL_INITIAL_CONDITIONS = {
    'x1': 20,
    'z1': 0,
    'x2': 90,
    'z2': 90,
    'x3': 90,
    'z3': 0,

}

HAND_INITIAL_CONDITIONS = {
    'x1': 20,
    'x2': 90,

}


if not os.path.exists('logs'):
    os.mkdir("logs")
