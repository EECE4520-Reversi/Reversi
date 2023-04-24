class User:
    """ Class representing user as stored in the database

    Methods:
        get_elo(): Returns user elo
        gain_elo(gain: int): Increments user elo by gain
        lose_elo(loss: int): Decrements user elo by loss
    """
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
