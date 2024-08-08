### Submission 2: Machine Learning Pipeline - AIDS Virus Infection Prediction 💉
Nama: Jericho Luthfi Syahli

Username dicoding: jericho_luthfi_ihFK

| | Deskripsi |
| ----------- | ----------- |
| **Dataset** | [AIDS Virus Infection Prediction](https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction/data) |
| **Masalah** | Prediksi apakah seorang pasien dengan AIDS terinfeksi atau tidak berdasarkan berbagai fitur klinis dan demografis. |
| **Solusi machine learning** | Solusi menggunakan model machine learning untuk memprediksi infeksi pada pasien AIDS dengan memanfaatkan fitur-fitur seperti waktu perawatan, jenis perawatan, usia, berat badan, dan berbagai pengukuran kesehatan lainnya. |
| **Metode pengolahan** | Metode pengolahan data meliputi pembersihan data, transformasi fitur, dan pembagian data menjadi set pelatihan dan set pengujian. Data kemudian diubah menjadi format yang dapat diterima oleh TensorFlow Serving untuk prediksi. |
| **Arsitektur model** | Arsitektur model yang digunakan adalah jaringan saraf tiruan (Neural Network) dengan beberapa lapisan tersembunyi yang menggunakan aktivasi ReLU dan satu lapisan output dengan aktivasi sigmoid untuk klasifikasi biner. |
| **Metrik evaluasi** | Metrik evaluasi yang digunakan adalah akurasi biner (binary accuracy), AUC (Area Under the Curve), precision, dan recall untuk mengukur performa model dalam memprediksi infeksi. |
| **Performa model** | Model menunjukkan akurasi yang baik pada data pengujian dengan AUC yang tinggi, menunjukkan kemampuan model dalam membedakan antara pasien yang terinfeksi dan tidak terinfeksi. |
| **Opsi deployment** | Model di-deploy menggunakan TensorFlow Serving di platform Railway, yang memungkinkan model diakses melalui endpoint REST API untuk prediksi secara real-time. |
| **Web app** | [AIDS-Model](https://jericholuthfiihfk-pipeline-production.up.railway.app/v1/models/aids-model/metadata) |
| **Monitoring** | Hasil monitoring dari model serving menunjukkan bahwa model memberikan prediksi secara konsisten dengan waktu respons yang cepat. Monitoring dilakukan untuk memastikan bahwa endpoint model tetap tersedia dan performa prediksi tetap optimal. |
