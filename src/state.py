import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas

from src.constants import BALL_INITIAL_CONDITIONS, GRAVITY, HAND_INITIAL_CONDITIONS, HAND_RADIUS, TIMESTEP
from src.exceptions import BallDroppedError


class Game():
    def __init__(self) -> None:
        self.left_hand = Hand(HAND_INITIAL_CONDITIONS['x1'])
        self.right_hand = Hand(HAND_INITIAL_CONDITIONS['x2'])
        self.hands = [self.left_hand, self.right_hand]
        self.balls = [
            Ball(BALL_INITIAL_CONDITIONS['x1'], BALL_INITIAL_CONDITIONS['z1']),
            Ball(BALL_INITIAL_CONDITIONS['x2'], BALL_INITIAL_CONDITIONS['z2']),
            Ball(BALL_INITIAL_CONDITIONS['x3'], BALL_INITIAL_CONDITIONS['z3'])
        ]
        self.t = 0
        self.history = []

    def steps(self, actions):
        for action in actions:
            try:
                self.step(action)
            except BallDroppedError:
                self.log_state()
                raise

    def step(self, action):
        self.action = action
        self.t += 1
        throw = action.throw()
        for ball in self.balls:
            # Move balls
            caught = False
            for ii, hand in enumerate(self.hands):
                if hand.contains(ball):
                    # Ball in hand
                    caught = True
                    vx, vz = throw[2*ii:2*(ii+1)]
                    if vx == vz == 0:
                        # Keep ball in hand 
                        ball.x = hand.x
                    else:
                        ball.throw(vx, vz)
                        ball.move()
            if not caught:
                # Move ball (freefall)
                ball.move()
        # Move hands
        self.left_hand.x += action.left_hand_vx * TIMESTEP
        self.right_hand.x += action.right_hand_vx * TIMESTEP
        self.log_state()
        return

    def log_state(self):
        row = {
            "time": self.t,
            "left_hand_x": self.left_hand.x,
            "right_hand_x": self.right_hand.x,
            "ball1x": self.balls[0].x,
            "ball1z": self.balls[0].z,
            "ball1vx": self.balls[0].vx,
            "ball1vz": self.balls[0].vz,
            "ball2x": self.balls[1].x,
            "ball2z": self.balls[1].z,
            "ball2vx": self.balls[1].vx,
            "ball2vz": self.balls[1].vz,
            "ball3x": self.balls[2].x,
            "ball3z": self.balls[2].z,
            "ball3vx": self.balls[2].vx,
            "ball3vz": self.balls[2].vz,
            "action_throw_h1_vx": self.action.throw_h1_vx,
            "action_throw_h1_vz": self.action.throw_h1_vz,
            "action_throw_h2_vx": self.action.throw_h2_vx,
            "action_throw_h2_vz": self.action.throw_h2_vz,
            "action_left_hand_vx": self.action.left_hand_vx,
            "action_right_hand_vx": self.action.right_hand_vx,
        }
        self.history.append(row)

    def get_history(self) -> pandas.DataFrame:
        df = pandas.DataFrame(self.history)
        return df

    def write_history(self):
        df = self.get_history()
        timestamp = datetime.datetime.now().isoformat()
        df.to_csv(f'logs/{timestamp}.csv', index=False)
        df.to_csv(f'~/.juggle/latest.csv', index=False)
        print(df.head())
        return

    def plot_history(self):
        df = self.get_history()
        plt.scatter(df['ball1x'], df['ball1z'], label='ball1', c="r")
        plt.scatter(df['ball2x'], df['ball2z'], label='ball2', c="g")
        plt.scatter(df['ball3x'], df['ball3z'], label='ball3', c="b")
        plt.scatter(df['left_hand_x'], [0]*len(df), marker="x", c='purple', label='left_hand')
        plt.scatter(df['right_hand_x'], [0]*len(df), marker="x", c='pink', label='right_hand')
        plt.legend()
        plt.show()

class Ball():
    def __init__(self, x, z) -> None:
        self.x = x
        self.z = z
        self.vx = 0
        self.vz = 0

    def throw(self, vx, vz):
        self.vx = vx
        self.vz = vz

    def move(self):
        self.x = self.x + self.vx * TIMESTEP
        self.z = self.z + self.vz * TIMESTEP
        self.vz = self.vz - GRAVITY * TIMESTEP
        if self.z < 0:
            raise BallDroppedError
        if self.z > 100:
            raise BallTooHighError
        if self.x < 0:
            raise BallLeftError
        if self.x > 100:
            raise BallRightError


    def __repr__(self) -> str:
        return f"x: {self.x}\nz: {self.z}\nvx: {self.vx}\nvz: {self.vz}"

class Hand():
    def __init__(self, x) -> None:
        self.x = x

    def contains(self, ball: Ball) -> bool:
        distance = np.abs(ball.x - self.x)
        return distance <= HAND_RADIUS and ball.z == 0


class Throw():
    def __init__(self, vx, vz) -> None:
        self.vx = vx
        self.vz = vz
        return


class Action():
    def __init__(self, throw_h1_vx, throw_h1_vz, throw_h2_vx, throw_h2_vz, left_hand_vx, right_hand_vx) -> None:
        self.throw_h1_vx = throw_h1_vx
        self.throw_h1_vz = throw_h1_vz
        self.throw_h2_vx = throw_h2_vx
        self.throw_h2_vz = throw_h2_vz
        self.left_hand_vx = left_hand_vx
        self.right_hand_vx = right_hand_vx
    
    def throw(self):
        return self.throw_h1_vx, self.throw_h1_vz, self.throw_h2_vx, self.throw_h2_vz
