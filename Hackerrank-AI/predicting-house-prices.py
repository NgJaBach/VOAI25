import numpy as np 
from sklearn.linear_model import LinearRegression

# Read input
F, N = map(int, input().split())

# Read training data
X_train = []
y_train = []

for _ in range(N):
    *features, price = map(float, input().split())
    X_train.append(features)
    y_train.append(price)
    
# Read test data
T = int(input())
X_test = [list(map(float, input().split())) for _ in range(T)]

# To numpy array
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

for p in pred:
    print(f"{p:.2}")
