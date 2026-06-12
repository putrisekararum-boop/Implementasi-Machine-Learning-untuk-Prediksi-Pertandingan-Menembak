import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt

# Membuat dataset 300 data
np.random.seed(42)

data = []

for i in range(300):

    akurasi = np.random.randint(60,101)
    reaksi = round(np.random.uniform(0.5,2.0),2)
    jarak = np.random.choice([10,15,20])
    tepat = np.random.randint(20,51)

    if akurasi >= 85 and tepat >= 40:
        hasil = 1
    else:
        hasil = 0

    data.append([akurasi, reaksi, jarak, tepat, hasil])

df = pd.DataFrame(data, columns=[
    'Akurasi',
    'Waktu_Reaksi',
    'Jarak',
    'Tembakan_Tepat',
    'Hasil'
])

df.to_csv('dataset_menembak.csv', index=False)

X = df[['Akurasi',
        'Waktu_Reaksi',
        'Jarak',
        'Tembakan_Tepat']]

y = df['Hasil']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

akurasi_model = accuracy_score(y_test,y_pred)

print("Akurasi Model :",akurasi_model)

cm = confusion_matrix(y_test,y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Kalah","Menang"]
)

disp.plot()

plt.title("Confusion Matrix")
plt.show()

# Contoh prediksi
data_baru = [[92,0.7,10,47]]

prediksi = model.predict(data_baru)

if prediksi[0] == 1:
    print("Prediksi : MENANG")
else:
    print("Prediksi : KALAH")

    df.to_csv('dataset_menembak.csv', index=False)