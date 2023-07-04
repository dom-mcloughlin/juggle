from src.state import Action, Game


class Agent():
    def __init__(self, game: Game) -> None:
        self.game = game
    
    def choose_action(self) -> Action:
        current_state = self.game.history[self.game.t]
        action = Action(15,0,1,-1)
        return action