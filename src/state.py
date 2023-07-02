class Game():
    def __init__(self) -> None:
        self.hands = [Hand(), Hand()]
        self.balls = [Ball(), Ball(), Ball()]
        self.t = 0
    
    def step(self, action):
        self.t += 1
        throw = action.throw()
        for ball in self.balls:
            for hand in self.hands:
                if hand.contains(ball) and throw:
                    ball.throw(throw)
                    


class Ball():
    def __init__(self, x, z) -> None:
        self.x = x
        self.z = z
        self.vx = 0
        self.vz = 0
    
class Hand():
    def __init__(self, x, z) -> None:
        self.x = x
        self.z = z

