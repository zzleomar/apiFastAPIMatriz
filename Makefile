# Makefile para API Matriz
# Variables por defecto
PORT ?= 8000
CONTAINER_NAME = apimatriz_$(PORT)

# Colores para output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
NC = \033[0m # No Color

.PHONY: help build up down logs restart status clean test health

# Comando por defecto
help: ## Mostrar ayuda
	@echo "$(YELLOW)API Matriz - Comandos disponibles:$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Ejemplos de uso:$(NC)"
	@echo "  make up                    # Iniciar en puerto 8000"
	@echo "  make up PORT=8003          # Iniciar en puerto 8003"
	@echo "  make logs                  # Ver logs en tiempo real"
	@echo "  make restart PORT=8004     # Reiniciar en puerto 8004"

build: ## Construir la imagen Docker
	@echo "$(GREEN)🔨 Construyendo imagen Docker...$(NC)"
	@docker build -t apimatriz .
	@echo "$(GREEN)✅ Imagen construida exitosamente$(NC)"

up: ## Iniciar el contenedor
	@echo "$(GREEN)🚀 Iniciando API Matriz en puerto $(PORT)...$(NC)"
	@PORT=$(PORT) docker-compose up -d
	@echo "$(GREEN)✅ Contenedor iniciado: $(CONTAINER_NAME)$(NC)"
	@echo "$(YELLOW)🌐 API disponible en: http://localhost:$(PORT)$(NC)"
	@make health

down: ## Detener y eliminar el contenedor
	@echo "$(RED)🛑 Deteniendo contenedor...$(NC)"
	@PORT=$(PORT) docker-compose down
	@echo "$(RED)✅ Contenedor detenido$(NC)"

logs: ## Ver logs del contenedor en tiempo real
	@echo "$(YELLOW)📋 Mostrando logs del contenedor $(CONTAINER_NAME)...$(NC)"
	@echo "$(YELLOW)Presiona Ctrl+C para salir$(NC)"
	@docker logs -f $(CONTAINER_NAME) 2>/dev/null || echo "$(RED)❌ Contenedor no encontrado. Usa 'make up' primero$(NC)"

restart: ## Reiniciar el contenedor
	@echo "$(YELLOW)🔄 Reiniciando contenedor...$(NC)"
	@make down
	@make up PORT=$(PORT)

status: ## Mostrar estado del contenedor
	@echo "$(YELLOW)📊 Estado del contenedor:$(NC)"
	@docker ps --filter "name=$(CONTAINER_NAME)" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" || echo "$(RED)❌ Contenedor no encontrado$(NC)"

clean: ## Eliminar contenedor e imagen
	@echo "$(RED)🧹 Limpiando contenedores e imágenes...$(NC)"
	@docker stop $(CONTAINER_NAME) 2>/dev/null || true
	@docker rm $(CONTAINER_NAME) 2>/dev/null || true
	@docker rmi apimatriz 2>/dev/null || true
	@echo "$(RED)✅ Limpieza completada$(NC)"

test: ## Probar la API
	@echo "$(YELLOW)🧪 Probando API...$(NC)"
	@echo "$(YELLOW)Health Check:$(NC)"
	@curl -s http://localhost:$(PORT)/ | jq . 2>/dev/null || curl -s http://localhost:$(PORT)/ || echo "$(RED)❌ API no responde$(NC)"
	@echo ""
	@echo "$(YELLOW)Test de procesamiento de matrices:$(NC)"
	@curl -s -X POST http://localhost:$(PORT)/matriz \
		-H "Content-Type: application/json" \
		-d '{"matrix1": [[1,2,3],[4,5,6],[7,8,9]], "matrix2": [["a","c","b"],["b","a","c"],["c","b","a"]], "i": 1, "j": 2}' \
		| jq '.message.message' 2>/dev/null || echo "$(RED)❌ Test falló$(NC)"

health: ## Verificar estado de salud de la API
	@echo "$(YELLOW)🏥 Verificando estado de salud...$(NC)"
	@sleep 2
	@curl -s http://localhost:$(PORT)/ >/dev/null 2>&1 && echo "$(GREEN)✅ API funcionando correctamente$(NC)" || echo "$(RED)❌ API no responde$(NC)"

dev: ## Modo desarrollo (up + logs)
	@make up PORT=$(PORT)
	@make logs

# Comandos con puertos específicos
dev-8003: ## Iniciar en puerto 8003 y mostrar logs
	@make dev PORT=8003

dev-8004: ## Iniciar en puerto 8004 y mostrar logs
	@make dev PORT=8004

dev-8005: ## Iniciar en puerto 8005 y mostrar logs
	@make dev PORT=8005

# Comandos de múltiples puertos
multi-up: ## Iniciar múltiples instancias (8000, 8001, 8002)
	@make up PORT=8000
	@make up PORT=8001
	@make up PORT=8002
	@echo "$(GREEN)✅ Múltiples instancias iniciadas$(NC)"

multi-down: ## Detener múltiples instancias
	@make down PORT=8000
	@make down PORT=8001
	@make down PORT=8002
	@echo "$(RED)✅ Múltiples instancias detenidas$(NC)"

multi-status: ## Ver estado de múltiples instancias
	@echo "$(YELLOW)📊 Estado de múltiples instancias:$(NC)"
	@docker ps --filter "name=apimatriz_" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" || echo "$(RED)❌ No hay instancias ejecutándose$(NC)"