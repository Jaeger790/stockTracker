#imports
from polygon import RESTClient
import csv


client = RESTClient("mZXdYhjKZkUldzr9imLPyuATSryrOlFS")

aggs = client.get_aggs(
        "GME",
        1,
        "day",
        "2023-04-14",
        "2023-04-14",
        )

with open ('gmeData.json','w', newline='') as file:
    stockwriter = csv.writer(file)
    stockwriter.writerow(aggs)


print(aggs)


