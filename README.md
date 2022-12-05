# ~ VOLARE ~
Volare (voh-la-ray) is a Serverless data pipeline framework using AWS native serivces. 

## Who it's for
Data scientists who want to tranform and perform analytics on large datasets in a structured, predictable way. 
Data engineers who want to create Serverless ETL pipelines with the majority of infrastructure owned and managed by AWS. 
Teams who want a to be able to use AWS Glue datasets directly from python with a standard API.

## What it does
- Define your datasets by using python classes. You can easily customize the behavior of Glue operations (partitioning, schema discovery and evolution). Volare provides a data lineage capability on top of Glue. 
- Create steps for transforming your data and compose these steps into re-usable pipelines. Re-use portions of state machines together to easily create new pipelines. 
- Easily create pipeline configurations that can be validated. No more running into errors hours after kicking off a pipeline execution. 

## How it works

### Creating a Dataset and Pipeline 
```python 
from volare import Dataset
equity_ds = 

@Dataset
class MyHouseSizeDataset: 
    name = 'house-sizes' 
    schema='discover'

    def parse(): 
        # You can define custom parser logic here
        pass 
```

now that we've created a dataset class, we can add it to our pipeline: 

```python 
from volare import Pipeline

source_list = [ MyHouseSizeDataset ]

@Pipeline(
    sources=source_list
)
class MyHousingPipeline: 
    pass
```

### Deployment
Now that we've defined a simple pipeline and dataset, we can deploy it. 
```python
pipeline = MyHousingPipeline()
pipeline.deploy()
```

or alternatively:

```shell
volare deploy my_housing_pipeline.py
```
Which will deploy all class that are decorated with `@Pipeline` in the given python script.