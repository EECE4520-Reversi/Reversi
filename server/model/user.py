class User:
    def __init__(self, username: str, password: str = None, elo: int = 0):
        self.username = username
        self.password = password
        self.elo = elo

    def get_elo(self):
        return self.elo

    def gain_elo(self, gain):
        self.elo = self.elo + gain

    def lose_elo(self, loss):
        self.elo = self.elo - loss

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "elo": self.elo,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        user = cls(
            data.get("username"),
            data.get("password"),
            data.get("elo"),
        )
        return user
