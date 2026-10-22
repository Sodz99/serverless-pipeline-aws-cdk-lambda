# Build Serverless Pipeline using AWS CDK and Lambda in Python

Build Serverless Pipeline using AWS CDK and Lambda in Python — AWS Data Engineering project.

## Overview
Serverless architecture is a method of developing and deploying applications and services without maintaining infrastructure. Your application is still running on servers, but AWS manages them all. You no longer need to provision, scale, and maintain servers to operate your applications, databases, and storage systems. Learn more about serverless computing by clicking here. Serverless architecture allows developers to focus on their core product rather than maintaining and administering servers or runtimes in the cloud or on-premises. This decreased overhead frees up time and resources for developers to focus on creating excellent solutions that scale and are dependable. We aim to build a serverless pipeline using AWS CDK to analyze the finance data from 3 different sources. The historical stock data is stored in the Amazon aurora database, the historical FOREX data(Foreign Exchange Market) is stored in an AWS S3 bucket in JSON format, and the intraday stock data comes from the Alpha V

## Data
Alpha Vantage offers enterprise-grade financial market data via a collection of robust and developer-friendly data APIs and spreadsheets. Alpha Vantage is your one-stop shop for real-time and historical global market data delivered through REST stock APIs, Excel, and Google Sheets, ranging from traditional asset classes (e.g., stocks, ETFs, commodities) to economic metrics, foreign exchange rates to cryptocurrencies, fundamental data to technical indicators.

_Data is not included in this repository._

## Tech stack
➔ Language: Python ➔ Services: AWS S3, Amazon Lambda, Amazon Aurora, AWS Glue, Amazon Athena, Quicksight, AWS CDK

AWS CDK: The AWS Cloud Development Kit (AWS CDK) is an open-source software development platform for defining cloud architecture in code and provisioning it using AWS CloudFormation. It provides a high-level object-oriented framework for defining AWS resources with the capability of current programming languages.

## How to run
```bash
pip install -r Code/requirements-dev.txt
python Code/app.py
```

## Project structure
```
.gitignore
Code/
  .gitignore
  Analysis Queries.sql
  Load data to RDS.py
  README.md
  app.py
  data_deployment/
    data_deployment_stack.py
  glue_database/
    glue_database_stack.py
  glue_pipeline/
    glue_pipeline_stack.py
    scripts/
  lambda/
    convertHistoricalData.py
    getForexHourlyData.py
    getIntradayStockData.py
    helperFunctions.py
  lambda_pipeline/
    .~c9_invoke_p27Z6L.py
    lambda_pipeline_stack.py
  requirements-dev.txt
  requirements.txt
  scripts/
    backfill.py
  source.bat
  tests/
    __init__.py
    unit/
README.md
```

## Credits
Based on a ProjectPro guided project.
