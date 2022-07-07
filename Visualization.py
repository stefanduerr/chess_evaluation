import matplotlib.pyplot as plt
import numpy as np

Sg = [5.53, 0.35, -8.91]
Sm = [4.39, 0.81, -11.79]
Ch = [3.24, 0.69, -6.95]
axis = ['Position 1:\nBauernallianz', 'Position 2:\nCarlsen vs. Nepomniatchtchi',  'Position 3:\nSchwarze Übermacht']
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(Sg)) 
print(x) # the label locations
width = 0.30  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-0.3, Sg, width, label='Stockfish (Tiefe=1)')
rects2 = ax.bar(x, Sm, width, label='Stockfish (Tiefe=6)')
rects3 = ax.bar(x+0.3, Ch, width, label='CHEVA v2.0')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Bewertung')
ax.set_title('CHEVA vs. Stockfish')
ax.set_xticks(x, axis)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()