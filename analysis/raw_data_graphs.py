import pandas as pd
import matplotlib.pyplot as plt

# Loading data file
df = pd.read_csv('arduino_data.txt', names=['ax', 'ay', 'az', 'gx', 'gy', 'gz'])

# Basic info
print(df.head())
print(df.describe())

# Plot accelerometer data
plt.figure()
plt.plot(df['ax'], label='ax')
plt.plot(df['ay'], label='ay')
plt.plot(df['az'], label='az')
plt.legend()
plt.title('Accelerometer Data')
plt.xlabel('Sample')
plt.ylabel('Acceleration')
plt.show()

# Plot gyroscope data
plt.figure()
plt.plot(df['gx'], label='gx')
plt.plot(df['gy'], label='gy')
plt.plot(df['gz'], label='gz')
plt.legend()
plt.title('Gyroscope Data')
plt.xlabel('Sample')
plt.ylabel('Angular Velocity')
plt.show()

# Roughly smoothing out accelerometer values
df_smooth = df.rolling(window=10).mean()
# Plot smoothed accelerometer data
plt.figure()
plt.plot(df_smooth['ax'], label='ax (smoothed)')
plt.plot(df_smooth['ay'], label='ay (smoothed)')
plt.plot(df_smooth['az'], label='az (smoothed)')
plt.legend()
plt.title('Smoothed Accelerometer Data')
plt.show()
