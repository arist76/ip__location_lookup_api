# ip_location_lookup_api

This is a backend API that returns to the user the country and country code by IP address or hostname it originates from. The API reads the geo location information from IP2Location BIN data file. depending on the data file it can also find region or state, city, latitude and longitude, ZIP code, time zone, Internet Service Provider (ISP) or company name, domain name, net speed, area code, weather station code, weather station name, mobile country code (MCC), mobile network code (MNC) and carrier brand, elevation, usage type, address type and IAB category. It also has a functionality to update the data file.

## Requirements

- Python 3.5
- Django 4.1.3
- Djangorestframework 3.14.0
- IP2Loction 8.9.0
## Installation

```bash
git clone https://github.com/arist76/ip__location_lookup_api.git
```


## Bin data file

The bin data file containing data for ip addresses should be put in
a folder named "data" found in the same directory as the ip_lookup module.
Note that the bin data file must be the only file in side the folder. use
an IPv6 data file as it contains data for both IPv4 and IPv6. the details of
the data file depend on the type of the bin file. upgrade the bin file for a
more detailed and precises data. By default the bin file
## Endpoints

### Complete Fields

#### Http Request

```
http://127.0.0.1:8000/lookup/all/{ip_address}
```

#### Parameters

| Parameter       | Description                                               | Example                                    |
| --------------- | ------------                                              | -------------------------------------------|
| ip_address      | An IP address for which you want to retrieve the location | http://127.0.0.1:8000/lookup/all/112.1.2.1 |

#### Http Response

A JSON object containing all the data listed down below. The Example below shows
the response for the ip address in the above table. It uses the IP2Location™ LITE IP-COUNTRY Database.

```json
{
    "country_name": "China",
    "country_code": "CN",
    "region": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "city": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "ISP": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "latitude": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "longitude": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "domain_name": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "ZIP_code": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "time_zone": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "net_speed": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "area_code": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "IDD_code": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "weather_station_code": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "weather_station_name": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "MCC": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "MNC": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "mobile_brand": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "address_type": "This parameter is unavailable in selected .BIN data file. Please upgrade data file.",
    "category": "This parameter is unavailable in selected .BIN data file. Please upgrade data file."
}
```
### Complete Fields

#### Http Request

```
http://127.0.0.1:8000/lookup/unique/{ip_address}/{field}
```

#### Parameters

| Parameter       | Description                                               | Example                                                    |
| --------------- | ------------                                              | -----------------------------------------------------------|
| ip_address      | An IP address for which you want to retrieve the location | http://127.0.0.1:8000/lookup/all/112.1.2.1                 |
| field           | The unique field of the ip address                        | http://127.0.0.1:8000/lookup/unique/112.1.2.1/country_code |

#### Http Response

A json object with a key named after the query "field" and value containing its respective
answer.

#### Valid Unique Endpoints

| Field           | Description|
| --------------- | ------------|
| country_long    | short country name |
| country_code    | country code (2 letter, ISO 3166-1 alpha-2)|
| region          | region name (administrative division)|
| city            | city name |
| isp             | name of internet service provider |
| latitude        | latitude coordinate location|
| longitude       | longitude coordinate location |
| domain_name           | domain name associated with the ip|
| zipcode           | zipcode of the address|
| timezone           | timezone of the address |
| net_speed           | net speed|
| area_code           | area code of the address|
| idd_code           | idd code|
| weather_code           | weather station code|
| weather_name           | weather station name|
| mcc           | MCC |
| mnc           | MNC |
| mobile_brand           | mobile brand |
| address_type           | address type |
| category           | category |

## Authors

- [surafel_fikru](https://www.github.com/arist76)

