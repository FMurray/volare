from libs.catalog import Catalog
from libs.catalog.main import CatalogTable
import pickle

def test_catalog_init():
    cat = Catalog()
    assert cat.tables == set(), "Catalog should be initialized with an empty set of tables"

def test_catalog_add_table():
    cat = Catalog()
    cat.add_table("table1")
    assert pickle.dumps(cat.tables) == pickle.dumps({CatalogTable("table1")}), "Catalog should add a table to its set of tables"