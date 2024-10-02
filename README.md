![image](../images/confluent-logo-300-2.png)
  
# Documentation
This project implements a real-time order processing system that ingests order data from a simulated REST API using kafka, processes and enriches the data, and stores it in a postgreSQL database using kafka Connect. The system runs on docker compose.

Prerequisites:-
1.Docker and Docker Compose
2.Python (with kafka library for producer/consumer testing)
3.Git

System Architecture:-
1.Kafka: Handles streaming of order data.
2.Kafka connect: Enables integration between kafka and postgreSQL.
3.PostgreSQL: Stores the processed order data.
4.REST API Simulation: Produces real-time order events via HTTP.
5.Docker Compose: Manages the system components.

Setup Instructions
1.Clone the repository
2.Start docker containers: Using docker compose to set up kafka, kafka Connect, and postgreSQL
docker-compose up -d
3.Deploying Kafka Connectors
HTTP Source Connector:
curl -X POST -H "Content-Type: application/json" --data @http-source-connector.json http://localhost:8083/connectors
PostgreSQL Sink Connector:
curl -X POST -H "Content-Type: application/json" --data @postgres-sink-connector.json http://localhost:8083/connectors
4.Running the Kafka consumer
python consumer.py
5.Accessing the postgreSQL database container 
docker exec -it postgres psql -U user -d orders
You can run a query to see the records:-
SELECT * FROM enriched_orders;






You can find the documentation and instructions for this repo at [https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html](https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html?utm_source=github&utm_medium=demo&utm_campaign=ch.examples_type.community_content.cp-all-in-one)
