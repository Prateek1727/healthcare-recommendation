class DummyRLAgent:
    def __init__(self):
        self.state = {}

    def recommend(self, user_state):
        return "exercise: walking 30min"