## 🎏 Mage Streaming + dbt Demo Project

This project uses sample data from [the Google NYC Taxi Pubsub](https://github.com/googlecodelabs/cloud-dataflow-nyc-taxi-tycoon#public-pubsub-data-stream) to create a streaming pipeline in Mage that:

- Reads and transforms the stream
- Writes the stream as parquet to S3

Then, it creates a batch pipeline to:

- Read parquet files from S3.
- Execute a dbt model to store the raw data in a local Postgres instance.
- Execute a dbt model to transform the raw data to an SCD Type-2 table, logging the status updates for each ride.

<p align="center">
<img src="https://github.com/mage-ai/pubsub-devcontainer-demo/assets/59450879/e6605722-ea32-4784-af71-6336e67e00a2"></img>
</p>

## 🛠️ Configuration

**Prerequisites**

- Docker
- VSCode
- An AWS account (or other cloud storage provider) to store the stream

Let's get started 🎉

1. `git clone https://github.com/mage-ai/pubsub-devcontainer-demo`
2. Open the cloned file in VSCode.
3. Create a `.env` file with the requisite variables. See the `.env.example` file for guidance.
4. Select the prompt to `reopen in Container` to start the devcontainer _or_ open the command prompt and select `Devcontainers: Rebuild and Reopen in Container`. This will build a devcontainer (a Docker container) and install all dependencies to your project. This may take a few minutes.
5. Navigate to `localhost:6789` when the container is ready. You should see the Mage UI!

## 🙋‍♂️ Wait, what's happening?

![Architecture Diagram](/assets/magic-devcontainer.png)

By performing the above, VSCode is creating an isolated environment, installing a few extensions + building and running Docker as defined in `docker-compose.yaml`. 

We're using [Devcontainers](https://containers.dev/) to create a consistent development environment for our project. This means that we can be sure that our code will run in the same environment as our teammates and that we can easily share our code with others.

As for the stream itself, you might notice `kafka` and `zookeeper` in the `docker-compose.yaml` file. These are the tools we use to manage the stream. 

We're using `kafka` to manage the stream and `zookeeper` to manage `kafka`. You can read more about these tools [here](https://kafka.apache.org/).

The _acutal_ stream is managed by the `stream` container, which spins up a python container and executes `./stream/bin/send_stream.py`— this is the script that reads from the pubsub topic data (`./stream/data/taxi-stream.json`).

Data will begin streaming 30 seconds after the container starts.

## 🤓 Stream data from a dummy source to S3

1. Navigate to the "Pipelines" tab in the Mage UI.
2. Two pipelines exist— `kafka_demo` and `dbt_demo`— click `kafka_demo` then the "code" icon in the top left to open the pipeline code.
3. Double check the config— these should pull from your `.env` file.
4. Click `Execute pipeline` in the bottom right to run your stream. You should see data flowing!

<p align="center">
<img src="https://github.com/mage-ai/magic-devcontainer/assets/59450879/2adb9171-30ed-4097-924d-be83b355d822"></img>
</p>

Nice! We've got a working stream. You can click `Cancel pipeline` after some sample data has been loaded or let the stream run.

Behind the scenes, we're kicking off a Kafka + Zookeeper instance, creating a topic, and writing data to that topic. Mage is then pulling in this "simulated" stream, transforming it, and writing to S3!

## 🧱 Run dbt transformations

This container builds a postgres database alongside our Mage app for us to run transformations in dbt. Navigate to the `pipelines` page and select `dbt demo`. Select the code icon.

- The first cell reads in the data from our stream (stored in s3 or your cloud provider of choice). Click the play icon or hit CMD + Enter to run.
- You might notice there are some tests in this cell— Mage incorporates _runtime tests_ to check the quality of your data. What tests are we running here?
- The next cell writes our data to a postgres table using `dbt`. Note how we can read from our mage data _directly_, without the need for an intermediate table.
- Finally, we apply a transform to build an [SCD Type-2](https://en.wikipedia.org/wiki/Slowly_changing_dimension#Type_2:_add_new_row) table from our dataset. This is also known as a "change-log" format.
- The final cell pulls a sample ride! Do the pickup, enroute, & dropoff times lineup?
