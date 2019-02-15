partys = [{
      "id": 1,
      "name": "deni",
      "headquateraddress": "kenya",
      "logo_url": "logo_url",
}]


class PartysModel:

    def __init__(self):
        self.partys = partys

    def save(self, name, headquateraddress, logo_url):
        new_party = {
          "party_id": len(self.partys) + 1,
          "name": name,
          "headquateraddress": headquateraddress,
          "logo_url": logo_url,
        }
        partys.append(new_party)
        return new_party

    def get_single_party(self, party_id):
        return [party for party in partys if party_id in party.values()]

    def get_all_party(self):
        return self.partys

    def patch_party(self, party_id, name):
        for party in self.partys:
            if party_id in party.values():
                def update(find_key, new_value):
                    for key in party:
                        if key == find_key:
                            party[key] = new_value
                update("party_id", party_id)
                update("name", name)
                return party

    def delete_single_party(self, party_id):
        for party in self.partys:
            if party_id in party.values():
                self.partys.remove(party)
                return {"message": "Party deleted successfully."}
