# Συλλογή Δεδομένων

Όσον αφορά τις πηγές και τη συλλογή δεδομένων,προκειμένου να φέρουμε εις πέρας την ανάλυση του θέματος που επιλέξαμε, το έργο μας ήταν αρκετά ξεκάθαρο. Καταρχάς, ολόκληρο το σύνολο δεδομένων που αντλήσαμε προήλθε απο μία πηγή, την επίσημη ιστοσελίδα της ΕΔΑΑΠ. Για τα ερωτήματα που ενδιαφερόμασταν, χρειαστήκαμε τα δεδομένα απο την υποσελίδα "Πορίσματα/Εκθέσεις", στην οποία εμπεριέχονται τέσσερις πίνακες με πλήθος πληροφοριών σχετικά με τα αεροπορικά ατυχήματα στην Ελλάδα απο το 2000 έως και το 2020. Πιο συγκεκριμένα, **οι πληροφορίες που μας ενδιέφεραν είναι: η ημερομηνία του ατυχηματος, ο αριθμός των τραυματισμών και των θανάτων συνολικά**. Κατά τη διαδικασία του scraping(κάναμε multiple page scraping για να συλλέξουμε τα δεδομένα και απο τις τέσσερις σελίδες απο τα Πορίσματα/Εκθέσεις), συλλέξαμε όλες τις πληροφορίες, ακόμα και αυτές που δεν χρειαζόμασταν για την ανάπτυξη των ερωτημάτων που μας ενδιέφερε. Πιο συγκεκριμένα, καταρχάς προσπαθήσαμε να δημιουργήσουμε έναν scraper που θα αντλήσει τα δεδομένα μας απο τον κάθε πίνακα(μέσω inspect των html elements της σελίδας). Έπειτα, συγκεντρώσαμε τα 4 urls(κάθε ένα απο τα οποία περιέχει έναν πίνακα) σε μία λίστα την οποία ονομάσαμε urls, και στη συνέχεια φτιάξαμε μια for loop (for url in urls:...) στην οποία προσθέσαμε τον αρχικό scraper.
# Καθαρισμός και Ανάλυση Δεδομένων

Ο καθαρισμός των δεδομένων μας χωρίστηκε σε δύο στάδια-jupyter notebooks, κατά τα οποία χρησιμοποίησαμε pandas και regex. Στο πρωταρχικό, αφού είχαμε λάβει ένα αρκετα ξεκάθαρο dataframe απο το αρχείο scraping(multiple_pages_scraping_incidents), επιχειρήσαμε να καθαρίσουμε περαιτέρω, να αντικαταστήσουμε missing values, αλλά και να χωρίσουμε ορισμένες στήλες σε επιμέρους, έτσι ώστε οι πληροφορίες να παρουσιάζονται πιο ομοιόμορφα(jupyter notebook: all_incidents_cleaned). Σε δεύτερο στάδιο(jupyter notebook:final_data_cleaned), φτιάξαμε ένα καινούριο df με βάση φυσικά το προηγούμενο, και συγκεκριμένα τη στήλη fatalites(df1 = fatalities). Σε αυτό ουσιαστικά κρατήσαμε-με ορισμένες τροποποιήσεις- τις στήλες και τα δεδομένα που μας ενδιέφεραν, με κάποιες επιπλέον προσθήκες, οι οποίες θα μας βοηθούσαν στην οπτικοποίηση: (Αναλυτικά οι περισσότερες εντολές στο αρχείο DOCUMENTATION).

- Τις ημερομηνίες, που μετατράπηκαν σε απλά χρονολογίες('Year')
- Τους θανάσιμους τραυματισμούς('fatal_injuries')
- τους μικρούς τραυματισμούς('minor_injuries')
- τους σοβαρούς τραυματισμούς('serious_injuries')
- τις περιπτώσεις χωρίς τραυματισμούς('no_injuries')
- τον συνολικό αριθμό ατυχημάτων('all_incidents')
- τον συνολικό αριθμό τραυματισμών, εκτός των θανάσιμων(αντικαταστήσαμε τα Missing values με 0, μετατρέψαμε τα αριθμητικά δεδομένα απο μορφη float σε integer και έπειτα προσθέσαμε τα δεδομενα των δύο στηλών minor_injuries και serious_injuries)('total_injuries')

Η χρήση απλών εντολών regex μας βοήθησε να κάνουμε καλύτερο και πιο λειτουργικό καθαρισμό περιττών στοιχείων στα values ποικίλων columns.





# Οπτικοποίηση Δεδομένων

Προκειμένου να πετύχουμε ακριβή οπτικοποίηση των δεδομένω που θέλαμε, χρειάστηκε να επεξεργαστούμε λίγο ακόμα το τελικό DataFrame. Έτσι, δημιουργήσαμε επιπλέον csv αρχεία(fatal_injuries.csv,incidents_injuries.csv), στα οποία κρατήσαμε δύο ή τρεις στήλες μόνο, αναλόγως ποιές χρειαζόμασταν. Στο πρώτο, κρατήσαμε τις στήλες 'Year' και 'fatal_injuries', και έπειτα τις 'Year', 'all_incidents' και 'total_injuries'. Κατά τη διαδικασία της δημιουργίας των διαγραμμάτων, ένα split bars chart, το οποίο απεικονίζει το σύνολο των ατυχημάτων συνδυαστικά με εκείνο των τραυματισμών, ανά έτος, και ένα line chart, το οποίο αναπαριστά το σύνολο των θανάτων ανά έτος, χρησιμοποιήσαμε την πλατφόρμα Datawrapper.

# Δημοσιογραφικό μέρος

Όσον αφορά το δημοσιογραφικό μέρος της εργασίας μας, η κύρια πηγή πληροφοριών ήταν και πάλι η επίσημη ιστοσελίδα της ΕΔΑΑΠ. Τα δεδομένα και οι πληροφορίες που αντλήσαμε απο εκεί, μας έδωσαν μια γενική εικόνα των πραγμάτων με τα οποία θέλαμε να ασχοληθούμε, την οποία χρωμάτισε η συνέντευξη που μας παραχώρησε ο κύριος Ηλίας Τάρλας, πιλότος της 359 ΜΑΕΔΥ, εκπαιδευτής και ερευνητής της Πολιτικής Αεροπορίας. Τα συμπεράσματα της συγκεκριμένης συνέντευξης διελεύκαναν περισσότερο το μέρος της εργασίας που αφορούσε τις συστάσεις ασφαλείας, που εκδίδονται μετά απο κάθε ατύχημα, καθώς και το παρασκήνιό τους.




```python

```
