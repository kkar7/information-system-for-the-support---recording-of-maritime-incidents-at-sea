from ._anvil_designer import StatsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.plotly.graph_objs as go

class Stats(StatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Καλεί την server function για να πάρει τον αριθμό των μοναδικών σημάτων
    unique_sign_count = anvil.server.call('get_unique_sign_count')
    # Εμφανίζει τον αριθμό σε ένα label
    self.label_unique_signs.text = f"Μοναδικά σήματα: {unique_sign_count}"
    # Αυτή η συνάρτηση μπορεί να καλεστεί όταν φορτώνει η φόρμα ή όταν πατηθεί ένα κουμπί
    #def refresh_unique_sign_count():
    
    
    def show_nationality_chart(self):
      # Καλεί την server function για να πάρει τα δεδομένα για το διάγραμμα
      nationality_counts = anvil.server.call('get_nationality_counts')
    
      # Δημιουργία δεδομένων για το διάγραμμα
      data = go.Bar(
        x=list(nationality_counts.keys()),
        y=list(nationality_counts.values())
      )
    
      # Ορισμός της διάταξης του διαγράμματος
      layout = go.Layout(
        title='Εθνικότητες Πλοίων που Έχουν Ζητήσει Βοήθεια',
        xaxis=dict(title='Εθνικότητα'),
        yaxis=dict(title='Πλήθος')
      )
    
    # Δημιουργία του διαγράμματος και εμφάνιση στο στοιχείο Plot της φόρμας
    self.plot_nationalities.figure = go.Figure(data=[data], layout=layout)


    #stats = anvil.server.call('get_age_statistics')
   # self.label_mean.text = f"Μέσος Όρος: {stats['mean']:.2f}"
   # self.label_median.text = f"Διάμεσος: {stats['median']:.2f}"
   # self.label_range.text = f"Εύρος: {stats['range']}"
   # self.label_variance.text = f"Διακύμανση: {stats['variance']:.2f}"
   ## self.label_std_dev.text = f"Τυπική Απόκλιση: {stats['std_dev']:.2f}"
   # self.label_min.text = f"Ελάχιστη Τιμή: {stats['min']}"
   # self.label_max.text = f"Μέγιστη Τιμή: {stats['max']}"



