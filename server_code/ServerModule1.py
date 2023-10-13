import anvil.users
import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def get_all_contacts():
    return app_tables.contacts.search()
  