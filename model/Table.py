
from flask_table import Table, Col


class UserTable(Table):
    id = Col('Id')
    login = Col('Login')
