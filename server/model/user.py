class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.elo = 0
        self.games = []

    def register(self, username, password):
            if legalUsername(username):
                 self.username = username
            if legalPassword(password):
                 self.password = password
    
    def to_dict(self):
         return {
              "_username" : self.username,
              "password" : self.password,
              "elo" : self.elo,
              "games" : self.games
         }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        user = cls(
            data.get("_username"),
            data.get("password"),
            data.get("elo"),
            # UNSURE IF WORKS 
            # data.get("games"),
        )
        return user
def legalUsername(username):
    return username
    
def legalPassword(password):
    return password

