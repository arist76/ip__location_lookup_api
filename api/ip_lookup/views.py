from django.shortcuts import render
from .ip_lookup import IP
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(("GET",))
def all(request, ip):
    ip = IP(ip)

    return Response(ip.get_all())


@api_view(("GET",))
def unique(request, ip, key):
    ip = IP(ip)

    response = ip.lookup.__dict__.get(
        key,
        "This parameter is unavailable in selected .BIN data file or it is Invalid. Either upgrade the data file or review your query.",
    )

    return Response({key: response})
