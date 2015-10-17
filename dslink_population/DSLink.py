from dslink.DSLink import Configuration
from dslink.DSLink import DSLink
from dslink.Node import Node
import hammock


class PopulationDSLink(DSLink):
    def __init__(self):
        super().__init__(Configuration("Population", responder=True))
        self.countries = Node("Countries", self.super_root)

        self.hammock = hammock.Hammock("http://api.population.io/1.0")
        countries = self.hammock.countries().GET(headers={"Content-Type": "application/json"}).json()["countries"]
        for country in countries:
            country_node = Node(country, self.countries)
            self.countries.add_child(country_node)

        self.super_root.add_child(self.countries)
