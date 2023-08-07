import confluent_kafka
import json
import time

if __name__ == '__main__':
    
    topic = 'magic-stream'
    producer = confluent_kafka.Producer({'bootstrap.servers': 'kafka:29092'})
    print('starting stream...')
    time.sleep(10)
    
    with open('./data/taxi-stream.json', 'r') as f:
        messages = json.load(f)

        for i, m in enumerate(messages):
            
            producer.produce(topic, json.dumps(m).encode('utf-8'))

            if i % 1000 == 0:
                print('Sent 1000 messages...')
                print("Flushing records...", flush=True)
                
                time.sleep(3)
                producer.flush()
                
    producer.flush()
    
  

