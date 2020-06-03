from Q1.src.BondStorageSingleton import BondStorageSingleton
from Q1.src.PortfolioLogicManager import PortfolioLogicManager

class MockServer(object):
    @staticmethod
    def startServer():
        BondStorageSingleton.getInstance().batchLoadCsv("bonds_trading_data.csv")

    @staticmethod
    def calculatePortfolio(json_request):
        result, error_msgs = PortfolioLogicManager.calculatePortfolio(json_request["assets"])
        return result, error_msgs
