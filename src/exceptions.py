class BallOutOfBoundsError(Exception):
    pass


class BallDroppedError(BallOutOfBoundsError):
    pass


class BallTooHighError(BallOutOfBoundsError):
    pass


class BallLeftError(BallOutOfBoundsError):
    pass


class BallRightError(BallOutOfBoundsError):
    pass
