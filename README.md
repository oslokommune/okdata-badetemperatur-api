Badeball Api
========================

Lambda functions to collect and expose water-temperatures in Oslo.

## Setup

1. [Install Serverless Framework](https://serverless.com/framework/docs/getting-started/)
2. Install plugins: 
```
sls plugin install -n serverless-python-requirements
sls plugin install -n serverless-aws-documentation
```

## Running tests

Tests are run using [tox](https://pypi.org/project/tox/).

```
$ tox
```

## Input event format

Example kinesis event input:
```json
"TODO"
```
