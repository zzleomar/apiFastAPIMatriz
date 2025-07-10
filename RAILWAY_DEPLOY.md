# Deploy en Railway

## Problema Solucionado

❌ **Error anterior:**
```
Error: Invalid value for '--port': '$PORT' is not a valid integer.
```

✅ **Solución aplicada:**
- Cambio en Dockerfile para expandir correctamente variables de entorno
- Uso de `sh -c` para permitir expansión de `$PORT`

## Configuración para Railway

### 1. Dockerfile optimizado
```dockerfile
# Usar sh -c para permitir expansión de variables de entorno
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

### 2. Variables de entorno
Railway automáticamente provee la variable `PORT`, pero si necesitas configurar algo específico:

```bash
# Variables de entorno en Railway (opcional)
ENVIRONMENT=production
```

### 3. Health Check
La API incluye endpoints para monitoreo:
- `GET /` - Health check básico
- `GET /health` - Health check específico para Railway

## Pasos para Deploy

### Opción 1: Desde GitHub
1. Conecta tu repositorio a Railway
2. Railway detectará automáticamente el Dockerfile
3. El deploy se ejecutará automáticamente

### Opción 2: Railway CLI
```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### Opción 3: Deploy directo
1. Subir código a Railway
2. Railway build automáticamente con el Dockerfile
3. La variable `PORT` se asigna automáticamente

## Verificar el Deploy

Una vez desplegado, puedes probar:

```bash
# Health check
curl https://tu-app.railway.app/

# Test de matrices
curl -X POST https://tu-app.railway.app/matriz \
  -H "Content-Type: application/json" \
  -d '{
    "matrix1": [[1,2,3],[4,5,6],[7,8,9]],
    "matrix2": [["a","c","b"],["b","a","c"],["c","b","a"]],
    "i": 1,
    "j": 2
  }'
```

## Estructura de archivos para Railway

```
apiMatriz/
├── Dockerfile                 # ✅ Configurado para Railway
├── railway.json              # ✅ Configuración Railway
├── requirements.txt           # ✅ Dependencias Python
├── main.py                    # ✅ App con puerto dinámico
├── matrix_processor.py        # ✅ Lógica de negocio
├── matrix_validator.py        # ✅ Validaciones
└── RAILWAY_DEPLOY.md         # ✅ Esta guía
```

## Logs de Debug

Si necesitas debuggear, revisa los logs en Railway:
- Los logs mostrarán: `Uvicorn running on http://0.0.0.0:PORT`
- Donde PORT será el puerto asignado por Railway

## Configuración CORS

La API está configurada para aceptar requests desde cualquier origen:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para producción, cambiar por tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Para producción, cambia `allow_origins=["*"]` por tu dominio específico.

## Notas importantes

1. **Puerto dinámico**: Railway asigna automáticamente un puerto a través de la variable `PORT`
2. **Health checks**: Railway usa `/health` para verificar que la app esté funcionando
3. **Build automático**: Railway detecta el Dockerfile y construye automáticamente
4. **SSL/HTTPS**: Railway provee HTTPS automáticamente
5. **Variables de entorno**: Railway maneja automáticamente `PORT`, otras variables se configuran en el dashboard

## Troubleshooting

### Error de puerto
Si aún ves errores de puerto, verifica que:
- El Dockerfile use `sh -c` para expansión de variables
- La app lea `PORT` de variables de entorno
- No hay puertos hardcodeados en el código

### Error de health check
Si Railway marca la app como unhealthy:
- Verifica que `/health` responda correctamente
- Aumenta el timeout en `railway.json`
- Revisa los logs para errores de startup