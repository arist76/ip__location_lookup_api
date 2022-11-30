"""
contains the IP class responsible for quering the ip database.
"""
from .models import IPv4Model, IPv6Model
import ipaddress


class IP:
    """
    this class is responsible for quering the ip database. this class will be
    serialized by an IPserializer. for this reason this class is also
    responsible to manage the data to be sent to the user.
    """

    def __init__(self, ip_address) -> None:
        """
        the constructor queries the database for the ip address and manages data
        in the form of its attributes.
        """
        ip = ipaddress.ip_address(ip_address)
        model = IPv4Model if ip.version == 4 else IPv6Model
        ip_model = model.objects.get(ip_from__lte=int(ip), ip_to__gte=int(ip))
        ip_model_dict = ip_model.__dict__.copy()

        self.ip_address = ip.exploded

        dict_remove = ["ip_from", "ip_to", "_state"]
        for each in dict_remove:
            ip_model_dict.pop(each)

        self.ip_address_decimal = int(ip)

        for key, val in ip_model_dict.items():
            self.__dict__[key] = val
