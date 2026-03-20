import requests
import pandas as pd

URL = "https://fapi.binance.com/fapi/v1/ticker/24hr"

def main():
    response = requests.get(URL)
    data = response.json()

    rows = []
    for item in data:
        symbol = item["symbol"]
        if symbol.endswith("USDT"):
            volume = float(item["quoteVolume"])
            rows.append([symbol, volume])

    df = pd.DataFrame(rows, columns=["Ticker", "Volume (USDT)"])
    df = df.sort_values(by="Volume (USDT)", ascending=False)

    df.to_excel("binance_futures_volume.xls", index=False)
    print("Готово: binance_futures_volume.xls")

if __name__ == "__main__":
    main()