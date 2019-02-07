offices = []

class OfficesModel:
  def __init__(self):
    self.offices = offices
    

  def save(self, office_type, name):
    new_office = {
      "id": len(offices) +1,
      "office_type": office_type,
      "name": name,

    }
    offices.append(new_office)
    return new_office

  def single_office(self, id):
    return [office for office in offices if id in office.values()]

    