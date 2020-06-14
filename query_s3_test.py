from moto import mock_s3
from query_s3 import run_s3_code
import unittest
import boto3
import json

class TestS3(unittest.TestCase):
    @mock_s3
    def test_s3(self):
        bucket = 'pablosls-test-bucket'
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket)
 
        # GIVEN
        s3_client.put_object(Bucket=bucket,
                             Key="market_a/market_infos.json",
                             Body=json.dumps({
                                 'products': [
                                     {'price': 150},
                                     {'price': 250},
                                 ]
                             }))
 
        # WHEN
        run_s3_code()
 
        # THEN
        result = int(s3_client.get_object(Bucket=bucket,
                                          Key="market_a/total_price.txt")['Body'].read())
        self.assertEqual(result, 400)
