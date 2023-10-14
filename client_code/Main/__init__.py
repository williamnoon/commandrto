from ._anvil_designer import MainTemplate
from anvil import *
from ..ContactsComponent import ContactsComponent

class Main(MainTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        

        self.sidebar = ColumnPanel()
        self.add_component(self.sidebar)
        
        self.contacts_link = Link(text="Contacts")
        self.contacts_link.set_event_handler('click', self.show_contacts)
        self.sidebar.add_component(self.contacts_link)
        
        self.content_space = ColumnPanel()
        self.add_component(self.content_space)
        users = anvil.users.login_with_form()

    def show_contacts(self, **event_args):
        self.content_space.clear()
        contacts_component = ContactsComponent()
        self.content_space.add_component(contacts_component)

  
  #If using the Users service, uncomment this code to log out the user:
    def signout_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
     anvil.users.logout()
     open_form('Logout')

    def show_inventory(self, **event_args):
      """This method is called when the button is clicked"""
      pass











