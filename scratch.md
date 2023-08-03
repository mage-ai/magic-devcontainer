<img src="https://github.com/mage-ai/mage-ai/assets/59450879/5ea17901-b85b-4205-8f35-9cbfedfed99c" width="500" />

## What's Changed
### 🎉 Exciting New Features

#### 🤖 Create blocks and documentation using LLMs

Block Creation

<img src="https://github.com/mage-ai/mage-ai/assets/59450879/bd7aaf82-a162-4546-9bef-f4eb1d2b6892" width="600" />

Document Generation

<img src="https://github.com/mage-ai/mage-ai/assets/1066980/112790d5-ef16-45c1-a537-a47d678b952d" width="600" />

From the following PRs:
* Generate block using AI by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3095
* Generate documentation using AI by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3105
* Generate pipeline(multiple blocks) template from description by @matrixstone in https://github.com/mage-ai/mage-ai/pull/3103
* Create model and API endpoint for global data products by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3135

#### Enable batch upload for Snowflake destination

Leveraging `write_pandas` in the `snowflake-connector-python` library, this feature enhances the speed of batch uploads using Snowflake destinations 🤯 _by @csharplus in https://github.com/mage-ai/mage-ai/pull/2896_

#### Auto-delete logs after retention period

Now, Mage can auto-remove logs after your retention period expires! 

```yml
logging_config:
    retention_period: '15d'
```

or 

```bash
mage clean-old-logs k8s_project
```

_by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3139_

#### MongoDB destination support (data integration)

MongoDB is now supported as a destination! 🎉 _by @Luishfs in https://github.com/mage-ai/mage-ai/pull/3084_

#### Pipeline-level concurrency

It's now possible to configure concurrency at the pipeline level:

```yml
concurrency_config:
  block_run_limit: 1
  pipeline_run_limit: 1
```

_by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3112_

#### New add-block flow

![image](https://github.com/mage-ai/mage-ai/assets/59450879/5e9512d0-9993-470e-adcb-673345343224)

Mage's UI has been improved to feature a _new_ add-block flow! _by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3094_

#### Custom k8s executors

Mage now support custom k8s executor configuration:

```yml
k8s_executor_config:
  service_account_name: mageai
  job_name_prefix: "{{ env_var('KUBE_NAMESPACE') }}"
  container_config:
    image: mageai/mageai:0.9.7
    env:
    - name: USER_CODE_PATH
      value: /home/src/k8s_project
```

_by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3127_

#### Custom s3 `endpoint_url` in logger 

You can now configure a custom `endpoint_url` in s3 loggers, allowing you to customize how messages are displayed!

```yml
logging_config:
  type: s3
  level: INFO
  destination_config:
    bucket: <bucket name>
    prefix: <prefix path>
    aws_access_key_id: <(optional) AWS access key ID>
    aws_secret_access_key: <(optional) AWS secret access key>
    endpoint_url: <(optional) custom endpoint url>
```

_by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3137_

### 🐛 Bug Fixes
* Clear pipeline list filters when clicking Defaults by @johnson-mage in https://github.com/mage-ai/mage-ai/pull/3092
* Fetch Snowflake role by @mattppal in https://github.com/mage-ai/mage-ai/pull/3100
* Add service argument to OracleDB data loader by @mattppal in https://github.com/mage-ai/mage-ai/pull/3032
* Fix `pymssql` dependency by @dy46 in https://github.com/mage-ai/mage-ai/pull/3114
* Include runs without associated triggers in pipeline run count by @johnson-mage in https://github.com/mage-ai/mage-ai/pull/3118
* Fix positioning of nested flyout menu 4 levels deep by @johnson-mage in https://github.com/mage-ai/mage-ai/pull/3125
* Batch git sync in `pipeline_scheduler` by @dy46 in https://github.com/mage-ai/mage-ai/pull/3102
* Only try to interpolate variables if they are in the query by @dy46 in https://github.com/mage-ai/mage-ai/pull/3142
* Fix command for running streaming pipeline in k8s executor. by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3093
* Fix block flow bugs by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3094
* Catch timeout exception for test_connection by @dy46 in https://github.com/mage-ai/mage-ai/pull/3143
* Fix showing duplicate templates for v1 by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3128
* Add text on buttons when adding new blocks by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3106
* `check_status` method bug fix to look at pipelines ran between specific time period by @sumanshusamarora in https://github.com/mage-ai/mage-ai/pull/3115

### 💅 Enhancements & Polish
* Decrease variables response size by @johnson-mage in https://github.com/mage-ai/mage-ai/pull/3097
* Cancel block runs when pipeline run fails by @dy46 in https://github.com/mage-ai/mage-ai/pull/3096
* Clean up code in `VariableResource` method by @johnson-mage in https://github.com/mage-ai/mage-ai/pull/3099
* Import block function from file for test execution by @dy46 in https://github.com/mage-ai/mage-ai/pull/3110
* Misc UI improvements by @johnson-mage in https://github.com/mage-ai/mage-ai/pull/3133
* Azure Blob Storage upload kwargs to allow file overwrite by @sumanshusamarora in https://github.com/mage-ai/mage-ai/pull/3148
* Polish custom templates by @tommydangerous in https://github.com/mage-ai/mage-ai/pull/3120
* Throw correct exception about `io-config` by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3130
* Allow customize the timeout for the ECS task by @wangxiaoyou1993 in https://github.com/mage-ai/mage-ai/pull/3144

## New Contributors
* @sumanshusamarora made their first contribution in https://github.com/mage-ai/mage-ai/pull/3115

**Full Changelog**: https://github.com/mage-ai/mage-ai/compare/0.9.8...0.9.10
