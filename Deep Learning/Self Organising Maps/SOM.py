# Self Organising Maps

# Importing the usual suspects
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
creadit_card_df = pd.read_csv('dataset/Credit_Card_Applications.csv')
X = creadit_card_df.iloc[:, :-1].values
y = creadit_card_df.iloc[:, -1].values

# Feature scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Building and training the SOM
from minisom import MiniSom

som = MiniSom(x=20, y=20, input_len=15, sigma=1.0, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(data=X, num_iteration=100)

# Visualising Results
from pylab import bone, pcolor, plot, show, colorbar

plt.figure(figsize=(14, 12))
bone()
pcolor(som.distance_map().T,  cmap='YlGn')
colorbar()
markers = ['x', 'o']
colors = ['#E41A1C', '#377EB8']
for idx, vector in enumerate(X):
    winning_node = som.winner(vector)
    plot(winning_node[0] + 0.5,
         winning_node[1] + 0.5,
         markers[y[idx]],
         markeredgecolor=colors[y[idx]],
         markerfacecolor='None',
         markersize=6,
         markeredgewidth=2,
         alpha=0.8)
show()

# Finding the frauds
mappings = som.win_map(X)
frauds = np.concatenate([mappings[(11, 1)], mappings[(4, 1)]], axis=0)
frauds = scaler.inverse_transform(frauds)
