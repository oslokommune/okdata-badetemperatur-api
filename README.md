Badeball Api
========================

Lambda functions to collect and expose water-temperatures in Oslo.

## Setup

1. [Install Serverless Framework](https://serverless.com/framework/docs/getting-started/)
2. Install plugins: 
```
sls plugin install -n serverless-python-requirements
sls plugin install -n serverless-aws-documentation
sls plugin install -n serverless-pseudo-parameters
```

## Running tests

Tests are run using [tox](https://pypi.org/project/tox/).

```
$ tox
```

## Input event format

Example kinesis event input:
```json
{
    "Records": [
        {
            "kinesis": {
                "data": "eyJkYXRhIjogeyJkZXZpY2VJZCI6ICJ4bmIwMDM1NjQzNTQwMDAwMDAwMDBiIiwgImRldmljZU5hbWUiOiAiT3NsbyBiYWRldGVtcCAgMSIsICJzZW5zb3JzIjogW3sidHlwZSI6ICJSZWZlcmVuY2UgVm9sdGFnZSIsICJ2YWx1ZSI6IDIuODQ3MDE1MzgwODU5Mzc1LCAidW5pdCI6ICJWIn0sIHsidHlwZSI6ICJCYXR0ZXJ5IFZvbHRhZ2UiLCAidmFsdWUiOiA0LjEzODY5NjI4OTA2MjUsICJ1bml0IjogIlYifSwgeyJ0eXBlIjogIkFpciBUZW1wZXJhdHVyZSIsICJ2YWx1ZSI6IDIyLjIzMDM1NDAwMzkwNjI1LCAidW5pdCI6ICJDIn0sIHsidHlwZSI6ICJUZW1wZXJhdHVyZSIsICJ2YWx1ZSI6IDIyLjY3NTA0NjIyNjIzMjg5NCwgInVuaXQiOiAiQyJ9XX19"
            }
        },
        {
            "kinesis": {
                "data": "eyJkYXRhIjogeyJkZXZpY2VJZCI6ICJ4bmIwMDM1NjQzNTQwMDAwMDAwMDBjIiwgImRldmljZU5hbWUiOiAiT3NsbyBiYWRldGVtcCAgMiIsICJzZW5zb3JzIjogW3sidHlwZSI6ICJSZWZlcmVuY2UgVm9sdGFnZSIsICJ2YWx1ZSI6IDIuODQ3MDE1MzgwODU5Mzc1LCAidW5pdCI6ICJWIn0sIHsidHlwZSI6ICJCYXR0ZXJ5IFZvbHRhZ2UiLCAidmFsdWUiOiA0LjEzODY5NjI4OTA2MjUsICJ1bml0IjogIlYifSwgeyJ0eXBlIjogIkFpciBUZW1wZXJhdHVyZSIsICJ2YWx1ZSI6IDIyLjIzMDM1NDAwMzkwNjI1LCAidW5pdCI6ICJDIn0sIHsidHlwZSI6ICJUZW1wZXJhdHVyZSIsICJ2YWx1ZSI6IDIyLjY3NTA0NjIyNjIzMjg5NCwgInVuaXQiOiAiQyJ9XX19"
            }
        }
    ]
}
```
`kinesis.data` needs to be a base64 encoded object with the following format:
```json
{
  "data": {
        "deviceId": "xnb003564354000000000b", "deviceName": "Oslo badetemp  1", "sensors": [
            {"type": "Reference Voltage", "value": 2.847015380859375, "unit": "V"},
            {"type": "Battery Voltage", "value": 4.1386962890625, "unit": "V"},
            {"type": "Air Temperature", "value": 22.23035400390625, "unit": "C"},
            {"type": "Temperature", "value": 22.675046226232894, "unit": "C"}
        ]
    }
}
```