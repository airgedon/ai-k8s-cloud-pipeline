#  AI 추론 API 기반 클라우드 & Kubernetes 자동 배포 파이프라인

FastAPI를 활용한 AI 모델 추론 백엔드 서비스를 구축하고, Docker 컨테이너화 및 Kubernetes 오케스트레이션을 통해 클라우드 환경에 안정적으로 배포하는 엔드투엔드(End-to-End) 프로젝트입니다.

---

## 주요 기술 스택 (Tech Stack)

- **Backend & AI:** Python, FastAPI, Hugging Face (Transformers), PyTorch
- **Container & Orchestration:** Docker, Kubernetes (CKA)
- **Cloud Infrastructure:** AWS (EC2, S3)
- **CI/CD & Version Control:** GitHub Actions, Git

---

## 시스템 아키텍처 (System Architecture)

[ 사용자 요청 ]
│
▼
[ FastAPI 백엔드 ] ──► [ AI 추론 모델 (Hugging Face) ]
│
▼
[ Docker 컨테이너 ]
│
▼
[ Kubernetes 클러스터 (Deployment / NodePort Service) ] ──► [ AWS EC2 ]

---

## 핵심 구현 사항

1. **FastAPI 기반 RESTful API 구축**
   - AI 추론 엔드포인트 (`/predict`) 및 시스템 상태 점검 엔드포인트 (`/health`) 구현
2. **컨테이너화 및 경량화**
   - Python Slim 이미지를 활용한 최적화된 `Dockerfile` 작성
3. **Kubernetes 기반의 안정적 운영 (CKA 역량 활용)**
   - 2개의 Replica를 통한 고가용성 보장
   - `livenessProbe`를 통한 자가 치유(Self-healing) 인프라 구축
   - CPU/Memory Resource Limit 설정으로 시스템 안정성 확보

---

## 실행 방법 (Getting Started)

### 1. 로컬 환경 실행
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
