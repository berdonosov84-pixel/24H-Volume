import requests
import pandas as pd
import traceback

URL = "https://fapi.binance.com/fapi/v1/ticker/24hr"

def main():
    try:
        print("Запрос к Binance...")

        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        rows = []
        for item in data:
            symbol = item["symbol"]

            if symbol.endswith("USDT"):
                volume = float(item.get("quoteVolume", 0))
                rows.append([symbol, volume])

        print(f"Получено {len(rows)} тикеров")

        df = pd.DataFrame(rows, columns=["Ticker", "Volume (USDT)"])
        df = df.sort_values(by="Volume (USDT)", ascending=False)

        # Сохраняем в CSV вместо Excel
        df.to_csv("binance_futures_volume.csv", index=False, encoding='utf-8-sig')

        print("Файл сохранён: binance_futures_volume.csv")

    except Exception as e:
        print("ОШИБКА:")
        traceback.print_exc()

    input("Нажми Enter для выхода...")

if __name__ == "__main__":
    main()