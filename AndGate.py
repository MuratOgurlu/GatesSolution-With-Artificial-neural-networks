import numpy as np

# Sigmoid aktivasyon fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Ağırlıkları ve bias değerini rastgele başlat
np.random.seed(0)
w1, w2, b = np.random.randn(3)

# Eğitim veri seti
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 0, 0, 1])

# Hyperparametreler
learning_rate = 0.1
epochs = 10000

# Eğitim döngüsü
for epoch in range(epochs):
    for i in range(len(X)):
        x1, x2 = X[i]
        target = y[i]
        
        # Nöronun çıkışını hesapla
        z = x1*w1 + x2*w2 + b
        output = sigmoid(z)
        
        # Hatanın hesapla
        error = target - output
        d_w1 = x1 * error
        d_w2 = x2 * error
        d_b = error
        
        # Ağırlıkları güncelle
        w1 += learning_rate * d_w1
        w2 += learning_rate * d_w2
        b += learning_rate * d_b
        # Tek nöron olduğu için geri yayma yok
        
         
# Eğitim sonrası ağırlıkları kullanarak AND kapısını tahmin et
print("AND Kapısı Çıkışları:")
print("0 AND 0 ->", round(sigmoid(0*w1 + 0*w2 + b)))
print("0 AND 1 ->", round(sigmoid(0*w1 + 1*w2 + b)))
print("1 AND 0 ->", round(sigmoid(1*w1 + 0*w2 + b)))
print("1 AND 1 ->", round(sigmoid(1*w1 + 1*w2 + b)))