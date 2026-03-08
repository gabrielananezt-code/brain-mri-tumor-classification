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

## 6. Despliegue con ECR (opcional recomendado)

Si quieres separar build y runtime, publica imagenes en ECR y en EC2 usa `image:` en lugar de `build:`.

Flujo:

1. Crear repositorios ECR (`api` y `dashboard`)
2. `docker build -f Dockerfile.api -t <ECR_API_URI>:v1 .`
3. `docker build -f Dockerfile.dashboard -t <ECR_DASH_URI>:v1 .`
4. `docker push ...`
5. En EC2: `docker login` a ECR y `docker compose pull && docker compose up -d`

## 7. Recomendaciones de produccion

- Volumen EBS minimo `20 GB` (mejor `30 GB`) para builds con ML.
- Colocar Nginx/ALB delante del dashboard.
- Restringir acceso de red al puerto 8501.
- Anadir HTTPS (ACM + ALB o Nginx + certbot).
- Fijar versiones en `requirements-api.txt` y `requirements-dashboard.txt`.

## 8. Troubleshooting: no space left on device

Si falla el build con `no space left on device`:

```bash
df -h
docker system df
docker compose down --remove-orphans
docker builder prune -af
docker system prune -af --volumes
```

Luego reconstruye sin cache:

```bash
docker compose build --no-cache api
docker compose up -d
```
