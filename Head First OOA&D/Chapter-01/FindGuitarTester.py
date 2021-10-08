class Guitar(object):
    def __init__(self, serial_number, price, builder, model, guitar_type,
                 back_wood, top_wood):
        self.__serial_number = serial_number
        self.__price = price
        self.__builder = builder
        self.__model = model
        self.__type = guitar_type
        self.__back_wood = back_wood
        self.__top_wood = top_wood

    def get_serial_number(self):
        return self.__serial_number

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_builder(self):
        return self.__builder

    def get_model(self):
        return self.__model

    def get_type(self):
        return self.__type

    def get_back_wood(self):
        return self.__back_wood

    def get_top_wood(self):
        return self.__top_wood


class Inventory(object):
    def __init__(self):
        self.guitar_list = []

    def add_guitar(self, serial_number, price, builder, model, guitar_type,
                   back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, guitar_type,
                        back_wood, top_wood)
        self.guitar_list.append(guitar)

    def search(self, guitar):
        nulls = [None, '']
        for item in self.guitar_list:
            builder = guitar.get_builder()
            if (builder not in nulls) and (builder != item.get_builder()):
                continue

            model = guitar.get_model()
            if (model not in nulls) and (model != item.get_model()):
                continue

            guitar_type = guitar.get_type()
            if (guitar_type not in nulls) and (guitar_type != item.get_type()):
                continue

            back_wood = guitar.get_back_wood()
            if (back_wood not in nulls) and (back_wood != item.get_back_wood()):
                continue

            top_wood = guitar.get_top_wood()
            if (top_wood not in nulls) and (top_wood != item.get_top_wood()):
                continue

        return None


def initialize_inventory(inventory):
    # Add guitars to the inventoy
    inventory.add_guitar("11277", 3999.95, "Collings", "CJ", "acoustic",
                         "Indian Rosewood", "Sitka")
    inventory.add_guitar("V95693", 1499.95, "Fender", "Stratocastor",
                         "electric", "Alder", "Alder")
    inventory.add_guitar("V9512", 1549.95, "Fender", "Stratocastor", "electric",
                         "Alder", "Alder")
    inventory.add_guitar("122784", 5495.95, "Martin", "D-18", "acoustic",
                         "Mahogany", "Adirondack")
    inventory.add_guitar("76531", 6295.95, "Martin", "OM-28", "acoustic",
                         "Brazilian Rosewood", "Adriondack")
    inventory.add_guitar("70108276", 2295.95, "Gibson", "Les Paul", "electric",
                         "Mahogany", "Maple")
    inventory.add_guitar("82765501", 1890.95, "Gibson", "SG '61 Reissue",
                         "electric", "Mahogany", "Mahogany")
    inventory.add_guitar("77023", 6275.95, "Martin", "D-28", "acoustic",
                         "Brazilian Rosewood", "Adirondack")
    inventory.add_guitar("1092", 12995.95, "Olson", "SJ", "acoustic",
                         "Indian Rosewood", "Cedar")
    inventory.add_guitar("566-62", 8999.95, "Ryan", "Cathedral", "acoustic",
                         "Cocobolo", "Cedar")
    inventory.add_guitar("6 29584", 2100.95, "PRS", "Dave Navarro Signature",
                         "electric", "Mahogany", "Maple")


if __name__ == '__main__':
    inventory = Inventory()
    initialize_inventory(inventory)

    what_erin_likes = Guitar('', 0, "fender", "Stratocastor", "electric",
                             "Alder", "Alder")

    guitar = inventory.search(what_erin_likes)
    if guitar is not None:
        print('Erin, you might like this {0} {1} {2} guitar:\n  {3} back '
              'and sides,\n  {4} top.\nYou can have it for only {5}!'.format(
                guitar.get_builder(), guitar.get_model(),
                guitar.get_type(), guitar.get_back_wood(),
                guitar.get_top_wood(), guitar.get_price()))
    else:
        print('Sorry, Erin, we have nothing for you.')
