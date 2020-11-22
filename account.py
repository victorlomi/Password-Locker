class Account():
    """Store login information(username and password)"""

    def __init__(self, username='', password=''):
        """Store username and password"""
        self.username = username
        self.password = password