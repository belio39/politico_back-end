offices = [
  {
    "id" : 1,
    "officetype": "mp",
    "name": "kanu",

  }
]

class OfficesModel:
  def __init__(self):
    self.offices = offices


  def save(self, officetype, name):
    new_office = {
      "id": len(offices) +1,
      "officetype": officetype,
      "name": name,

    }
    offices.append(new_office)
    return new_office

  def single_office(self, id):
    return [office for office in offices if id in office.values()]

  def all_office(self):
    return offices  

    