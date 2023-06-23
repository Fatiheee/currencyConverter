import requests
import json

cvfrom = input("Bozulan döviz türü: ")
cvto = input("Alınan döviz turu: ")
amount = input(f"Ne kadar {cvfrom} bozdurmak istiyorsunuz: " )

headers= {
  "apikey": "7QFNWaT06cjBcsJEmeyABnBuBothk9mF"
}
url = "https://api.apilayer.com/exchangerates_data/convert?to=" + cvto + "&from=" + cvfrom + "&amount=" + amount

result = requests.get(url, headers=headers)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(cvfrom, result["info"]["rate"], cvto))
print("{0} {1} = {2} {3}".format(amount, cvfrom, result["result"], cvto))

