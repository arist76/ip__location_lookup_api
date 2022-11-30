from django.test import TestCase, Client
from ..models import IPv4Model, IPv6Model
from django.urls import reverse
import ipaddress


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ipv4_test_data = IPv4Model.objects.create(
            ip_from=16797952,
            ip_to=16798207,
            country_code="JP",
            country_name="Japan",
            region_name="Yamaguchi",
            city_name="Hikari",
            latitude="33.961940",
            longitude="131.942220",
            zip_code="743-0021",
            time_zone="+09:00",
        )

        cls.ipv6_test_data = IPv6Model.objects.create(
            ip_from=281470698541056,
            ip_to=281470698541311,
            country_code="JP",
            country_name="Japan",
            region_name="Shimane",
            city_name="Izumo",
            latitude="35.367000",
            longitude="132.767000",
            zip_code="693-0044",
            time_zone="+09:00",
        )

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.test_ipv4 = "1.0.81.0"
        cls.test_ipv6 = "0000:0000:0000:0000:0000:ffff:0100:5000"
        cls.valid_keys = [
            "country_code",
            "country_name",
            "region_name",
            "city_name",
            "latitude",
            "longitude",
            "zip_code",
            "time_zone",
        ]

    def setUp(self) -> None:
        self.client = Client()

    def test_all_success_status_code(self):
        res_v4 = self.client.get(reverse("all", args=[self.test_ipv4]))
        res_v6 = self.client.get(reverse("all", args=[self.test_ipv6]))

        self.assertEqual(res_v4.status_code, 200)
        self.assertEqual(res_v6.status_code, 200)

    def test_all_invalid_ip_address(self):
        res_v4 = self.client.get(reverse("all", args=["256.0.0.0"]))
        res_v6 = self.client.get(
            reverse("all", args=["zzzz:0000:0000:0000:0000:ffff:0100:5000"])
        )

        self.assertEqual(res_v4.status_code, 404)
        self.assertEqual(res_v6.status_code, 404)

    def test_all_response(self):
        res_v4 = self.client.get(reverse("all", args=[self.test_ipv4]))
        res_v6 = self.client.get(reverse("all", args=[self.test_ipv6]))

        v4_data = res_v4.json()
        v6_data = res_v6.json()

        for key in self.valid_keys:
            if key == "latitude" or key == "longitude":
                self.assertEqual(v4_data[key], float(self.ipv4_test_data.__dict__[key]))
                continue
            self.assertEqual(v4_data[key], self.ipv4_test_data.__dict__[key])

        for key in self.valid_keys:
            if key == "latitude" or key == "longitude":
                self.assertEqual(v6_data[key], float(self.ipv6_test_data.__dict__[key]))
                continue
            self.assertEqual(v6_data[key], self.ipv6_test_data.__dict__[key])

    def test_unique_success_status_code(self):
        for key in self.valid_keys:
            res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, key]))
            res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, key]))

            self.assertEqual(res_v4.status_code, 200)
            self.assertEqual(res_v6.status_code, 200)

    def test_unique_invalid_ip_address(self):
        res_v4 = self.client.get(reverse("unique", args=["256.1.2.1", "country_name"]))
        res_v6 = self.client.get(
            reverse(
                "unique",
                args=["zzzz:0000:0000:0000:0000:ffff:0100:5000", "country_name"],
            )
        )

        self.assertEqual(res_v4.status_code, 404)
        self.assertEqual(res_v6.status_code, 404)

    def test_unique_invalid_key_argument(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "random"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "random"]))

        self.assertEqual(res_v4.status_code, 404)
        self.assertEqual(res_v6.status_code, 404)

    def test_unique_response_ip_address(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "ip_address"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "ip_address"]))

        self.assertEqual(res_v4.json(), self.test_ipv4)
        self.assertEqual(res_v6.json(), self.test_ipv6)

    def test_unique_response_ip_address_decimal(self):
        res_v4 = self.client.get(
            reverse("unique", args=[self.test_ipv4, "ip_address_decimal"])
        )
        res_v6 = self.client.get(
            reverse("unique", args=[self.test_ipv6, "ip_address_decimal"])
        )

        self.assertEqual(res_v4.json(), int(ipaddress.ip_address(self.test_ipv4)))
        self.assertEqual(res_v6.json(), int(ipaddress.ip_address(self.test_ipv6)))

    def test_unique_response_country_code(self):
        res_v4 = self.client.get(
            reverse("unique", args=[self.test_ipv4, "country_code"])
        )
        res_v6 = self.client.get(
            reverse("unique", args=[self.test_ipv6, "country_code"])
        )

        self.assertEqual(res_v4.json(), self.ipv4_test_data.__dict__["country_code"])
        self.assertEqual(res_v6.json(), self.ipv6_test_data.__dict__["country_code"])

    def test_unique_response_country_name(self):
        res_v4 = self.client.get(
            reverse("unique", args=[self.test_ipv4, "country_name"])
        )
        res_v6 = self.client.get(
            reverse("unique", args=[self.test_ipv6, "country_name"])
        )

        self.assertEqual(res_v4.json(), self.ipv4_test_data.__dict__["country_name"])
        self.assertEqual(res_v6.json(), self.ipv6_test_data.__dict__["country_name"])

    def test_unique_response_region_name(self):
        res_v4 = self.client.get(
            reverse("unique", args=[self.test_ipv4, "region_name"])
        )
        res_v6 = self.client.get(
            reverse("unique", args=[self.test_ipv6, "region_name"])
        )

        self.assertEqual(res_v4.json(), self.ipv4_test_data.__dict__["region_name"])
        self.assertEqual(res_v6.json(), self.ipv6_test_data.__dict__["region_name"])

    def test_unique_response_city_name(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "city_name"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "city_name"]))

        self.assertEqual(res_v4.json(), self.ipv4_test_data.__dict__["city_name"])
        self.assertEqual(res_v6.json(), self.ipv6_test_data.__dict__["city_name"])

    def test_unique_response_latitude(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "latitude"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "latitude"]))

        self.assertEqual(res_v4.json(), float(self.ipv4_test_data.__dict__["latitude"]))
        self.assertEqual(res_v6.json(), float(self.ipv6_test_data.__dict__["latitude"]))

    def test_unique_response_longitude(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "longitude"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "longitude"]))

        self.assertEqual(
            res_v4.json(), float(self.ipv4_test_data.__dict__["longitude"])
        )
        self.assertEqual(
            res_v6.json(), float(self.ipv6_test_data.__dict__["longitude"])
        )

    def test_unique_response_zip_code(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "zip_code"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "zip_code"]))

        self.assertEqual(res_v4.json(), self.ipv4_test_data.__dict__["zip_code"])
        self.assertEqual(res_v6.json(), self.ipv6_test_data.__dict__["zip_code"])

    def test_unique_response_time_zone(self):
        res_v4 = self.client.get(reverse("unique", args=[self.test_ipv4, "time_zone"]))
        res_v6 = self.client.get(reverse("unique", args=[self.test_ipv6, "time_zone"]))

        self.assertEqual(res_v4.json(), self.ipv4_test_data.__dict__["time_zone"])
        self.assertEqual(res_v6.json(), self.ipv6_test_data.__dict__["time_zone"])
