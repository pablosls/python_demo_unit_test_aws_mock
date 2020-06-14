import boto3
import json
 
def run_s3_code():
    client = boto3.client('s3')
 
    market_infos = client.get_object(
        Bucket="pablosls-test-bucket",
        Key="market_a/market_infos.json"
    )['Body'].read().decode('utf-8')
 
    client.put_object(
        Bucket="pablosls-test-bucket",
        Key="market_a/total_price.txt",
        Body=str(sum(map(lambda a: a['price'], json.loads(market_infos)['products'])))
    )