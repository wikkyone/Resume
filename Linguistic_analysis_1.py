import pandas as pd
import torch
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification

filename = "cafe_reviews.csv"
model_name = 'blanchefort/rubert-base-cased-sentiment'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def analyze_sentiment(text):
    """Анализ тональности текста с преобразованием меток"""
    inputs = tokenizer(
        text, 
        padding=True, 
        truncation=True, 
        max_length=512, 
        return_tensors='pt'
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Преобразование выходов модели: [0=Neutral, 1=Positive, 2=Negative] 
    predicted_label = torch.argmax(outputs.logits).item()
    return {0: 2, 1: 0, 2: 1}[predicted_label]

df = pd.read_csv(filename)

# Применение модели к текстам
df['predicted_sentiment'] = df['text'].apply(analyze_sentiment)

sentiment_labels = ['Neutral', 'Positive', 'Negative']
counts = df['predicted_sentiment'].value_counts().reindex([0, 1, 2], fill_value=0)
# Создание графиков
plt.figure(figsize=(10, 6))
bars = plt.bar(
    sentiment_labels,
    counts,
    color=['gray', 'green', 'red'],
    edgecolor='black'
)

plt.title('Распределение тональности отзывов (Predicted)', fontsize=14)
plt.xlabel('Тональность', fontsize=12)
plt.ylabel('Количество отзывов', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Добавление значений на столбцы
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2., 
        height, 
        f'{int(height)}', 
        ha='center', 
        va='bottom',
        fontsize=10
    )

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()