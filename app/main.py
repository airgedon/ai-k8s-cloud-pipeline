from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_text

app = FastAPI(
    title="AI 추론 백엔드 API",
    description="FastAPI 기반의 AI 모델 추론 및 클라우드 배포 파이프라인"
)

class TextRequest(BaseModel):
    text: str

@app.get("/health", summary="헬스 체크")
def health_check():
    return {"status": "healthy", "message": "서비스가 정상 작동 중입니다."}

@app.post("/predict", summary="AI 모델 추론 요청")
def predict(request: TextRequest):
    result = predict_text(request.text)
    return {"input_text": request.text, "prediction": result}
