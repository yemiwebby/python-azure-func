import json
import unittest
from unittest.mock import MagicMock
import azure.functions as func
from function_app import sumFunction

class TestSumFunction(unittest.TestCase):

    def test_sumFunction_query(self):
        req = func.HttpRequest(
            method='GET',
            url='/api/sumFunction',
            params={'name': 'TestUser'},
            body=None
        )
        resp = sumFunction(req)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello, TestUser.", resp.get_body().decode())

    def test_sumFunction_body(self):
        req_body = json.dumps({"name": "JsonUser"}).encode('utf-8')
        req = func.HttpRequest(
            method='POST',
            url='/api/sumFunction',
            body=req_body,
            headers={"Content-Type": "application/json"}
        )
        resp = sumFunction(req)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello, JsonUser.", resp.get_body().decode())

if __name__ == '__main__':
    unittest.main()
