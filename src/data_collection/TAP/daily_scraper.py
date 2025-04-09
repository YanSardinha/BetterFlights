import requests
import pandas as pd
import json

with requests.Session() as session:
    url = "https://www.flytap.com/api/calendar?functionName=calendar"
    
    all_responses = []

    for i in range(12):
        body = {
            "cabinClass": "E",
            "destination": "DUB",
            "market": "BR",
            "month": i + 1,
            "origin": "PMW",
            "paxType": "ADT",
            "payWithMiles": False,
            "starAlliance": False,
            "tripType": "R",
            "year": "2025"
        }
        
        try:
            response = session.post(url, json=body)
            
            response.raise_for_status()
            
            all_responses.append({
                "month": i + 1,
                "status_code": response.status_code,
                "data": response.json().get('data', {}).get('bestPriceForDates', [])
            })

        except requests.exceptions.HTTPError as errh:
            print(f"Erro HTTP para o mês {i+1}: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Erro ao fazer a requisição para o mês {i+1}: {err}")

prices_data = []

for response in all_responses:
    for item in response['data']:
        price_info = {
            "departureDate": item.get("departureDate"),
            "departureAirport": item.get("departureAirport"),
            "arrivalAirport": item.get("arrivalAirport"),
            "bestTotalPrice": item.get("bestTotalPrice"),
            "currency": item.get("currency"),
            "cabinClass": item.get("cabinClass")
        }
        prices_data.append(price_info)

df = pd.DataFrame(prices_data)

# TODO: Remover outliers, como por exemplo bestTotalPrice vazios
print(df.head())

min_price = df['bestTotalPrice'].min()
print(f"O menor preço encontrado foi: R${min_price}")

avg_price_by_date = df.groupby('departureDate')['bestTotalPrice'].mean().reset_index()
print("\nMédia de preço por data de partida:")
print(avg_price_by_date)

cheapest_by_airport = df.loc[df.groupby('departureAirport')['bestTotalPrice'].idxmin()]
print("\nPreço mais barato por aeroporto de partida:")
print(cheapest_by_airport[['departureAirport', 'bestTotalPrice', 'departureDate']])

with open('flight_prices.json', 'w') as f:
    json.dump(prices_data, f, indent=4)

df.to_csv('flight_prices.csv', index=False)
