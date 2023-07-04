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

NEURAL_NETWORK_PARAMETERS = {
    "input_size": 14,
    "first_layer_size": 11,
    "second_layer_size": 11,
    "third_layer_size": 11,
    "output_size": 4,

}

FIXED_THROW_VZ = 15

if not os.path.exists('logs'):
    os.mkdir("logs")
