class CatalogTable():
    def __init__(self, name):
        self.name = name

class Catalog():
    def __init__(self):
        self.tables = set()

    def add_table(self, table_name):
        table = CatalogTable(table_name)
        self.tables.add(table)
        return table


class Storage():
    pass