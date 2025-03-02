from datetime import datetime
from typing import Dict, Union, List
import logging

class EcommerceOrder:
    def __init__(self, customer_id: int, product_id: int, quantity: int, order_status: str, order_address: str, price: float):
        self.customer_id = customer_id
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.order_status = order_status  
        self.order_address = order_address
    
    def __call__(self) -> Dict[str, Union[str, int, float, List[Dict[str, Union[str, int]]]]]:
        ecomm_info = {
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
            "order_time": self.order_time,
            "order_status": self.order_status,
            "order_address": self.order_address,
        }
        return ecomm_info

    @staticmethod
    def to_dict(data, ctx) -> Dict[str, Union[int, str, float]]:
        return {
            "customer_id": data.get("customer_id"),
            "product_id": data.get("product_id"),
            "price": data.get("price"),
            "quantity": data.get("quantity"),
            "order_time": data.get("order_time"),
            "order_status": data.get("order_status"),
            "order_address": data.get("order_address"),
            
        }