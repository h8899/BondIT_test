import csv

from Q1.src.Bond import Bond

"""
BondStorageSingleton: manage the bonds information (loaded from CSV file).

SingletonDesignPattern is used because:
- We want only a single instance that stores all the bonds, and other methods can easily access this manager without
passing this around as parameter

- We prefer SingletonDesignPattern over static class because for this data is stored in heap and disposable/ clonable
while static class is stored in stack (which is more limited if bonds data is big) and not disposable/ clonable.

"""
class BondStorageSingleton(object):
    __instance = None

    @staticmethod
    def getInstance():
        """ Method for retrieveing the singleton instance if already exists"""
        if BondStorageSingleton.__instance == None:
            BondStorageSingleton()
        return BondStorageSingleton.__instance

    def __init__(self):
        self.__bonds = dict()
        BondStorageSingleton.__instance = self

    def get(self, id):
        return self.__bonds.get(id, None)

    def set(self, id, bond):
        # TODO: Clarify if we allow to overwrite the old data (by id)
        """ Defensive programming: Type check """
        if (isinstance(bond, Bond) is False):
            raise Exception("Set invalid object to bond storage")
            return
        self.__bonds[id] = bond

    def checkValidBondInput(self, row):
        return row["bond_id"] != "null" and row["price_dirty"] != "null" \
            and row["yield"] != "null" and row["duration"] != "null"

    def batchLoadCsv(self, csv_file_path):
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                if self.checkValidBondInput(row):
                    bond_obj = Bond(
                        int(row["bond_id"]), float(row["price_dirty"]),
                        float(row["yield"]), float(row["duration"]),
                    )
                    self.set(int(row["bond_id"]), bond_obj)
        csv_file.close()
