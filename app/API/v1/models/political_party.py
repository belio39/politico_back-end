partys = [{
      "id" : 1,
      "name" : "deni",
      "hq_address" : "kenya",
      "logo_url": "logo_url",
}]

class PartysModel:
  def __init__(self, name, hq_address, logo_url):
    self.partys = partys
    self.name = name
    self.hq_address = hq_address
    self.logo_url = logo_url

  def save(self, name, hq_address, logo_url):
    new_party = {
      "id": len(self.partys) +1,
      "name": name,
      "hq_address": hq_address,
      "logo_url": logo_url,
    }  
    partys.append(new_party)
    return new_party
