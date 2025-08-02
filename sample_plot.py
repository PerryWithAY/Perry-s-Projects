import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tem.rawdata1.csv')

plt.plot(df['x'], label='x', color='green')
plt.plot(df['y'], label='y', color='red')
plt.plot(df['z'], label='z', color='blue')

plt.xlabel('Milliseconds')
plt.ylabel('')
plt.title('TEM Plot')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()