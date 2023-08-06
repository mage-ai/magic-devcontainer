import confluent_kafka
import json
import time

if __name__ == '__main__':
    
    topic = 'magic-stream'
    producer = confluent_kafka.Producer({'bootstrap.servers': 'kafka:29092'})

    with open('./data/taxi-stream.json', 'r') as f:
        messages = json.load(f)

        for i in messages:
            producer.produce(topic, json.dumps(i).encode('utf-8'))
            time.sleep(.01)
            print(f'Sent message ' + i.get('ride_id'))

    print("Flushing records...")
    producer.flush()
            
    
  

