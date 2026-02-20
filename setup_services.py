import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lcf.settings') # <-- Ensure 'myproject' matches your folder name
django.setup()

from myapp.models import Service

def populate_services():
    service_tags = [
        "IATA AGENT", "CUSTOM BROKER – IMPORT – COMMODITY", 
        "CUSTOM BROKER – EXPORT – COMMODITY", "NVOCC – PORTS SERVED",
        "SHIPPING LINE – PORTS SERVED", "FREIGHT FORWARDER", 
        "CONSOLIDATOR", "OVERSEAS AGENT", "SHIPPER", "CONSIGNEE", 
        "CONTAINER SELLER", "CONTAINER BUYER", "TRANSPOTER", 
        "QUALITY CERTIFICATION", "REEFER CONTAINER"
    ]

    for tag in service_tags:
        obj, created = Service.objects.get_or_create(name=tag)
        if created:
            print(f"Added: {tag}")
        else:
            print(f"Skipped: {tag}")

if __name__ == "__main__":
    populate_services()