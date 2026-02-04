from parser import main_parse


async def post_custom_currency(id_of_currency_1: int, id_of_currency_2: int):
    
    for currency in await main_parse():
        if currency["id"] == id_of_currency_1:
            currency_1 = currency
        elif currency["id"] == id_of_currency_2:
            currency_2 = currency
        
    if currency_1 is None and currency_2 is None:
        return "Валюты не найдены" 
    elif currency_1 is None:
        return "Валюта 1 не найдена" 
    elif currency_2 is None:
        return "Валюта 2 не найдена" 
    else:
        return {"id_1": currency_1["id"],
                "id_2": currency_2["id"],
                "exchange_1": currency_1["exchange"],
                "exchange_2": currency_2["exchange"],
                "name" : currency_1["name"][:3] + "/" + currency_2["name"][:3],
                "price" : round(currency_1["price"] / currency_2["price"], 4),
                "date" : currency_1["date"]}

print(post_custom_currency(0,3))

