import json

from Q1.src.MockServer import MockServer

if __name__ == "__main__":
    MockServer.startServer()

    f = open("portfolio_request.json", "r")
    json_request = json.load(f)
    f.close()

    result, err_msgs = MockServer.calculatePortfolio(json_request)

    """
    result: {'portfolio_holding_value': 30288000.0, 'normalized_portfolio_duration': 0.01, 'normalized_portfolio_total_return': 0.05770635235076598}
    """
    print(result)

    """
    err_msgs: {'invalid_bond_ids': [12898, 12976, 13064, 13299, 13669, 13699, 13782, 14025, 17038, 17242, 20029, 21314, 109207, 112530, 116045, 117086, 118916, 119123, 120049]}
    """
    print(err_msgs)
