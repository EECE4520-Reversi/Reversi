class User:
    def __init__(self, username: str, password: str = None, elo: int = 0):
        self.username = username
        self.password = password
        self.elo = elo

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

    def getPassword(self):
        return self.password


def legalUsername(username):
    return username


def legalPassword(password):
    return password
