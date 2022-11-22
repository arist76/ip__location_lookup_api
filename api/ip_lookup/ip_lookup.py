#!/usr/bin/env python3
"""
This module is the main module for the ip_location_lookup_api project that works to 
return country information based on an ip address.
"""

from abc import ABC, abstractmethod
import os
import IP2Location


class IP:
    """
    An IP adress representation where all the respective data of the ip address
    is represented according to the data in the BIN data file. all the data on the ip
    are loaded in memory from the bin file for faster response.

    Attributes
    ----------
    BIN_FILE : str - an object representing the BIN database file.
    ip_address : str - the IP address the object represents
    lookup : IP2LocationRecord - stores all the data found from the database.

    Methods
    -------
    get_all() - returns all the data retrieved from the database about the IP address
    """

    try:
        BIN_FILE = os.path.join(
            os.getcwd(),
            "ip_lookup",
            "data",
            os.listdir("ip_lookup/data")[0],  # running from django
        )
    except FileNotFoundError:
        BIN_FILE = os.path.join(
            os.getcwd(), "api", "ip_lookup", "data", os.listdir("api/ip_lookup/data")[0]
        )  # running from a test in the same dir

    def __init__(self, ip_address: str) -> None:
        self.ip_address = ip_address
        self.lookup = IP2Location.IP2Location(self.BIN_FILE).get_all(ip_address)

    def get_all(self):
        """
        returns all the data retrieved from the database about the IP address.
        """

        return {
            "country_long": self.lookup.country_long,
            "country_code": self.lookup.country_short,
            "region": self.lookup.region,
            "city": self.lookup.city,
            "isp": self.lookup.isp,
            "latitude": self.lookup.latitude,
            "longitude": self.lookup.longitude,
            "domain_name": self.lookup.domain,
            "zipcode": self.lookup.zipcode,
            "timezone": self.lookup.timezone,
            "net_speed": self.lookup.netspeed,
            "area_code": self.lookup.area_code,
            "idd_code": self.lookup.idd_code,
            "weather_code": self.lookup.weather_code,
            "weather_name": self.lookup.weather_name,
            "mcc": self.lookup.mcc,
            "mnc": self.lookup.mnc,
            "mobile_brand": self.lookup.mobile_brand,
            "address_type": self.lookup.address_type,
            "category": self.lookup.category,
        }
