users = []
admins = [
  {
    "firstname": "dennis",
    "lastname": "belio",
    "othername": "rotich",
    "email": "belio@gmail.com",
    "phonenumber": +254723624569,
    "isAdmin": True,
    }
]


class UsersModel:

    def __init__(self, firstname, lastname, othername, email,
                 phonenumber, passporturl, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phonenumber = phonenumber
        self.passporturl = passporturl
        self.password = password
        self.admins = admins

    def save(self, firstname, lastname, othername, email,
             phonenumber, passporturl, password):
        def isAdmin():
            for admin in admins:
                if email in admin.values():
                    return True
                if phonenumber in admin.values():
                    return True
                else:
                    return False

        new_user = {
          "id": len(users) + 1,
          "firstname": firstname,
          "lastname": lastname,
          "othername": othername,
          "email": email,
          "phonenumber": phonenumber,
          "passporturl": passporturl,
          "password": password,
          "isAdmin": isAdmin()
        }
        users.append(new_user)
        return new_user
