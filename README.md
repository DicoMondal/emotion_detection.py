# 🧠 Emotion Detection from Text using Python

This is a simple Python project that detects basic human emotions (like `happy`, `sad`, `angry`) from user-input text using basic Python tools — no machine learning needed!

## 📁 Project Structure

emotion-detection/
├── emotion\_dataset.csv       # Dataset with text and labeled emotions
├── emotion\_detection.py      # Main Python script for detecting emotions
└── README.md                 # Project documentation (this file)


## 🚀 Features

- ✅ Detects emotions from user input using sentence matching
- ✅ Uses `pandas` to handle CSV data
- ✅ Simple logic with `if`, `for`, and `functions`
- ✅ Optional bar chart using `matplotlib`

## 🔧 Requirements

Install the necessary packages using:

```bash
pip install pandas matplotlib
````

## ▶️ How to Run

1. Make sure `emotion_dataset.csv` and `emotion_detection.py` are in the **same folder**.
2. Run the script using:

```bash
python emotion_detection.py
```

3. Enter a sentence like:

```
Enter a sentence: I am so sad and lonely
Detected Emotion: sad


## 📊 Dataset Preview (`emotion_dataset.csv`)

```csv
text,emotion
I am feeling great today,happy
I am so sad and depressed,sad
I hate everything,angry
...
```

It contains 35 real-life emotional expressions with one of these labels: `happy`, `sad`, or `angry`.

---

## 💻 Code Overview (`emotion_detection.py`)

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("emotion_dataset.csv")

def detect_emotion(input_text):
    input_text = input_text.lower()
    emotion_count = {"happy": 0, "sad": 0, "angry": 0}

    for _, row in df.iterrows():
        if row['text'].lower() in input_text:
            emotion_count[row['emotion']] += 1

    if all(v == 0 for v in emotion_count.values()):
        return "Emotion not found"

    return max(emotion_count, key=emotion_count.get)

user_input = input("Enter a sentence: ")
result = detect_emotion(user_input)

print("Detected Emotion:", result)


## 📈 Optional: Visualize Emotions

To show a bar chart of emotions in the dataset:

```python
def visualize_emotions():
    emotion_freq = df['emotion'].value_counts()
    emotion_freq.plot(kind='bar', color=['green', 'blue', 'red'])
    plt.title("Emotion Distribution")
    plt.xlabel("Emotion")
    plt.ylabel("Count")
    plt.show()
```

Just call `visualize_emotions()` at the bottom of the script.

---

## 🛠 Built With

* Python 3
* pandas
* matplotlib
* Basic Python logic (if/else, loops, functions)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

⭐ If you like this project, feel free to give it a star on GitHub!

