import unittest
from ip_lookup import IP
import os


class TestIP(unittest.TestCase):

    test_ip = {
        "19.5.10.1": "US",
        "25.5.10.2": "GB",
        "43.5.10.3": "JP",
        "47.5.10.4": "CA",
        "53.5.10.6": "DE",
        "2001:0200:0102::": "JP",
        "2a01:04f8:0d16:25c2::": "DE",
        "2a01:04f8:0d16:26c2::": "DE",
        "2a01:ad20::": "ES",
        "2a01:af60::": "PL",
        "127.0.0.1": "-",
        "192.168.1.1": "-",
        "1000:10:1:1": "INVALID IP ADDRESS",
    }

    def setUp(self):
        self.ip = []
        for each_ip in self.test_ip.keys():
            tmp = IP(each_ip)
            self.ip.append(tmp)

    def test_get_all(self):
        for test in self.ip:
            self.assertEqual(
                test.get_all()["country_code"], self.test_ip[test.ip_address]
            )


if __name__ == "__main__":
    unittest.main()
