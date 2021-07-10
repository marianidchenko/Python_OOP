import re
pattern = r"^(?=.*?\d)(?=.*?[A-Z])[\w+*&#@$%^]{8,}$"


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not re.match(pattern, value):
            raise ValueError("The password must be 8 or more characters with "
                             "at least 1 digit and 1 uppercase letter.")
        else:
            self.__password = value

    def __str__(self):
        encoded_password = "*" * len(self.__password)
        return f"You have a profile with username: \"{self.__username}\" and password: {encoded_password}"


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)