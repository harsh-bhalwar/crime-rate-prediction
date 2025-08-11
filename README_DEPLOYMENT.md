# 🚀 Deployment Guide

This guide covers different deployment options for the Crime Rate Prediction API.

## 📋 Prerequisites

- Python 3.8+
- Docker (for containerized deployment)
- Git

## 🐳 Docker Deployment (Recommended)

### Quick Start with Docker Compose

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crime-rate-prediction.git
   cd crime-rate-prediction
   ```

2. **Ensure model files are in the models/ directory**
   ```bash
   ls models/
   # Should show: random_forest.pkl, xgModel.pkl, knnModel.pkl, city_encoder.pkl, knnFeatures.pkl
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the API**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs

### Manual Docker Build

```bash
# Build the image
docker build -t crime-prediction-api .

# Run the container
docker run -p 8000:8000 -v $(pwd)/models:/app/models crime-prediction-api
```

## 🐍 Python Virtual Environment Deployment

### Local Development

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

### Production Server

1. **Install system dependencies**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-venv nginx
   ```

2. **Set up the application**
   ```bash
   cd /var/www/
   sudo git clone https://github.com/yourusername/crime-rate-prediction.git
   cd crime-rate-prediction
   sudo python3 -m venv venv
   sudo venv/bin/pip install -r requirements.txt
   ```

3. **Create systemd service**
   ```bash
   sudo nano /etc/systemd/system/crime-prediction.service
   ```

   Add the following content:
   ```ini
   [Unit]
   Description=Crime Rate Prediction API
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/var/www/crime-rate-prediction
   Environment="PATH=/var/www/crime-rate-prediction/venv/bin"
   ExecStart=/var/www/crime-rate-prediction/venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

4. **Start the service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable crime-prediction
   sudo systemctl start crime-prediction
   ```

5. **Configure Nginx (optional)**
   ```bash
   sudo nano /etc/nginx/sites-available/crime-prediction
   ```

   Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   Enable the site:
   ```bash
   sudo ln -s /etc/nginx/sites-available/crime-prediction /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

## ☁️ Cloud Deployment

### Heroku

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Ubuntu/Debian
   sudo snap install heroku --classic
   ```

2. **Create Procfile**
   ```bash
   echo "web: uvicorn app:app --host=0.0.0.0 --port=\$PORT" > Procfile
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### AWS EC2

1. **Launch EC2 instance**
2. **Connect via SSH**
3. **Follow the production server setup above**

### Google Cloud Platform

1. **Enable Cloud Run API**
2. **Deploy using Cloud Run**
   ```bash
   gcloud run deploy crime-prediction-api \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

## 🔧 Environment Variables

Create a `.env` file for configuration:

```bash
# API Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=false

# Model Configuration
MODEL_PATH=./models
```

## 📊 Monitoring and Logging

### Health Checks

The API includes a health check endpoint at `/` that returns a 200 status when healthy.

### Logging

Enable logging by setting the log level:

```bash
uvicorn app:app --log-level info
```

### Performance Monitoring

Consider adding monitoring tools:
- Prometheus + Grafana
- New Relic
- Datadog

## 🚨 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   sudo lsof -i :8000
   sudo kill -9 <PID>
   ```

2. **Model files not found**
   - Ensure all `.pkl` files are in the `models/` directory
   - Check file permissions

3. **Dependencies issues**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

### Debug Mode

For debugging, run with:
```bash
uvicorn app:app --reload --log-level debug
```

## 📚 Additional Resources

- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Systemd Service Management](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
