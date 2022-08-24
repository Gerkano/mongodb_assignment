from pymongo import MongoClient
from random_word import RandomWords
import logging
from statistics import mean
from random import random, randint, uniform


class FruitsAndClothes:
    def __init__(self) -> None: 
        self.client = MongoClient('localhost', 37017)
        self.db_fruits = self.client['fruits']
        self.db_clothes = self.client['clothes']
        self.collection_fruits = self.db_fruits['fruits_db']
        self.collection_clothes = self.db_clothes['clothes_db']
        # self.database = DatabaseFunctions(self.client)
        self.fruit_list = ["Apple", "Apricots", "Avocado", "Banana", "Grapefruit", "Guava", "Gooseberries", "Honeydew Melon",
"Jujube Fruit", "Kiwifruit", "Mandarin", "Mango", "Orange", "Pear", "Peaches", "Pitanga", "Plantain", "Prickly Pear", "Quince", "Raspberries"]
        self.r = RandomWords()
        self.log = logging.basicConfig(filename='logs_fruits_clothes.log', level=logging.DEBUG)

    def fruits(self) -> None:
        counter = []
        for i in range(0, randint(25,50)):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            random_color = (r,g,b)
            fruits = {"fruit": i, "cost": round(uniform(9.99, 99.99), 2), "size": round(uniform(9.99, 99.99), 2), "weight": round(uniform(9.99, 99.99)), "collor": random_color}    
            self.collection_fruits.insert_one(fruits)
            logging.debug(f'Fruits added to the database: {fruits}')
            counter.append(i)
        logging.debug(f'Fruits added to the database: {len(counter)}\n')

    def clothes(self) -> None:
        counter = []
        for i in range(0, randint(25,50)):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            random_color = (r,g,b)
            clothes = {"clothes": self.r.get_random_word(), "cost": round(uniform(9.99, 99.99), 2), "size": round(uniform(9.99, 99.99), 2), "weight": round(uniform(9.99, 99.99)), "collor": random_color}
            self.collection_clothes.insert_one(clothes)
            logging.debug(f'Clothes added to the database: {clothes}')
            counter.append(i)
        logging.debug(f'Clothes added to the database: {len(counter)}\n')

    def fruits_counter(self) -> str:
        list_fruits = [item for item in self.collection_fruits.find()]
        logging.debug(f"Our collected data count: {len(list_fruits)}")
        return f"Our collected data count: {len(list_fruits)}"

    def clothes_counter(self) -> str:
        list_clothes = [item for item in self.collection_clothes.find()]
        logging.debug(f"Our collected data count: {len(list_clothes)}")
        return f"Our collected data count: {len(list_clothes)}"

    def average_price_fruits(self) -> str:
        price_list = mean([i['cost'] for i in self.collection_fruits.find()])
        logging.debug(f"Average cost of fruits is: {round(price_list, 2)} $")
        return f"Average cost of fruits is: {round(price_list, 2)} $"
        
    def average_price_clothes(self) -> str:
        price_list = mean([i['cost'] for i in self.collection_clothes.find()])
        logging.debug(f"Average cost of clothes is: {round((price_list), 2)} $")
        return f"Average cost of clothes is: {round((price_list), 2)} $"
    
    def max_cost_fruit(self)-> str:
        price_list = max([i['cost'] for i in self.collection_fruits.find()])
        logging.debug(f"Highest cost of fruit is: {price_list} $")
        return f"Highest cost of fruit is: {price_list} $"

    def max_cost_clothes(self)-> str:
        price_list = max([i['cost'] for i in self.collection_clothes.find()])
        logging.debug(f"Highest cost of clothes is: {price_list} $")
        return f"Highest cost of clothes is: {price_list} $"

    def weight_fruit(self)-> str:
        weight_list = [i['weight'] for i in self.collection_fruits.find()]
        logging.debug(f"Heaviest fruit: {max(weight_list)} Kg, Lightest fruit: {min(weight_list)} Kg")
        return f"Heaviest fruit: {max(weight_list)} Kg\nLightest fruit: {min(weight_list)} Kg"
    
    def weight_clothes(self)-> str:
        weight_list = [i['weight'] for i in self.collection_clothes.find()]
        logging.debug(f"Heaviest clothing: {max(weight_list)} Kg, Lightest clothing: {min(weight_list)} Kg")
        return f"Heaviest clothing: {max(weight_list)} Kg\nLightest clothing: {min(weight_list)} Kg"

    def monetary_value_all(self)-> str:
        cost_all = round(sum([sum([i['cost'] for i in self.collection_fruits.find()]), sum([i['cost'] for i in self.collection_clothes.find()])]), 2)
        logging.debug(f"All fruits and clothes can be sold for: {cost_all} $")
        return f"All fruits and clothes can be sold for: {cost_all} $"

    def delete_all(self) -> None:
        self.collection_fruits.delete_many({})
        self.collection_clothes.delete_many({})

goods = FruitsAndClothes()
goods.fruits()
goods.clothes()
print(goods.fruits_counter())
print(goods.clothes_counter())
print(goods.average_price_fruits())
print(goods.average_price_clothes())
print(goods.max_cost_fruit())
print(goods.max_cost_clothes())
print(goods.weight_fruit())
print(goods.weight_clothes())
print(goods.monetary_value_all())
# goods.delete_all()


