class User:
    def __init__(self, username, PFP, age_range, gender, admin = False):
        self._username = username
        self._PFP = PFP
        self._age_range = age_range
        self._gender = gender
        self._admin = admin

########################################################################################## Getters
        
    @property
    def username(self):
        return self._username
    @property
    def PFP(self):
        return self._PFP
    @property
    def age_range(self):
        return self._age_range
    @property
    def gender(self):
        return self._Gender
    @property
    def admin(self):
        return self._admin
    
################################################################### Setters

    @username.setter
    def username(self, value):
        self._username = value
    @PFP.setter
    def PFP(self, value):
        self._PFP = value
    @age_range.setter
    def age_range(self, value):
        self._age_range = value
    @gender.setter
    def gender(self, value):
        self._gender = value
    @admin.setter
    def admin(self, value):
        self._admin = value

    def __str__(self):
        if self._admin == True:
            print(f"{self._username} is a admin")
        else:
            print(f"{self._username} is not a admin")
        return ""


########################################### Main TEST

User1 = User("Sillyman", "pic", "8-10", "Male")
print(User1.username)
print(User1.age_range)
User1.username = "Johnny"
print(User1.username)
print(User1)