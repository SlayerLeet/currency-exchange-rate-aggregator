from fastapi import APIRouter
from fastapi import HTTPException

from parser import main_parse


router = APIRouter()


@router.get("/data")
async def data():
    data = await main_parse()  # ✅ ждём результат
    return data

    

@router.get("/data/search_exchanges/{name_of_exchange}")
async def get_currencies_of_exchange(name_of_exchange: str):
    api_data = await main_parse()
    data = []
    for exchange in api_data:
        if exchange["exchange"] == name_of_exchange:
            data.append(exchange)
    if len(data) > 0:
        return data
    else:
        raise HTTPException(status_code=404, detail="Биржа не найдена")
    
@router.get("/data/search_currencies/{name_of_currency}")
async def get_currencies_of_name(name_of_currency: str):
    api_data = await main_parse()
    data = []
    for currency in api_data:
        if currency["name"][:3] == name_of_currency:
            data.append(currency)
    if len(data) > 0:
        return data
    else:
        raise HTTPException(status_code=404, detail="Валюта не найдена")

@router.get("/data/search_id/{id_of_currency}")
async def get_currencies_of_id(id_of_currency: int):
    api_data = await main_parse()
    for currency in api_data:
        if currency["id"] >= id_of_currency:
            return currency
    raise HTTPException(status_code=404, detail="Валюта не найдена")


# @router.post("/data/custom_pair")
# def create_pair(data: ):
    