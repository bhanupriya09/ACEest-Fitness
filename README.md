# ACEest Fitness & Gym – DevOps CI/CD Implementation

## Overview
A full CI/CD pipeline for a Flask-based gym management app using **Git, Jenkins, Docker, SonarQube, Kubernetes, and Pytest.**

### Tech Stack
- Flask (Python)
- Jenkins (CI/CD)
- SonarQube (Code Quality)
- Docker (Containerization)
- Kubernetes via Minikube (Deployment)
- Docker Hub (Image Registry)

## Run Locally
```bash
pip install -r requirements.txt
python ACEest_Fitness.py

Run Tests
pytest -q

Build Docker Image
docker build -t aceest-fitness:latest .
docker run -p 5000:5000 aceest-fitness:latest

Deploy to Minikube
kubectl apply -f k8s/
kubectl get pods
minikube service aceest-service

CI/CD Pipeline Summary

Code push triggers Jenkins pipeline.

Jenkins runs Pytest and SonarQube.

Docker image built & pushed to Docker Hub.

Kubernetes deploys via Rolling or Blue-Green strategy.

Rollback with:

kubectl rollout undo deployment/aceest-app
