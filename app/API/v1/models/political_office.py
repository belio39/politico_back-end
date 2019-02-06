offices = []

class OfficesModel:
  def __init__(self, office_type, name):
    self.offices = offices
    self.office_type = office_type
    self.name = name

  def save(self, office_type, name):
    new_office = {
      "id": len(offices) +1,
      "office_type": office_type,
      "name": name,

    }
    offices.append(new_office)
    return new_office

