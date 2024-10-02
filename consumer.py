from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer('orders', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for message in consumer:
    order = message.value
    quantity = order.get('quantity', 0)
    price = order.get('price', 0)

    if quantity > 0 and price > 0:
        total_value = quantity * price
        order['total_value'] = total_value
        producer.send('enriched_orders', value=order)
    else:
        producer.send('invalid_orders', value=order)
