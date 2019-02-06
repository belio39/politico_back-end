users = []
admins = [
  {
    "first_name": "dennis",
    "last_name": "belio",
    "other_name": "rotich",
    "email": "belio@gmail.com",
    "phone_number": +254723624569,
    "isAdmin": True,
    }
]

class UsersModel:
  def __init__(self, first_name, last_name, other_name, email, phone_number, passport_url, password):
    self.first_name = first_name
    self.last_name = last_name
    self.other_name = other_name
    self.email = email
    self.phone_number = phone_number
    self.passport_url= passport_url
    self.password = password
    self.admins = admins

  def save(self, first_name, last_name, other_name, email, phone_number, passport_url, password):
    def isAdmin():
      for admin in admins:
        if email in admin.values():
          return True
        if phone_number in admin.values():
          return True
        else:
          return False
          
    new_user = {
      "id": len(users) +1,
      "first_name": first_name,
      "last_name": last_name,
      "other_name": other_name,
      "email": email,
      "phone_number": phone_number,
      "passport_url": passport_url,
      "password": password,
      "isAdmin": isAdmin()
    }
    users.append(new_user)
    return new_user

