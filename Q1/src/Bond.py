"""
Bond object
"""
class Bond(object):
    __id = None
    __price_dirty = None
    __yield_val = None
    __duration = None

    def __init__(self, id, price_dirty, yield_val, duration):
        self.__id = id
        self.__price_dirty = price_dirty
        self.__yield_val = yield_val
        self.__duration = duration

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getPriceDirty(self):
        return self.__price_dirty

    def setPriceDirty(self, price_dirty):
        self.__price_dirty = price_dirty

    def getYieldVal(self):
        return self.__yield_val

    def setYieldVal(self, yield_val):
        self.__yield_val = yield_val

    def getDuration(self):
        return self.__duration

    def setDuration(self, duration):
        self.__duration = duration
