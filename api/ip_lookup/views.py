from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ip import IP
from .serializers import IPSerializer
from django.core.exceptions import ObjectDoesNotExist

@api_view(("GET",))
def all(request, ip):
    try:
        ip_address = IP(ip)
    except ValueError as err:
        return Response({'error' : str(err)})
    except ObjectDoesNotExist:
        return Response({'error' : 'ip not found'})

    serialized_ip = IPSerializer(ip_address)
    return Response(serialized_ip.data)


@api_view(("GET",))
def unique(request, ip, key):
    try:
        ip_address = IP(ip)
    except ValueError as err:
        return Response({'error' : str(err)})
    except ObjectDoesNotExist:
        return Response({'error' : 'ip not found'})

    serialized_ip = IPSerializer(ip_address)
    try:
        res = serialized_ip.data[key]
    except KeyError:
        return Response({'error' : 'invalid key'})
    return Response(res)
