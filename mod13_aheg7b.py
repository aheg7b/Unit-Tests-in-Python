from datetime import datetime

def is_valid_symbol(symbol: str) -> bool:
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def is_valid_chat_type(chat_tpe: str) -> bool:
    return chat_tpe in ["1", "2"]

def is_valid_time_series(ts: str) -> bool:
    return ts in ["1", "2", "3", "4"]

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_valid_input(prompt, validator):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print("Invalid input, please try again.")

def main():
    symbol = get_valid_input("Please enter a stock symbol: ", is_valid_symbol)
    chart_type = get_valid_input("Please enter chart type (1 or 2): ", is_valid_chat_type)
    time_series = get_valid_input("Please enter time series (1-4): ", is_valid_time_series)
    start_date = get_valid_input("Please enter start date (YYYY-MM-DD): ", is_valid_date)
    end_date = get_valid_input("Please enter end date (YYYY-MM-DD): ", is_valid_date)
    print("\nAll inputs are valid!")
    print("Symbol:", symbol)
    print("Chart type:", chart_type)
    print("Time series:", time_series)
    print("Start date:", start_date)
    print("End date:", end_date)

if __name__ == "__main__":
    main()