from django.core.management import BaseCommand
from ip_lookup.models import IPv4Model, IPv6Model


class Command(BaseCommand):
    help = "checks if the ipv4 and ipv6 databases are populated"

    def add_arguments(self, parser) -> None:
        parser.add_argument("version", choices=["ipv4", "ipv6"])

    def handle(self, *args, **options):
        if options.get("version") is not None:
            IPV4_TOTAL_ROWS = 3031464
            IPV6_TOTAL_ROWS = 4908498
            if options["version"] == "ipv4":
                ipv4_row_count = IPv4Model.objects.all().count()
                self.stdout.write(
                    "true" if ipv4_row_count == IPV4_TOTAL_ROWS else "false"
                )
            elif options["version"] == "ipv6":
                ipv6_row_count = IPv6Model.objects.all().count()
                self.stdout.write(
                    "true" if ipv6_row_count == IPV6_TOTAL_ROWS else "false"
                )
            else:
                self.stderr.write(f"{options['version']} is not a valid input")
        else:
            self.stderr.write("Specify the database version to check")
