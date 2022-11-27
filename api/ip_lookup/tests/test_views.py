from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
import json

class TestViews(APITestCase):
    '''
    tests for different endpoints in the application. This tests work with the first 100
    lines of the ip address csv files for both versions.

    NOTE : run ./manage.py import_csv both --path data/IP2LOCATION-LITE-DB11.CSV --path-two data/IP2LOCATION-LITE-DB11.IPV6.CSV
    before running the tests. you can replace the two path arguments with any file you want.
    '''
    def setUp(self) -> None:
        super().setUp()
        with open('ip_lookup/tests/test_data.json', 'r') as test_data:
            self.data = json.load(test_data)
        self.client = APIClient()

    def test_all_status_code(self):
        for each_data in self.data:
            res = self.client.get(reverse('all', args=[each_data['ip_address']]))
            self.assertEqual(res.status_code, 200)
            
    def test_all(self):
        for each_data in self.data:
            res = self.client.get(reverse('all', args=[each_data['ip_address']]))
            res_data = json.loads(res.content)
            for key in each_data.keys():
                self.assertEqual(
                    each_data[key],
                    res_data[key]
                )

    def test_unique(self):
        endpoints = ['country_code', 'country_name', 'region_name', 'city_name', 'latitude', 'longitude', 'zip_code', 'time_zone', 'version']
        for ip in self.data:
            for endpoint in endpoints:
                res = self.client.get(reverse('unique', args=[ip['ip_address'], endpoint]))
                res_data = json.loads(res.content)
                self.assertEqual(res.status_code, 200)
                self.assertEqual(res_data[endpoint], ip[endpoint])
