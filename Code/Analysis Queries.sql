
----Intraday Price Trend

SELECT datetime, close
FROM "AwsDataCatalog"."finance_database"."stock_data_intraday"
WHERE ticker = 'MSFT'
ORDER BY datetime ASC;




-----Calculate Percentage Change (Returns)

SELECT datetime,
       ticker,
       (close - LAG(close) OVER (PARTITION BY ticker ORDER BY datetime)) / LAG(close) OVER (PARTITION BY ticker ORDER BY datetime) * 100 AS pct_change
FROM "AwsDataCatalog"."finance_database"."stock_data_intraday"
WHERE ticker = 'MSFT';


-----Daily High & Low

SELECT date,
       ticker,
       MAX(high) AS day_high,
       MIN(low) AS day_low
FROM "AwsDataCatalog"."finance_database"."stock_data_intraday"
GROUP BY date, ticker
ORDER BY date DESC;



-----Moving Average (Short-Term Trend)

SELECT datetime,
       ticker,
       AVG(close) OVER (PARTITION BY ticker ORDER BY datetime ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS moving_avg_4
FROM "AwsDataCatalog"."finance_database"."stock_data_intraday"
WHERE ticker = 'AMZN';

