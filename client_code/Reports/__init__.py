from ._anvil_designer import ReportsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Reports(ReportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #Populate plot_1 with dummy data. All three Bar charts will be added to the same figure
   

    #Return the figure from the server to populate plot_2
    self.plot_2.figure = anvil.server.call('return_bar_charts')

    self.plot_3.data = [
      go.Pie(
        labels=["Mobile", "Tablet", "Desktop"],
        values=[2650, 755, 9525]
      )
    ]
    

