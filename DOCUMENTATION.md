Αρχικά, έχουμε παραθέσει όλα τα στάδια του scraping, cleaning analysing σε αρχεία jupyter notebook. Η σειρά με την οποία διαβάζονται είναι η εξής: 

1. multiple_pages_scraping_incidents.ipynb => all_incidents.csv
2. all_incidents_cleaned.ipynb => all_incidents_cleaned.csv
3. final_data_cleaned.ipynb => fatalities.csv
4. Απο το fatalities.csv προκύπτουν τα επιμέρους incidents_injuries.csv, fatal_injuries.csv

Όσον αφορά τα τελικά μας αρχεία η βασική πορεία που ακολουθήσαμε είναι:

#### final_data_cleaned.ipynb => fatalities.csv

- **df** (= pd.read_csv('all_incidents_cleaned.csv))

*Το αρχικό df μας ισούται  με το αρχείο csv που έχουμε αντλήσει απο το scraping/cleaning που έχει προηγηθεί. Έτσι, δίνουμε εντολή στο pandas να το διαβάσει* 

- **df['Year']** (= pd.to_datetime(df.incident_date).dt.year) 

*Δημιουργήσαμε μια επιπλέον στήλη, στην οποία ομαδοποιήσαμε τις χρονολογίες, απο την original στήλη(incident_date)*

- **fatalities** (= df.groupby('Year').fatalities.value_counts().unstack().reset_index() )

*Εδώ, φτιάξαμε το καινούριο df, με όνομα fatalities, που ουσιαστικά αποτελεί έναν πίνακα που aπεικονίζει οι θάνατοι ανά έτος*

- **fatalities['all_incidents']** (= fatalities[['Θανάσιμος τραυματισμός', 'Μικρός τραυματισμός','Σοβαρός τραυματισμός', 'Χωρίς Τραυματισμό']].sum(axis=1))  

*Επιπρόσθετη στήλη με τον συνολικό αριθμό των ατυχημάτων ανά έτος*

- **df1** (= fatalities),**fatalities_pd** (= pd.DataFrame(fatalities))

*Επίσημα μετατρέψαμε το fatalities σε DataFrame, df1 αυτή τη φορά, για να το ξεχωρίζουμε απο το αρχικό.*

- **df1** (= df1.fillna(0))

*Αντικαθιστούμε τα missing values NaN με 0, έτσι ώστε να μπορέσουμε να συγχωνεύσουμε ακριβέστερα τις δύο στήλες με τους τραυματισμούς, όπως βλέπουμε παρακάτω*

- **fatalities_pd.rename(columns = {'Θανάσιμος τραυματισμός':'fatal_injuries','Μικρός τραυματισμός': 'minor_injuries', 'Σοβαρός τραυματισμός' :'serious_injuries', 'Χωρίς Τραυματισμό' : 'no_injuries'}, inplace = True)**

*Μετονομάσαμε τα ελληνικά labels των columns για καλύτερη λειτουργικότητα αργότερα:))*

- **df1["total_injuries"]** (=df1["minor_injuries"]+df1["serious_injuries"]) 

*Επιπρόσθετη στήλη με το σύνολο των τραυματισμών πλην των θανάσιμων, κάνοντας merge τα columns "minor_injuries" και "serious_injuries"*

- **df1['minor_injuries']** (= df1['minor_injuries'].apply(np.int64))
- **df1['serious_injuries']** (= df1['serious_injuries'].apply(np.int64))
- **df1['fatal_injuries']** (= df1['fatal_injuries'].apply(np.int64))
- **df1['all_incidents']** (= df1['all_incidents'].apply(np.int64))
- **df1['total_injuries']** (= df1['total_injuries'].apply(np.int64))
- **df1['no_injuries']** (= df1['no_injuries'].apply(np.int64))

*Μετατρέψαμε όλα τα δεδομένα των columns του df1, απο float σε integer για να διευκολυνθούμε μελλοντικά(εκτός απο το 'Year', καθώς ήταν ήδη σε integer form)*

- **df2** (= df.drop(['fatal_injuries','minor_injuries','serious_injuries','no_injuries'],axis=1))

*Εδώ σε ξεχωριστό notebook αφαιρέσαμε τις παραπάνω στήλες, έτσι ώστε να έχουμε ένα df μόνο με την αναλογία των ατυχημάτων και των τραυματισμών ανά έτος*

- **df3** (= df.drop(['minor_injuries','serious_injuries','no_injuries', 'all_incidents', 'total_injuries'],axis=1))

*Eδώ αφαιρέσαμε διαφορετικές, ετσι ώστε να έχουμε ένα df με τους θανάτους ανά έτος*

Οι τελευταίες εντολές εξυπηρέτησαν την ακριβέστερη οπτικοποίηση των δεδομένων, με τα οποία θέλαμε να εμπλουτίσουμε το story μας






 



```python

```
