from django.apps import AppConfig
from threading import Thread
from django.core.management import call_command

class InventoryConfig(AppConfig):
    name = 'inventory'

    def ready(self):
        # Start the background thread to run the management command
        thread = Thread(target=self.start_periodic_task)
        thread.daemon = True
        thread.start()

    def start_periodic_task(self):
        call_command('fetch_items')

