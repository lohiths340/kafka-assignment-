![image](../images/confluent-logo-300-2.png)
  
# Documentation
A project which implements a real-time order processing system that ingests order data from a simulated REST API using kafka, processes and enriches the data, and stores it in a postgreSQL database using kafka connect. The system runs on docker compose.

Prerequisites:-<br> 
1.Docker and Docker Compose <br> 
2.Python (with kafka library for producer/consumer testing)<br> 
3.Git<br> 
<br> 
System Architecture:-<br> 
1.Kafka: Handles streaming of order data.<br> 
2.Kafka connect: Enables integration between kafka and postgreSQL.<br> 
3.PostgreSQL: Stores the processed order data.<br> 
4.REST API Simulation: Produces real-time order events via HTTP.<br> 
5.Docker compose: Manages the system components.<br> 
<br> 
Setup Instructions<br> 
1.Clone the repository<br> 
2.Start docker containers: Using docker compose to set up kafka, kafka Connect, and postgreSQL<br> 
docker-compose up -d<br> 
<br> 
3.Deploying Kafka Connectors<br> 
HTTP Source Connector:<br> 
curl -X POST -H "Content-Type: application/json" --data @http-source-connector.json http://localhost:8083/connectors<br> 
<br> 
PostgreSQL Sink Connector:<br> 
curl -X POST -H "Content-Type: application/json" --data @postgres-sink-connector.json http://localhost:8083/connectors<br> 
<br> 
4.Running the Kafka consumer<br> 
python consumer.py<br> 
<br> 
5.Accessing the postgreSQL database container <br> 
docker exec -it postgres psql -U user -d orders<br> 
You can run a query to see the records:-<br> 
SELECT * FROM enriched_orders;<br> 
<br> 





You can find the documentation and instructions for this repo at [https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html](https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html?utm_source=github&utm_medium=demo&utm_campaign=ch.examples_type.community_content.cp-all-in-one)
