from datetime import datetime
def is_valid_symbol(symbol: str) -> bool:
    return symbol.isalpha() and symbol.isupper() and 1<= len(symbol) <=7

def is_valid_chat_type(chat_tpe :str) -> bool:
    return chat_tpe in ["1","2"]

def is_valid_time_series(ts:str)->bool:
    return ts in ["1","2","3","4"]

def is_valid_date(date_str:str)->bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False