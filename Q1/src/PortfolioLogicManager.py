from Q1.src.BondStorageSingleton import BondStorageSingleton

"""
PortfolioLogicManager: in charge of logic operations to to process portfolio

In the future can add multiple ways of calculating portfolio to this manager. Currently
only has one way to do the calculation.
"""
class PortfolioLogicManager(object):
    @staticmethod
    def calculatePortfolio(assets):
        valid_bonds, invalid_bond_ids = list(), list()

        portfolio_holding_value, portfolio_duration, portfolio_total_return = 0, 0, 0

        """ Loop through each asset, only keep bond that exists in database"""
        for asset_info in assets:
            id, units = asset_info["bondit_id"], asset_info["units"]
            bond = BondStorageSingleton.getInstance().get(id)

            if bond is None:
                invalid_bond_ids.append(id)
            else:
                portfolio_holding_value += bond.getPriceDirty() * units
                portfolio_duration += bond.getDuration() * (bond.getPriceDirty() * units)
                portfolio_total_return += bond.getYieldVal() * (bond.getPriceDirty() * units)

        """If none of the assets is valid, dividing by 0 will lead to error so this check is necessary"""
        if portfolio_holding_value > 0:
            normalized_portfolio_duration = portfolio_duration / portfolio_holding_value
            normalized_portfolio_total_return = portfolio_total_return / portfolio_holding_value
        else:
            normalized_portfolio_duration = 0
            normalized_portfolio_total_return = 0

        result = {
            "portfolio_holding_value": portfolio_holding_value,
            "normalized_portfolio_duration": normalized_portfolio_duration,
            "normalized_portfolio_total_return": normalized_portfolio_total_return,
        }

        error_msg = {
            "invalid_bond_ids": invalid_bond_ids,
        }

        return result, error_msg
