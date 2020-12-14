# Big Data Tweet Detection


Run Steps:


Open terminal

Start Zookeper Service:
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties

Start Kafka Service:
kafka-server-start /usr/local/etc/kafka/server.properties

Start ElasticSearch

cd /usr/local/Cellar/elasticsearch-full/7.10.0/bin && elasticsearch

Run program:
Go to the directory and execute 
spark-submit producer.py
Spark-submit consumer.py 

Dashboard:
http://localhost:5601/
 
