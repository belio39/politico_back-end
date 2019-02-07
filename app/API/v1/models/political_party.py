partys = []

class PartysModel:
  def __init__(self):
    self.partys = partys
  def save(self, name, hq_address, logo_url):
    new_party = {
      "party_id": len(self.partys) +1,
      "name": name,
      "hq_address": hq_address,
      "logo_url": logo_url,
    }
    partys.append(new_party)
    return new_party

  def get_single_party(self, party_id):
    return [party for party in partys if party_id in party.values()]

