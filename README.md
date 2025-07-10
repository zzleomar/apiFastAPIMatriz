# API Matriz

API FastAPI para procesamiento de matrices con configuración dinámica de puerto.

## Características

- **Puerto dinámico**: Configurable via variables de entorno
- **Docker**: Contenedor optimizado para desarrollo y producción
- **CORS**: Configurado para permitir comunicación con frontend
- **Health Check**: Endpoint para verificar estado de la API

## Configuración

### Variables de Entorno

```bash
PORT=8002  # Puerto de la API (por defecto: 8002)
```

### Ejecución Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar con puerto por defecto
python main.py

# Ejecutar con puerto personalizado
PORT=8003 python main.py
```

### Ejecución con Docker

#### Build y Run Manual

```bash
# Build de la imagen
docker build -t apimatriz .

# Ejecutar con puerto por defecto (8002)
docker run -d -p 8002:8002 --name apimatriz apimatriz

# Ejecutar con puerto personalizado
docker run -d -p 8003:8003 -e PORT=8003 --name apimatriz apimatriz
```

#### Docker Compose

```bash
# Ejecutar con puerto por defecto
docker-compose up -d

# Ejecutar con puerto personalizado
PORT=8003 docker-compose up -d

# Detener servicios
docker-compose down
```

## Endpoints

### Health Check
```
GET /
```

### Procesar Matrices
```
POST /matriz
Content-Type: application/json

{
  "matrix1": [[1,2,3],[4,5,6],[7,8,9]],
  "matrix2": [["a","c","b"],["b","a","c"],["c","b","a"]],
  "i": 1,
  "j": 2
}
```

## Estructura del Proyecto

```
apiMatriz/
├── main.py                 # Aplicación principal
├── matrix_processor.py     # Lógica de procesamiento
├── matrix_validator.py     # Validación de matrices
├── requirements.txt        # Dependencias
├── Dockerfile             # Configuración Docker
├── docker-compose.yml     # Orquestación Docker
├── .env.example          # Variables de entorno ejemplo
└── README.md             # Documentación
```

## Cambios Realizados

### Dockerfile
- **Corregido**: Comando `RUN` cambiado a `CMD` para ejecución correcta
- **Añadido**: Configuración dinámica de puerto via `ENV PORT=8002`
- **Añadido**: `EXPOSE $PORT` para documentar el puerto
- **Mejorado**: Estructura para aprovechar cache de Docker

### main.py
- **Añadido**: Middleware CORS para comunicación con frontend
- **Corregido**: Puerto por defecto cambiado de 8000 a 8002

### docker-compose.yml
- **Creado**: Configuración completa con variables de entorno
- **Añadido**: Health check para monitoreo
- **Añadido**: Restart policy para alta disponibilidad

## Pruebas

✅ **Build de Docker exitoso**
✅ **Ejecución con puerto por defecto (8002)**
✅ **Ejecución con puerto personalizado (8003, 8004, 8005)**
✅ **Health check funcional**
✅ **Endpoint de matrices funcional**
✅ **Docker Compose funcional**

## Uso con Makefile (Recomendado)

### Comandos principales:
```bash
# Ver todos los comandos disponibles
make help

# Iniciar en puerto por defecto (8002)
make up

# Iniciar en puerto personalizado
make up HOST_PORT=8003

# Ver logs en tiempo real
make logs

# Modo desarrollo (up + logs)
make dev

# Probar la API
make test

# Ver estado del contenedor
make status

# Reiniciar contenedor
make restart

# Detener contenedor
make down
```

### Comandos con puertos específicos:
```bash
make dev-8003    # Desarrollo en puerto 8003
make dev-8004    # Desarrollo en puerto 8004
make dev-8005    # Desarrollo en puerto 8005
```

### Múltiples instancias:
```bash
make multi-up      # Inicia en puertos 8002, 8003, 8004
make multi-status  # Ve estado de múltiples instancias
make multi-down    # Detiene múltiples instancias
```

## Uso Tradicional

### Docker Compose:
```bash
# Puerto por defecto
docker-compose up -d

# Puerto personalizado
PORT=8003 docker-compose up -d
```

### Variables de entorno:
```bash
# Archivo .env
PORT=8003
```

## Cambios en la Unificación de Puertos

### Variables unificadas:
- ✅ **Una sola variable `PORT`** para todo
- ✅ **Puerto host = Puerto contenedor = Puerto aplicación**
- ✅ **Consistencia total** en configuración

### Antes (múltiples variables):
```bash
HOST_PORT=8003 CONTAINER_PORT=8003 docker-compose up -d
```

### Ahora (una sola variable):
```bash
PORT=8003 docker-compose up -d
make up PORT=8003
PORT=8003 python main.py
```

### comando para activar el entorno virtual
source venv/bin/activate 