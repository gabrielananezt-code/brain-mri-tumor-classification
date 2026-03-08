# Despliegue en EC2 con Docker

Este proyecto se ejecuta con dos contenedores:

- API FastAPI (`:8000`)
- Dashboard Streamlit (`:8501`)

## 1. Prerrequisitos en EC2

Instala Docker y Docker Compose Plugin:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

## 2. Abrir puertos en Security Group

Configura reglas de entrada:

- `22` (SSH) desde tu IP
- `8000` (FastAPI) opcional, solo si deseas acceso público a la API
- `8501` (Dashboard) desde IPs autorizadas o temporalmente `0.0.0.0/0` para pruebas

## 3. Clonar y construir

```bash
git clone <URL_REPO>
cd brain-mri-tumor-classification
docker compose build
docker compose up -d
```

## 4. Verificar servicios

```bash
docker compose ps
docker compose logs -f api
docker compose logs -f dashboard
```

Pruebas:

- API health: `http://<EC2_PUBLIC_IP>:8000/health`
- Dashboard: `http://<EC2_PUBLIC_IP>:8501`

## 5. Operación básica

```bash
docker compose restart
docker compose down
docker compose up -d --build
```
