# Project Phase 1-3 Report

## GitHub Link
**[Insert your GitHub repository link here]**

---

## Project Overview
This project upgrades an existing monolithic Django "Wiki" application into a two-tier architecture. The web application handles frontend logic and API interactions running within a Gunicorn server, while the backend relies on a robust PostgreSQL database to persist encyclopedic entries or related data. The application is fully containerized using an optimized, multi-stage Dockerfile and orchestrated using Kubernetes manifests to run on Minikube with replicas for high availability.

---

## Step-by-Step Instructions

### Application Development & Verifying Local Changes
1. **Prepare Database Settings:** Local connectivity to the DB is handled directly in `wiki/wiki/settings.py` via environment variables.
2. **Review Git Commits:** Run `git log --oneline` to see the incremental commit history confirming development progression.

### Phase 2: Docker Containerization
1. Ensure Docker is running locally.
2. Navigate to the project root: `cd /path/to/unix_project`
3. Build the backend and frontend services:
   ```bash
   docker-compose build
   ```
4. Start the application locally:
   ```bash
   docker-compose up -d
   ```
5. *Verify:* Access `http://localhost:8000` to confirm the application functions. Bring instances down with `docker-compose down`.

### Phase 3: Kubernetes Orchestration
1. Ensure Minikube is started: `minikube start`
2. Load the newly built Docker image into Minikube (so K8s doesn't try to pull it from Docker Hub):
   ```bash
   minikube image load django-app-image:latest
   minikube image load postgres:15-alpine
   ```
3. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/postgres-deployment.yaml
   kubectl apply -f k8s/django-deployment.yaml
   kubectl apply -f k8s/django-service.yaml
   ```
4. Check the rollout status of pods and services:
   ```bash
   kubectl get pods -l app=django-app
   kubectl get svc django-service
   ```
5. Access the application via Minikube (since it uses a NodePort):
   ```bash
   minikube service django-service
   ```

---

## Proof of Execution (Screenshots)

*Please replace the placeholders below with the requested screenshots.*

1. **Screenshot 1: Docker Build Success**
   *(Paste screenshot of successful `docker-compose build` run or resulting images)*

2. **Screenshot 2: Running Application Locally**
   *(Paste screenshot of `docker-compose up` logs or browser at `localhost:8000`)*

3. **Screenshot 3: Kubernetes Pods Running**
   *(Paste screenshot of output for `kubectl get pods` showing 2 django replicas and 1 postgres pod)*

4. **Screenshot 4: Kubernetes Service Access**
   *(Paste screenshot of output for `minikube service django-service` or browser successfully loading the app via minikube URL)*

5. **Screenshot 5: Git Commit History**
   *(Paste screenshot of `git log --oneline` showing multiple incremental commits)*
