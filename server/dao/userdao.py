from dao.basedao import BaseDao
from model.user import User

class UserDao:
    def __init__(self):
        self.collection = "user"

    def save_user(self, user: User):
        BaseDao().db[self.collection].replace_one(
            {"_username": User.username}, user.to_dict(), upsert=True
        )

    def fetch_users(self):
        return BaseDao().db[self.collection].find()
    
    def fetch_specific_user(self, username):
        return BaseDao().db[self.collection].find_one({"_username" : username})