from django.core.management import BaseCommand
from api.settings import BASE_DIR
import os
from django.db import connection
from ip_lookup.models import IPv4Model, IPv6Model


class Command(BaseCommand):
    help = "stores data from a csv file to a postgres database"

    def add_arguments(self, parser) -> None:
        parser.add_argument("action")
        parser.add_argument(
            "-f",
            "--path-ipv4",
            nargs="?",
            default="/tmp/data/IPV4.CSV",
        )
        parser.add_argument(
            "-s",
            "--path-ipv6",
            nargs="?",
            default="/tmp/data/IPV6.CSV",
        )

        parser.add_argument("--ip-version", nargs=1, choices=[4, 6], type=int)

    def handle(self, *args, **options):
        if options["action"] == "copy":
            path_invalid = not (
                os.path.exists(options["path_ipv4"])
                and os.path.exists(options["path_ipv6"])
            )
            if path_invalid:
                print(os.getcwd())
                self.stderr.write("path for one or both arguments does not exist!")
                self.stdout.write(
                    "if you have not passed any path as an argument\nthen the default path and files do not exist. \ntry to put the csv files in a /tmp/data folder and name them IPV4.CSV and IPV6.CSV"
                )
            else:
                self.__handle_copy(4, options[f"path_ipv4"])
                self.__handle_copy(6, options[f"path_ipv6"])
                exit()

        elif options["action"] == "clean":
            if options["ip_version"][0] in [4, 6]:
                self.__handle_clean(options["ip_version"])
                exit()
            else:
                self.stdout.write(
                    f"{options['ip_version']} is not a valid version, enter between 4 and 6"
                )

    def __handle_copy(self, version, path):
        model = IPv4Model if version == 4 else IPv6Model
        is_populated = model.objects.all().count()
        if is_populated:
            self.stdout.write(
                "The database seems to be populated. its going to be wipped out and replaced by your new data"
            )
        confirmation = self.__request_confirmation(
            "Are you sure you want to clean and repopulated the database?[y,n]"
        )

        if confirmation:
            self.__clean_db(version)
            self.__import_csv(version, path)
        else:
            self.stdout.write("Exiting...")
            exit()

    def __handle_clean(self, version):
        model = IPv4Model if version == 4 else IPv6Model
        is_populated = model.objects.all().count()
        if is_populated:
            confirmation = self.__request_confirmation(
                "your data will be lost, continue [y,n]\n"
            )
            if confirmation:
                self.__clean_db(version)
            else:
                self.stdout.write("Exiting...")
                exit()
        else:
            self.stdout.write("database already empty. Exiting...")
            exit()

    def __import_csv(self, version, path):
        with connection.cursor() as cursor:
            table = "ip_lookup_ipv4model" if version == 4 else "ip_lookup_ipv6model"
            cursor.execute(
                f"COPY {table}(ip_from,ip_to,country_code, country_name, region_name, city_name, latitude, longitude, zip_code, time_zone) FROM '{path}' DELIMITER ',' CSV;",
                [table, path],
            )

    def __clean_db(self, version):
        with connection.cursor() as cursor:
            table = "ip_lookup_ipv4model" if version == 4 else "ip_lookup_ipv6model"
            cursor.execute(f"TRUNCATE TABLE {table};")

    def __request_confirmation(self, prompt_msg):
        confirmation = input(prompt_msg)
        while confirmation not in ["y", "Y", "n", "N", "no", "yes"]:
            self.stdout.write("please pick between y/n")
            confirmation = input(prompt_msg)

            if confirmation in ["n", "N", "no"]:
                break

        return True if confirmation in ["y", "Y", "yes"] else False


"""
    copy [-f(--ipv4-path) <csv_file_path>, -s(--ipv6-path) <csv_file_path>]
    clean [-f(--ipv4-path), -s(--ipv6-path) <csv_file_path>]
"""
