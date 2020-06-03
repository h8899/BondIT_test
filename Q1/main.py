import json

from Q1.src.MockServer import MockServer

if __name__ == "__main__":
    MockServer.startServer()

    f = open("portfolio_request.json", "r")
    json_request = json.load(f)
    f.close()

    result, err_msgs = MockServer.calculatePortfolio(json_request)

    """
    result: {
        'portfolio_holding_value': 104001323.00999999, 
        'normalized_portfolio_duration': 0.8459412259721022, 
        'normalized_portfolio_total_return': 0.0037964872334560126
        }
    """
    print(result)

    """
    err_msgs: {
        'invalid_bond_ids': 
            [11720, 12831, 12898, 13064, 13299, 13782, 14025, 17038, 17242, 20029, 20643, 21314, 22918, 24361, 103624, 109207, 112530, 116045, 117086, 118916, 119123, 120049]
    }
    """
    print(err_msgs)
