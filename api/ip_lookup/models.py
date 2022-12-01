from django.db import models
import ipaddress


class IPModel(models.Model):
    """
    An abstract model to be inherited by IPv4Model and IPv6Model. the reason
    for this is that the fields ip_from and ip_to are necessary to be
    separated for both versions to make queries possible.
    """

    ip_from = models.DecimalField(
        max_digits=40, decimal_places=0, unique=True, primary_key=True
    )
    ip_to = models.DecimalField(max_digits=40, decimal_places=0, unique=True)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=64)
    region_name = models.CharField(max_length=128)
    city_name = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zip_code = models.CharField(max_length=30)
    time_zone = models.CharField(max_length=8)

    class Meta:
        abstract = True
        unique_together = [["ip_from", "ip_to"]]


class IPv4Model(IPModel):
    """
    Inherits from IPModel and represents IPv4 addresses
    """

    def __str__(self) -> str:
        super().__str__()
        return f"Range['{str(ipaddress.IPv4Address(int(self.ip_from)))}' : '{str(ipaddress.IPv4Address(int(self.ip_to)))}']"


class IPv6Model(IPModel):
    """
    Inherits from IPModel and represents IPv6 addresses
    """

    def __str__(self) -> str:
        super().__str__()
        return f"Range['{ipaddress.IPv6Address(int(self.ip_from)).exploded}' : '{ipaddress.IPv6Address(int(self.ip_to)).exploded}']"
