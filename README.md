# Proyek UAS Kecerdasan Buatan (Kelas C)

**Dosen Pengampu:** Dr. Raden Arief Setyawan, ST., MT.
**Nama Mahasiswa:** Putri Sekar Arum

---

## 1. Penjelasan Proyek

Proyek ini mengimplementasikan algoritma **Random Forest** untuk memprediksi hasil pertandingan menembak berdasarkan beberapa parameter performa atlet. Sistem melakukan klasifikasi hasil pertandingan menjadi dua kategori, yaitu **Menang** dan **Kalah**.

Parameter yang digunakan dalam proses prediksi meliputi:

* Akurasi tembakan (%)
* Waktu reaksi (detik)
* Jarak target (meter)
* Jumlah tembakan tepat sasaran

Tujuan dari sistem ini adalah membantu melakukan analisis performa atlet menembak serta memberikan prediksi hasil pertandingan berdasarkan data yang tersedia.

## 2. Dataset atau Link Dataset

* **Total Data:** 300 Data
* **Jenis Data:** Data simulasi pertandingan menembak
* **Fitur yang Digunakan:**

  * Akurasi
  * Waktu Reaksi
  * Jarak Target
  * Tembakan Tepat
* **Target Klasifikasi:**

  * Menang
  * Kalah

**Pembagian Data:**

* 80% Data Training (240 data)
* 20% Data Testing (60 data)

Dataset dibuat menggunakan Python dan disimpan dalam format CSV untuk proses pelatihan model.

## 3. Hasil Evaluasi Model

Model dilatih menggunakan algoritma **Random Forest Classifier** dari library Scikit-Learn. Setelah proses training dan testing, model dievaluasi menggunakan **Accuracy Score** dan **Confusion Matrix**.

Berdasarkan hasil pengujian, model mampu melakukan klasifikasi hasil pertandingan menembak dengan tingkat akurasi yang sangat baik. Confusion Matrix menunjukkan bahwa sebagian besar data berhasil diprediksi dengan benar oleh model.

Berikut adalah visualisasi **Confusion Matrix**:

![Confusion Matrix](confusion_matrix.png)

## 4. Link Video Demo (3–5 Menit)

[KLIK DI SINI UNTUK MENONTON VIDEO DEMO PROYEK](TULIS_LINK_VIDEO_YOUTUBE_ATAU_GOOGLE_DRIVE_DI_SINI)

## 5. Teknologi yang Digunakan

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Random Forest Classifier

## 6. Kesimpulan

Berdasarkan hasil implementasi dan evaluasi, algoritma Random Forest berhasil digunakan untuk memprediksi hasil pertandingan menembak berdasarkan parameter performa atlet. Model menunjukkan performa yang baik dalam melakukan klasifikasi sehingga dapat digunakan sebagai contoh penerapan Machine Learning pada bidang olahraga.
