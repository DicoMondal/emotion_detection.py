import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emotion_dataset.csv")


def detect_emotion(input_text):
    input_text = input_text.lower()
    emotion_count = {"happy": 0, "sad": 0, "angry": 0}

    for index, row in df.iterrows():
        if row['text'].lower() in input_text:
            emotion_count[row['emotion']] += 1

    if all(v == 0 for v in emotion_count.values()):
        return "Emotion not found"

    return max(emotion_count, key=emotion_count.get)

user_input = input("Enter a sentence: ")
result = detect_emotion(user_input)

print("Detected Emotion:", result)

def visualize_emotions():
    emotion_freq = df['emotion'].value_counts()
    emotion_freq.plot(kind='bar', color=['green', 'blue', 'red'])
    plt.title("Emotion Distribution in Dataset")
    plt.xlabel("Emotion")
    plt.ylabel("Frequency")
    plt.show()

