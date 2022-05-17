class UserName:
    id = None
    name = None

    def __init__(self, user):
        if user.isdigit():
            self.id = user
        else:
            if not user.startswith("@"):
                self.name = "@{0}".format(user)
            else:
                self.name = user

    def get_user_id(self):
        if self.id:
            return self.id
        else:
            return self.name

    def to_string(self):
        if self.name:
            return self.name
        else:
            return self.id
