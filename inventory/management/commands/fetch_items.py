import os
import requests
import json
from django.core.management.base import BaseCommand
from datetime import datetime
from django.conf import settings
import time


class Command(BaseCommand):
    help = 'Fetch items with quantity 0 and save to a JSON file'

    def handle(self, *args, **kwargs):
        data_dir = os.path.join(settings.BASE_DIR, 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        while True:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            url = 'http://127.0.0.1:8000/api/inventory/v1/items/?quantity=0'

            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                filename = os.path.join(data_dir, f'items_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)

            except requests.RequestException as e:
                self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))

            time.sleep(60)
