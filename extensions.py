import requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass


class ValuesConvertor:
    @staticmethod
    def get_price( quote: str, base: str, amount: str,):
        if quote == base:
            raise ConvertionExeption(f'невозможно перевести одтнаковые валюты {base}.')
        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'не удалось обработать валюту {quote}')
        
        try:
            base_ticket = keys[base]
        except KeyError:
            raise ConvertionExeption(f'не удалось обработать валюту {base}')
        
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'не удолось обработать количество{amount}.')
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        total_base = ((json.loads(r.content)[keys[base]])*(float(amount)))
        return total_base
