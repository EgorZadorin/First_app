from typing import List

from model.User import User
from model.Table import UserTable


def build_users_page(users: List[User]):
    table = UserTable(users, border=True)
    return table
