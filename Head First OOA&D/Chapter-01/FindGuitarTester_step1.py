from enum import Enum


class Type(Enum):
    ACOUSTIC = 'acoustic'
    ELECTRIC = 'electric'

    def __str__(self):
        return self.value


class Builder(Enum):
    FENDER = 'Fender'
    MARTIN = 'Martin'
    GIBSON = 'Gibson'
    COLLINGS = 'Collings'
    OLSON = 'Olson'
    RYAN = 'Ryan'
    PRS = 'PRS'
    ANY = 'Any'

    def __str__(self):
        return self.value


class Wood(Enum):
    INDIAN_ROSEWOOD = 'Indian Rosewood'
    BRAZILIAN_ROSEWOOD = 'Brazilian Rosewood'
    MAHOGANY = 'Mahogany'
    MAPLE = 'Maple'
    COCOBOLO = 'Cocobolo'
    CEDAR = 'Cedar'
    ADIRONDACK = 'Adirondack'
    ALDER = 'Alder'
    SITKA = 'Sitka'

    def __str__(self):
        return self.value


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

    def search(self, search_guitar):
        matching_guitars = []
        for guitar in self.guitar_list:
            if search_guitar.get_builder() != guitar.get_builder():
                continue
            model = search_guitar.get_model().lower()
            if (model not in [None, '']) and (
                    model != guitar.get_model().lower()):
                continue

            if search_guitar.get_type() != guitar.get_type():
                continue

            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue

            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue

            matching_guitars.append(guitar)

        return matching_guitars


def initialize_inventory(inventory):
    # Add guitars to the inventory
    inventory.add_guitar("1177", 3999.95, Builder.COLLINGS, "CJ", Type.ACOUSTIC,
                         Wood.INDIAN_ROSEWOOD, Wood.SITKA)
    inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocastor",
                         Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("V9512", 1549.95, Builder.FENDER, "Stratocastor",
                         Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("122784", 5495.95, Builder.MARTIN, "D-18",
                         Type.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK)
    inventory.add_guitar("76531", 6295.95, Builder.MARTIN, "OM-28",
                         Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD,
                         Wood.ADIRONDACK)
    inventory.add_guitar("70108276", 2295.95, Builder.GIBSON, "Les Paul",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY)
    inventory.add_guitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY)
    inventory.add_guitar("7023", 6275.95, Builder.MARTIN, "D-28", Type.ACOUSTIC,
                         Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK)
    inventory.add_guitar("1092", 12995.95, Builder.OLSON, "SJ", Type.ACOUSTIC,
                         Wood.INDIAN_ROSEWOOD, Wood.CEDAR)
    inventory.add_guitar("566-62", 8999.95, Builder.RYAN, "Cathedral",
                         Type.ACOUSTIC, Wood.COCOBOLO, Wood.CEDAR)
    inventory.add_guitar("6 29584", 2100.95, Builder.PRS, "Dave Navarro "
                                                          "Signature",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE)


if __name__ == '__main__':
    inventory = Inventory()
    initialize_inventory(inventory)

    what_erin_likes = Guitar('', 0, Builder.FENDER, "Stratocastor",
                             Type.ELECTRIC, Wood.ALDER, Wood.ALDER)

    matching_guitars = inventory.search(what_erin_likes)
    if len(matching_guitars) != 0:
        print('Erin, you might like these guitars')
        for guitar in matching_guitars:
            print('We have a {0} {1} {2} guitar:\n    {3} back and sides,\n    '
                  '{4} top.\nYou can have it for only {5}!\n  ------'.format(
                    guitar.get_builder(), guitar.get_model(),
                    guitar.get_type(), guitar.get_back_wood(),
                    guitar.get_top_wood(), guitar.get_price()))
    else:
        print('Sorry, Erin, we have nothing for you.')
