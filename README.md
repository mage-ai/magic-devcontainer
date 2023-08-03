## Mage Streaming + dbt Demo Project

This project uses a sample topic— [the Google NYC Taxi Pubsub](https://github.com/googlecodelabs/cloud-dataflow-nyc-taxi-tycoon#public-pubsub-data-stream) to create a streaming pipeline in Mage that:

- Reads and transforms the stream
- Writes the stream as parquet to S3

Then, it creates a batch pipeline to:

- Read parquet files from S3 (using DuckDB 🤓).
- Execute a dbt model to store the raw data in a local Postgres instance.
- Execute a dbt model to transform the raw data to an SCD Type-2 table, logging the status updates for each ride.

## Set-up

**Prerequisites**

- Docker
- VSCode
- A GCP project for Pubsub setup & a service account
- An AWS account (or other cloud storage provider) to store the stream

Let's get started 🎉

1. `git clone https://github.com/mage-ai/pubsub-devcontainer-demo`
2. Configure the Google Cloud Pubsub topic using [these instuctions](https://github.com/googlecodelabs/cloud-dataflow-nyc-taxi-tycoon#public-pubsub-data-stream) for guidance. All that's required are: the `gcloud` CLI, a GCP account, and one command. You'll also need [a service account](https://cloud.google.com/iam/docs/service-accounts-create) for our Mage instance.
3. Copy your service account key json file to the root of the directory and rename it `google_secrets.json`.
4. Run the Pubsub stream with `gcloud alpha pubsub subscriptions create taxi-test-sub --topic projects/pubsub-public-data/topics/taxirides-realtime` in your terminal of choice.
5. Open the cloned file in VSCode.
6. Create a `.env` file with the requisite variables. See the `.env.example` file for guidance.
7. Select the prompt to "Reopen in Container" to start the devcontainer _or_ open the command prompt and select "Devcontainers: Rebuild and Reopen in Container." This will build a devcontainer (a Docker container) and install all dependencies to your project. This may take a few minutes.
8. Navigate to `localhost:6789` when the container is ready. You should see the Mage UI!

## Stream data from a Pubsub topic to S3

1. Navigate to the "Pipelines" tab in the Mage UI.
2. Two pipelines exist— `pub_sub_stream` and `dbt_demo`— click `pub_sub_stream` then the "code" icon in the top left to open the pipeline code.
3. Double check the config— these should pull from your `.env` file.
4. Click `Execute pipeline` in the bottom right to run your stream.

Nice! We've got a working stream. You can click `Cancel pipeline` after some sample data has been loaded or let the stream run. Don't forget to run `gcloud alpha pubsub subscriptions delete projects/verdant-current-393218/subscriptions/taxi-test-sub` to terminate your sample stream.

## Run dbt transformations

This container builds a postgres database alongside our Mage app for us to run transformations in dbt. Navigate to the `pipelines` page and select `dbt demo`. Select the code icon.

- The first cell reads in the data from our stream. Click the play icon or hit CMD + Enter to run.
- You might notice there are some tests in this cell— Mage incorporates _runtime tests_ to check the quality of your data. What tests are we running here?
- The next cell writes our data to a postgres table using `dbt`. Note how we can read from our mage data _directly_, without the need for an intermediate table.
- Finally, we apply a transform to build an [SCD Type-2](https://en.wikipedia.org/wiki/Slowly_changing_dimension#Type_2:_add_new_row) table from our dataset. This is also known as a "change-log" format.
- The final cell pulls a sample ride! Do the pickup, enroute, & dropoff times lineup?
