from django.test import TestCase
from ..ip import IP
from ..models import IPv4Model, IPv6Model
import ipaddress

class TestIP(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ipv4_test_data = IPv4Model.objects.create(
            ip_from = 16797952,
            ip_to = 16798207,
            country_code = 'JP',
            country_name = 'Japan',
            region_name = 'Yamaguchi',
            city_name = 'Hikari',
            latitude = '33.961940',
            longitude = '131.942220',
            zip_code = '743-0021',
            time_zone = '+09:00'
        )

        cls.ipv6_test_data = IPv6Model.objects.create(
            ip_from = 281470698541056,
            ip_to = 281470698541311,
            country_code = 'JP',
            country_name = 'Japan',
            region_name = 'Shimane',
            city_name = 'Izumo',
            latitude = '35.367000',
            longitude = '132.767000',
            zip_code = '693-0044',
            time_zone = '+09:00'
        )


    def setUp(self) -> None:
        self.raw_ipv4 = '1.0.81.0'
        self.raw_ipv6 = '0000:0000:0000:0000:0000:ffff:0100:5000'
        self.ipv4_range = [16797952, 16798207]
        self.ipv6_range = [281470698541056, 281470698541311]

        self.ipv4 = IP(self.raw_ipv4)
        self.ipv6 = IP(self.raw_ipv6)



    def test_ip_db_query(self):
        self.assertGreaterEqual(self.ipv4.ip_address_decimal, self.ipv4_range[0])
        self.assertLessEqual(self.ipv4.ip_address_decimal, self.ipv4_range[1])

        self.assertGreaterEqual(self.ipv6.ip_address_decimal, self.ipv6_range[0])
        self.assertLessEqual(self.ipv6.ip_address_decimal, self.ipv6_range[1])

    def test_ip_address(self):
        self.assertEqual(self.ipv4.ip_address, self.raw_ipv4)
        self.assertEqual(self.ipv6.ip_address, self.raw_ipv6)

    def test_ip_address_decimal(self):
        self.assertEqual(self.ipv4.ip_address_decimal, int(ipaddress.ip_address(self.raw_ipv4)))
        self.assertEqual(self.ipv6.ip_address_decimal, int(ipaddress.ip_address(self.raw_ipv6)))

    def test_ip_from_doesnt_exist(self):
        self.assertIsNone(self.ipv4.__dict__.get('ip_from'))

    def test_ip_to_doesnt_exist(self):
        self.assertIsNone(self.ipv4.__dict__.get('ip_to'))


    def test_ip_state_doesnt_exist(self):
        self.assertIsNone(self.ipv4.__dict__.get('_state'))


    def test_ip_id_doesnt_exist(self):
        self.assertIsNone(self.ipv4.__dict__.get('id'))

