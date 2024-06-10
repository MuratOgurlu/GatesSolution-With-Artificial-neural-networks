import numpy as np

# Sigmoid aktivasyon fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Yapay sinir ağı tahmin fonksiyonu
def predict(X, W1, b1, W2, b2):
    # İlk katman çıkışı
    A1 = sigmoid(np.dot(X, W1) + b1)

    # İkinci katman çıkışı (tahmin)
    A2 = sigmoid(np.dot(A1, W2) + b2)

    return A2.round()

# Veri seti oluşturma
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Etiketler (XOR mantıksal kapısı çıkışları)
y = np.array([[0],
              [1],
              [1],
              [0]])

# Rastgele ağırlık ve bias değerlerini oluşturma
np.random.seed(0)
W1 = np.random.randn(2, 2)  # 2x2 ağırlık matrisi
b1 = np.random.randn(2)     # İki nöron için bias

W2 = np.random.randn(2, 1)  # 2x1 ağırlık matrisi
b2 = np.random.randn(1)     # Tek bir nöron için bias

# Modelin eğitim aşaması
learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # İleri yayılım (forward propagation)
    # İlk katman çıkışı
    A1 = sigmoid(np.dot(X, W1) + b1)

    # İkinci katman çıkışı (tahmin)
    A2 = sigmoid(np.dot(A1, W2) + b2)

    # Kayıp hesaplama
    loss = np.mean(np.square(y - A2))

    # Geriye yayılım (backpropagation)
    # Hata hesaplama
    dA2 = (A2 - y) * A2 * (1 - A2)
    dW2 = np.dot(A1.T, dA2)
    db2 = np.sum(dA2, axis=0)

    dA1 = np.dot(dA2, W2.T) * A1 * (1 - A1)
    dW1 = np.dot(X.T, dA1)
    db1 = np.sum(dA1, axis=0)

    # Ağırlık ve bias güncelleme
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    # Her 1000 epoch'ta bir kaybı yazdırma
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Modelin eğitilmiş ağırlıklarını kullanarak tahminler yapma
predictions = predict(X, W1, b1, W2, b2)

# Sonuçları gösterme
print("\nXOR Kapısı Çıkışları:")
for i in range(len(X)):
    print(X[i], "->", int(predictions[i]))