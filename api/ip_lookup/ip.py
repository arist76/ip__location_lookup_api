'''

'''
from .models import IPv4Model, IPv6Model
import ipaddress

class IP():
    '''
    
    '''

    def __init__(self, ip_address) -> None:
        ip = ipaddress.ip_address(ip_address)
        model = IPv4Model if ip.version == 4 else IPv6Model
        ip_model = model.objects.get(ip_from__lte=int(ip), ip_to__gte=int(ip))
        ip_model_dict = ip_model.__dict__.copy()
    
        self.ip_address = ip.exploded

        dict_remove = ['ip_from', 'ip_to', '_state', 'id']
        for each in dict_remove:
            ip_model_dict.pop(each)

        self.ip_address_decimal = int(ip)

        for key, val in ip_model_dict.items():
            self.__dict__[key] = val
 