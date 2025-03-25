
# 🚀 GitHub Actions con Python y Runner Autohospedado

Este repositorio muestra un ejemplo de cómo configurar un flujo de trabajo de GitHub Actions para desplegar una aplicación Python usando Docker y Kubernetes, junto con un **runner autohospedado**.

----------

## 📁 Estructura del Proyecto

```
my-python-api/
├── app/
│   └── main.py # Código principal de la aplicación Python 
├── requirements.txt # Dependencias del proyecto 
├── Dockerfile # Imagen Docker de la aplicación 
├── k8s/
│   ├── deployment.yaml # Configuración de despliegue en Kubernetes 
│   └── service.yaml # Configuración del servicio en Kubernetes 
└── .github/
    └── workflows/
        └── deploy.yaml # Workflow de GitHub Actions
```

----------

## 🛠️ Configuración del Runner Autohospedado

Sigue los siguientes pasos para configurar un runner autohospedado en Linux:

### 1. Crear el directorio del runner

bash

CopiarEditar

```
mkdir -p ~/github-runners/python-api-runner cd ~/github-runners/python-api-runner
```

### 2. Descargar el paquete del runner

```
curl -LO https://github.com/actions/runner/releases/download/v2.316.0/actions-runner-linux-x64-2.316.0.tar.gz
```

### 3. Extraer los archivos

```
tar xzf actions-runner-linux-x64-2.316.0.tar.gz
```

### 4. Configurar el runner

Reemplaza `<TOKEN>` con el token generado desde la UI de GitHub:

```
./config.sh --url https://github.com/fredwinrosales/github-actions-python \
            --token <TOKEN> \
            --name python-runner \
            --labels self-hosted,python
```

### 5. Instalar el servicio del runner

```
sudo ./svc.sh install
```

### 6. Iniciar el servicio del runner

```
sudo ./svc.sh start
```

### 7. Verificar el estado del runner

```
sudo systemctl status actions.runner.fredwinrosales-github-actions-python.*
```

### 8. Listar unidades relacionadas al runner

```
systemctl list-units | grep actions.runner
```

----------

## ✅ Resultado Esperado

Una vez configurado correctamente, el runner autohospedado procesará los flujos de trabajo definidos en `.github/workflows/deploy.yaml`, desplegando tu aplicación en un clúster de Kubernetes según las configuraciones en el directorio `k8s/`.
