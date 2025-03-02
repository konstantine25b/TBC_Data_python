import sys
import random
import logging
from uuid import uuid4
from KafkaProducer import KafkaProducer
from AvroSerializationManager import AvroSerializationManager
from Ecommerce import EcommerceOrder
from Config import producer_conf, schema_registry_url, auth_user_info
from confluent_kafka.serialization import SerializationContext, MessageField


def generate_random_order():
    customer_id = random.randint(1, 1000)  
    product_id = random.randint(100, 999)  
    price = random.uniform(10.0, 100.0)
    quantity = random.randint(1, 10) 
    order_status = random.choice(["Pending", "Shipped", "Delivered", "Canceled"])
    order_address = f"{random.randint(1, 999)} {random.choice(['Main St', 'Broadway', 'Elm St', 'Pine St'])}, {random.choice(['Springfield', 'Rivertown', 'Hillview'])}, {random.choice(['USA', 'Canada', 'UK'])}"
    return EcommerceOrder(customer_id, product_id, quantity, order_status, order_address, price)

sys.dont_write_bytecode = True
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

topic = "EcommerceOrder"
avro_manager = AvroSerializationManager(schema_registry_url, auth_user_info, topic, EcommerceOrder.to_dict)
string_serializer = avro_manager.string_serializer

if __name__ == "__main__":
    producer = KafkaProducer(producer_conf)
    
    try:
        while True:
            ecom_order_data = generate_random_order()
            serialized_key = string_serializer(str(uuid4()))
            serialized_value = avro_manager.avro_serializer(ecom_order_data(), SerializationContext(topic, MessageField.VALUE))

            print(ecom_order_data())

            producer.produce_message(
                topic=topic,
                message_key=serialized_key,
                message_value=serialized_value
            )
                            
    except KeyboardInterrupt:
        logging.info("Process interrupted by user.")
        producer.close()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        producer.close()