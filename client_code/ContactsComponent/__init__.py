from ._anvil_designer import ContactsComponentTemplate
from anvil import DataGrid, Button
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ContactsComponent(ContactsComponentTemplate):
  def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)
      self.title_label = Label(text="Contacts List")
      self.add_component(self.title_label)
      self.contacts_datagrid = DataGrid()
      self.add_component(self.contacts_datagrid)
      self.refresh_button = Link(text="Refresh")
      self.refresh_button.set_event_handler('click', self.refresh_data)
      self.add_component(self.refresh_button)
      # Any code you write here will run before the form o
        
       
        
  def refresh_data(self, **event_args):
        contacts = anvil.server.call('get_all_contacts')
        self.contacts_datagrid.items = contacts