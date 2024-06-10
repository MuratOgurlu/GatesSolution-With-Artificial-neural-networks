# Yapay Sinir Ağı / Artificial Neural Network (ANN)

![Perceptron](https://www.allaboutcircuits.com/uploads/articles/how-to-train-a-basic-perceptron-neural-network_rk_aac_image1.jpg)

Bu proje, yapay sinir ağlarının (Artificial Neural Network - ANN) temel prensiplerini ve nasıl çalıştığını açıklamaktadır. Yapay sinir ağları, biyolojik sinir ağlarının bilgi işleme şeklinden esinlenilmiş hesaplamalı modellerdir.

This project explains the fundamental principles of Artificial Neural Networks (ANNs) and how they work. ANNs are computational models inspired by the way biological neural networks process information in the human brain.

## Ana Bileşenler / Key Components

1. **Nöronlar (Düğümler) / Neurons (Nodes):**
   - **Giriş Nöronları / Input Neurons:** Giriş verilerini alır. / Receive input data.
   - **Gizli Nöronlar / Hidden Neurons:** Giriş verilerini dönüştürerek çıktı katmanına kullanılabilir hale getirir. / Intermediate processing units that transform input into something the output layer can use.
   - **Çıkış Nöronları / Output Neurons:** Nihai sonuç veya çıktıyı üretir. / Produce the final result or output.

2. **Katmanlar / Layers:**
   - **Giriş Katmanı / Input Layer:** Verilerin ağa girdiği ilk katmandır. / The first layer where the data enters the network.
   - **Gizli Katmanlar / Hidden Layers:** Bir veya daha fazla katman olup, bu katmanlarda hesaplamalar gerçekleştirilir. Bu katmanlar, verilerdeki karmaşık desenleri yakalar. / One or more layers where computations are performed. These layers capture the complex patterns in the data.
   - **Çıkış Katmanı / Output Layer:** Ağın nihai çıktısını sağlayan son katmandır. / The final layer that provides the output of the network.

3. **Ağırlıklar ve Biaslar / Weights and Biases:**
   - **Ağırlıklar / Weights:** Eğitim sırasında ayarlanan ve giriş verilerinin ağda nasıl işlendiğini etkileyen parametrelerdir. / Parameters that adjust during training, influencing how input data is transformed as it passes through the network.
   - **Biaslar / Biases:** Modelin verileri daha iyi uyarlamasına yardımcı olmak için nöronların çıktısına eklenen ek parametrelerdir. / Additional parameters that are added to the neurons' output to help the model fit the data better.

4. **Aktivasyon Fonksiyonları / Activation Functions:**
   - Her nöronun çıktısına uygulanan ve ağın karmaşık desenleri öğrenmesini sağlayan doğrusal olmayan fonksiyonlardır. Yaygın aktivasyon fonksiyonları arasında ReLU (Rectified Linear Unit), Sigmoid ve Tanh bulunur. / Functions applied to the output of each neuron to introduce non-linearity, enabling the network to learn complex patterns. Common activation functions include ReLU (Rectified Linear Unit), Sigmoid, and Tanh.

## Yapay Sinir Ağlarının Çalışma Prensipleri / How ANNs Work

1. **Başlangıç / Initialization:**
   - Ağ, rastgele atanmış ağırlıklar ve biaslarla başlar. / The network starts with randomly assigned weights and biases.

2. **İleri Yayılım (Forward Propagation):**
   - Veriler, giriş katmanından başlayarak gizli katmanlar üzerinden çıkış katmanına doğru ağda ilerler. Her nöron, giriş verilerini işler, ağırlıklar ve biasları uygular, toplar ve sonucu bir aktivasyon fonksiyonundan geçirir. / Data passes through the network from the input layer, through the hidden layers, to the output layer. Each neuron processes the input data, applies weights and biases, sums them up, and passes the result through an activation function.

3. **Kayıp Hesaplama / Loss Calculation:**
   - Ağın çıktısı, gerçek hedef değerlerle bir kayıp fonksiyonu (örneğin, Ortalama Kare Hata, Çapraz Entropi Kaybı) kullanılarak karşılaştırılır. Bu adım, ağın tahminlerinin gerçek değerlerden ne kadar uzak olduğunu ölçer. / The network’s output is compared to the actual target values using a loss function (e.g., Mean Squared Error, Cross-Entropy Loss). This step quantifies how far the network's predictions are from the actual values.

4. **Geri Yayılım (Backpropagation):**
   - Ağ, kayıplara göre ağırlık ve biaslarını ayarlar. Gradyan inişi kullanılarak, kayıp fonksiyonunun her ağırlık ve bias için gradyanı hesaplanır ve bunlar kaybı minimize edecek şekilde güncellenir. / The network adjusts its weights and biases based on the loss. Using gradient descent, the network computes the gradient of the loss function with respect to each weight and bias, updating them to minimize the loss.

5. **İterasyon / Iteration:**
   - Adımlar 2-4, ağın performansı tatmin edici olana kadar birçok kez (epoch) tekrarlanır. / Steps 2-4 are repeated for many iterations (epochs) until the network's performance is satisfactory.

## Uygulamalar / Applications

- **Bilgisayarlı Görü / Computer Vision:** Görüntü tanıma, nesne algılama, yüz tanıma. / Image recognition, object detection, facial recognition.
- **Doğal Dil İşleme (NLP) / Natural Language Processing (NLP):** Metin üretimi, duygu analizi, dil çevirisi. / Text generation, sentiment analysis, language translation.
- **Konuşma Tanıma / Speech Recognition:** Konuşulan dili metne dönüştürme. / Converting spoken language into text.
- **Otonom Sistemler / Autonomous Systems:** Otonom araçlar, robotik sistemler. / Self-driving cars, robotics.
- **Sağlık / Healthcare:** Hastalık tahmini, tıbbi görüntü analizi. / Disease prediction, medical image analysis.

## Avantajlar / Advantages

- **Öğrenme Yeteneği / Learning Capability:** Verilerdeki karmaşık desenleri öğrenme ve modelleme yeteneği. / Can learn and model complex patterns in data.
- **Uyarlanabilirlik / Adaptability:** Yeni, görülmemiş verilere uyum sağlama kapasitesi. / Capable of adapting to new, unseen data.
- **Otomasyon / Automation:** Manuel özellik çıkarımı ve kural tabanlı programlamayı azaltır. / Reduces the need for manual feature extraction and rule-based programming.

## Zorluklar / Challenges

- **Hesaplama Kaynakları / Computational Resources:** Büyük ağlar için önemli ölçüde hesaplama gücü gerektirir. / Requires significant computational power, especially for large networks.
- **Veri Gereksinimleri / Data Requirements:** Eğitim için büyük miktarda etiketlenmiş veri gerektirir. / Needs large amounts of labeled data for training.
- **Yorumlanabilirlik / Interpretability:** Modelin iç işleyişini anlamak genellikle zordur ("kara kutu" olarak adlandırılır). / Often considered a "black box" due to the difficulty in understanding the internal workings of the model.

Bu projede, yapay sinir ağlarının temelleri ele alınmakta ve bu ağların nasıl çalıştığı ayrıntılı olarak açıklanmaktadır. Yapay sinir ağları, geleneksel programlama yöntemleriyle gerçekleştirilemeyen veya pratik olmayan görevleri mümkün kılarak birçok alanda devrim yaratmıştır.

This project covers the basics of artificial neural networks and explains how they work in detail. ANNs have revolutionized many fields by enabling tasks that were previously impossible or impractical with traditional programming methods.


# Mantık Kapıları (Logic Gates) / Logic Gates

Bu proje, mantık kapılarının temel prensiplerini ve nasıl çalıştıklarını açıklamaktadır. Mantık kapıları, dijital devrelerin temel yapı taşlarıdır ve çeşitli mantıksal işlemleri gerçekleştirmek için kullanılır.

This project explains the fundamental principles of logic gates and how they work. Logic gates are the basic building blocks of digital circuits and are used to perform various logical operations.

## Mantık Kapıları Nedir? / What are Logic Gates?

Mantık kapıları, bir veya daha fazla girişten ve bir çıkıştan oluşan dijital devre elemanlarıdır. Her bir kapı, belirli bir mantıksal işlemi gerçekleştirir ve bu işlemi gerçekleştirirken giriş sinyallerine dayanır.

Logic gates are digital circuit components that consist of one or more inputs and one output. Each gate performs a specific logical operation based on its input signals.

## Temel Mantık Kapıları / Basic Logic Gates

### VE Kapısı (AND Gate)

- **Türkçe:** VE kapısı, tüm girişler 1 olduğunda çıkışı 1 olan bir mantık kapısıdır. Aksi takdirde çıkışı 0'dır.
- **İngilizce:** The AND gate is a logic gate that outputs 1 when all inputs are 1. Otherwise, the output is 0.

**Sembol / Symbol:** 

<img src="https://www.vedantu.com/question-sets/34cb5291-c2c8-4a5a-9b43-2bcfa76071606917240058642263338.png" alt="AND Gate" width="200"/>

**Doğruluk Tablosu / Truth Table:**

| A | B | Çıkış / Output |
|---|---|----------------|
| 0 | 0 | 0              |
| 0 | 1 | 0              |
| 1 | 0 | 0              |
| 1 | 1 | 1              |

### VEYA Kapısı (OR Gate)

- **Türkçe:** VEYA kapısı, herhangi bir giriş 1 olduğunda çıkışı 1 olan bir mantık kapısıdır. Tüm girişler 0 ise çıkışı 0'dır.
- **İngilizce:** The OR gate is a logic gate that outputs 1 when any input is 1. If all inputs are 0, the output is 0.

**Sembol / Symbol:**

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfewwuFY3BCKdp0WI_1K5Nru1y1Og4UmMpvA&s" alt="OR Gate" width="200"/>

**Doğruluk Tablosu / Truth Table:**

| A | B | Çıkış / Output |
|---|---|----------------|
| 0 | 0 | 0              |
| 0 | 1 | 1              |
| 1 | 0 | 1              |
| 1 | 1 | 1              |

### XOR Kapısı (XOR Gate)

- **Türkçe:** XOR kapısı, girişlerden yalnızca biri 1 olduğunda çıkışı 1 olan bir mantık kapısıdır. Diğer durumlarda çıkışı 0'dır.
- **İngilizce:** The XOR gate is a logic gate that outputs 1 when only one of the inputs is 1. In other cases, the output is 0.

**Sembol / Symbol:**

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiFVAcCLlTViT4jqqMopN_DDmBVwXbcdVfnQ&s" alt="OR Gate" width="200"/>

**Doğruluk Tablosu / Truth Table:**

| A | B | Çıkış / Output |
|---|---|----------------|
| 0 | 0 | 0              |
| 0 | 1 | 1              |
| 1 | 0 | 1              |
| 1 | 1 | 0              |

## Uygulamalar / Applications

- **Dijital Devreler / Digital Circuits:** Mantık kapıları, bilgisayarlar, mikroişlemciler ve diğer dijital sistemlerde temel bileşenler olarak kullanılır.
- **Boolean Algebra / Boole Cebiri:** Mantık kapıları, Boole cebiri ifadelerinin uygulanmasında kullanılır.
- **Kontrol Sistemleri / Control Systems:** Mantık kapıları, endüstriyel kontrol sistemlerinde ve otomasyon projelerinde yaygın olarak kullanılır.

Mantık kapıları, dijital elektroniğin temelini oluşturur ve modern teknolojinin birçok alanında hayati bir rol oynar. Bu proje, mantık kapılarının ne olduğunu, nasıl çalıştıklarını ve nerelerde kullanıldıklarını anlamak için temel bir rehber sağlar.

Logic gates form the foundation of digital electronics and play a crucial role in many areas of modern technology. This project provides a basic guide to understanding what logic gates are, how they work, and where they are used.
