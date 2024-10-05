from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    order = message.value
    order_id = order['order_id']
    product_name = order['product_name']
    quantity = order['quantity']
    price = order['price']
    
    if quantity > 0 and price > 0:
        order_value = quantity * price
        enriched_order = {
            'order_id': order_id,
            'product_name': product_name,
            'quantity': quantity,
            'price': price,
            'total_value': order_value
        }
        producer.send('enriched_orders', value=enriched_order)
    else:
        producer.send('invalid_orders', value=order)
