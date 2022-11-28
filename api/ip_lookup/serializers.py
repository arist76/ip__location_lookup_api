from rest_framework import serializers


class IPSerializer(serializers.Serializer):
    """
    serializes the IP object
    """

    ip_address = serializers.IPAddressField()
    ip_address_decimal = serializers.IntegerField()
    country_code = serializers.CharField(max_length=2)
    country_name = serializers.CharField(max_length=64)
    region_name = serializers.CharField(max_length=128)
    city_name = serializers.CharField(max_length=128)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    zip_code = serializers.CharField(max_length=30)
    time_zone = serializers.CharField(max_length=8)

    class Meta:
        read_only_fields = "__all__"
