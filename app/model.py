from transformers import pipeline

# Hugging Face의 경량화 텍스트 감정 분석 모델 로드
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_text(text: str):
    return classifier(text)[0]
