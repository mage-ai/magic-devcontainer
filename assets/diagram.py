from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.onprem.analytics import Dbt
from diagrams.onprem.container import Docker
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import Postgresql
from diagrams.programming.language import Python
from diagrams.oci.database import Stream

graph_attr = {
    "fontsize": "45",
    "charset": "UTF-8",
    "fontcolor": "black",
    "color": "black",
    "margin":"-2, -2"
}

with Diagram(filename="magic-devcontainer", direction="LR", graph_attr=graph_attr):
  s3 = S3("S3")
  with Cluster("devcontainer"):
    with Cluster("Docker"):
      kafka = Kafka("Kafka")
      db = Postgresql("Postgres")
      python = Python("Producer")
      taxi = Custom("Taxi data", "./img/car.png")
      with Cluster("Mage 🧙🏻‍♂️"):
        batch = Dbt("Batch pipeline")
        stream = Stream("Streaming pipeline")

  [taxi, kafka] >> python
  python >> stream >> s3
  s3 >> batch >> db

        
        
        
