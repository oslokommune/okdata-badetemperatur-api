okdata-badetemperatur-api
=========================

Lambda functions and API to collect and expose water temperatures in Oslo.

## Setup

1. [Install Serverless Framework](https://serverless.com/framework/docs/getting-started/)
2. Install dependencies
```
make init
```

## Running tests

Tests are run using [tox](https://pypi.org/project/tox/).

```
$ make test
```

## Deploy

Deploy to both dev and prod is automatic via GitHub Actions on push to
`main`. You can alternatively deploy from local machine (requires `saml2aws`)
with: `make deploy` or `make deploy-prod`.

## Input event format

Example Kinesis event input:
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
    "id": "xnb003564354000000000b",
    "name": "Oslo badetemp # 1",
    "time": "2019-02-28T08:13:35.000+0000",
    "sensors": [
        {
            "type": "Temperature",
            "value": 3.0326954949977676,
            "unit": "C"
        }
    ]
}
```
