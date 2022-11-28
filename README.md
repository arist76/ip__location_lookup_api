# ip_location_lookup_api

This is a backend API that returns to the user the country and country code by IP address or hostname it originates from. It can also find region or state, city, latitude and longitude, ZIP code, time zone.

## Requirements

- Python 3.10
- Django 4.1.3
- Djangorestframework 3.14.0
- IP2Loction 8.9.0
## Installation

```bash
git clone https://github.com/arist76/ip_location_lookup_api.git
cd ip_location_lookup_api/api
python3 manage.py runserver
```

Then read the end points below and try it out with curl or postman

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
    ip_address : 16797952,
    ip_address_decimal : 16798207,
    country_code : "JP",
    country_name : "Japan",
    region_name : "Yamaguchi",
    city_name : "Hikari",
    latitude : "33.961940",
    longitude : "131.942220",
    zip_code : "743-0021",
    time_zone : "+09:00",
    version : "4"
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

| Field           | Description                                 |
| --------------- | --------------------------------------------|
| country_long    | short country name                          |
| country_code    | country code (2 letter, ISO 3166-1 alpha-2) |
| region          | region name (administrative division)       |
| city            | city name                                   |
| isp             | name of internet service provider           |
| latitude        | latitude coordinate location                |
| longitude       | longitude coordinate location               |
| domain_name     | domain name associated with the ip          |
| zipcode         | zipcode of the address                      |
| timezone        | timezone of the address                     |

## Testing

```bash
python3 manage.py test
```

## Authors

- [surafel_fikru](https://www.github.com/arist76)

