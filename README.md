# 🎬 Movie Watchlist — DevOps Mini-Project

A lightweight, automated DevOps practical demonstration featuring a Flask-based **Movie Watchlist** web service.

---

## 📌 Project Overview & Pipeline
This project demonstrates an end-to-end continuous integration and deployment (CI/CD) workflow:

```
GitHub ──▶ Jenkins (CI) ──▶ Automated Tests (pytest) ──▶ Docker Container ──▶ AWS EC2 (Ubuntu) ──▶ Health Check
```

- **Application:** Movie Watchlist API built using Flask.
- **Testing:** Automated unit and route testing via `pytest`.
- **CI Server:** Jenkins pipeline automatically checks out code, sets up a virtual environment, installs dependencies, and runs tests.
- **Containerization:** Docker packages the application into an isolated, lightweight container.
- **Cloud Deployment:** Hosted on an AWS EC2 Ubuntu instance accessible via port `5000`.
- **Monitoring:** `/health` endpoint for uptime verification.

---

## 🛠️ Application Endpoints

| Endpoint | Method | Description | Sample Output |
| :--- | :---: | :--- | :--- |
| `/` | GET | Welcome message & available route directory | `{"message": "Welcome to the Personal Movie Watchlist Tracker API!", ...}` |
| `/watchlist` | GET | List of planned movies with title, genre, year | `{"total_movies": 3, "movies": [...]}` |
| `/top-pick` | GET | Tonight's featured movie recommendation | `{"recommendation": {"title": "Inception", ...}}` |
| `/health` | GET | DevOps health-check endpoint | `{"status": "healthy"}` |

---

## 🚀 Local Setup & Testing

### 1. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Automated Tests
```bash
pytest -v
```

### 4. Run Application Locally
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

---

## 🐳 Docker Commands

### 1. Build the Docker Image
```bash
docker build -t movie-watchlist-app .
```

### 2. Run the Container
```bash
docker run -d -p 5000:5000 --name movie-app movie-watchlist-app
```

### 3. Check Running Container & Logs
```bash
docker ps
docker logs movie-app
```

---

## ☁️ AWS EC2 Deployment Steps

1. Launch an **Ubuntu 22.04 / 24.04 LTS** EC2 instance on AWS.
2. Configure **Security Group** Inbound Rules:
   - **Port 22 (SSH):** Anywhere (`0.0.0.0/0`) or My IP.
   - **Port 5000 (Flask/Docker):** Custom TCP, Port 5000 from Anywhere (`0.0.0.0/0`).
   - **Port 8080 (Jenkins):** Custom TCP, Port 8080 from Anywhere (`0.0.0.0/0`).
3. Connect to the EC2 terminal via SSH or EC2 Instance Connect.
4. Install Docker:
   ```bash
   sudo apt update && sudo apt install -y docker.io git
   sudo systemctl start docker
   sudo systemctl enable docker
   sudo usermod -aG docker $USER
   ```
5. Clone repository and run container:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd movie-watchlist-devops
   docker build -t movie-watchlist-app .
   docker run -d -p 5000:5000 --name movie-app movie-watchlist-app
   ```
6. Access application in your browser:
   - `http://<EC2_PUBLIC_IP>:5000`
   - `http://<EC2_PUBLIC_IP>:5000/watchlist`
   - `http://<EC2_PUBLIC_IP>:5000/top-pick`
   - `http://<EC2_PUBLIC_IP>:5000/health`
