import streamlit as st
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('~/.juggle/latest.csv')
# st.write(df)
max_time = int(df.time.max())
start_time = st.slider(
    "Timestamp:",
    min_value=0,
    value=0,
    max_value=max_time,
    step=1,
)
end_time = st.slider(
    "Timestamp:",
    min_value=0,
    value=max_time,
    max_value=max_time,
    step=1,
)

df = df.loc[df.time.between(start_time, end_time, inclusive="both"), :]

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(-5, 100)
ax.scatter(df['ball1x'], df['ball1z'], label='ball1', c="r")
ax.scatter(df['ball2x'], df['ball2z'], label='ball2', c="g")
ax.scatter(df['ball3x'], df['ball3z'], label='ball3', c="b")
ax.scatter(df['left_hand_x'], [0]*len(df), marker="x", c='purple', label='left_hand')
ax.scatter(df['right_hand_x'], [0]*len(df), marker="x", c='pink', label='right_hand')

st.pyplot(fig)
