from django.core.management.base import BaseCommand
from ip_lookup.models import IPv4Model, IPv6Model
import sys
import csv

class Command(BaseCommand):

    def add_arguments(self, parser) -> None:
        parser.add_argument('version', type=str, help='the version of ip to store, this chooses the database')

        parser.add_argument('--path', type=str, help='path to the ip address csv file')
        parser.add_argument('--path-two', type=str, help='path to the ip address csv file, used only with both')

    def handle(self, *args, **kwargs):
        if kwargs['version'] == 'ipv4':
            if kwargs.get('path') != None:
                store_ip(kwargs['path'], IPv4Model)
            else:
                self.stderr.write('ipv4 path argument missing')
        elif kwargs['version'] == 'ipv6':
            if kwargs.get('path') != None:
                store_ip(kwargs['path'], IPv6Model)
            else:
                self.stderr.write('ipv6 path argument missing')
        elif kwargs['version'] == 'both':
            if kwargs.get('path') != None and kwargs.get('path_two') != None:
                print('Storing IPv4 data ...') 
                store_ip(kwargs['path'], IPv4Model)
                print('\n\nStoring IPv6 data ...') 
                store_ip(kwargs['path'], IPv6Model)
            else:
                self.stderr.write('ipv4 and ipv6 path argument missing')



def store_ip(path, ip_model):
    with open(path, 'r') as csv_file:
        csv_dict = csv.reader(csv_file)
        line_number = 0
        for row in csv_dict:
            try:
                ip_model.objects.create(
                    ip_from = row[0],
                    ip_to = row[1],
                    country_code = row[2],
                    country_name = row[3],
                    region_name = row[4],
                    city_name = row[5],
                    latitude = row[6],
                    longitude = row[7],
                    zip_code = row[8],
                    time_zone = row[9]
                )
                print(f'[DONE] line {line_number}')
            except Exception as e:
                print(f'[ERROR] line {line_number} --> {e}')

            if line_number == 100:
                break

            line_number += 1
        print('--- FINISHED ---')
