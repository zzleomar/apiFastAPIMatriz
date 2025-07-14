# Makefile para API Matriz
# Variables por defecto
CONTAINER_NAME = apimatriz

# Colores para output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
NC = \033[0m # No Color

.PHONY: help build up down logs restart status clean test health


build: ## Construir la imagen Docker
	@echo "$(GREEN)🔨 Construyendo imagen Docker...$(NC)"
	docker-compose -f docker-compose.yml --env-file ./docker/api.env build --no-cache
	@echo "$(GREEN)✅ Imagen construida exitosamente$(NC)"

up: ## Iniciar el contenedor
	@echo "$(GREEN)🚀 Iniciando API Matriz en puerto $(PORT)...$(NC)"
	docker-compose --env-file ./docker/api.env up -d 
	@echo "$(GREEN)✅ Contenedor iniciado: $(CONTAINER_NAME)$(NC)"
	@echo "$(YELLOW)🌐 API disponible en: http://localhost:$(PORT)$(NC)"
	@make health

down: ## Detener y eliminar el contenedor
	@echo "$(RED)🛑 Deteniendo contenedor...$(NC)"
	docker-compose --env-file ./docker/api.env down
	@echo "$(RED)✅ Contenedor detenido$(NC)"

logs: ## Ver logs del contenedor en tiempo real
	@echo "$(YELLOW)📋 Mostrando logs del contenedor $(CONTAINER_NAME)...$(NC)"
	@echo "$(YELLOW)Presiona Ctrl+C para salir$(NC)"
	docker-compose -f docker-compose.yml logs -f $(CONTAINER_NAME)

restart: ## Reiniciar el contenedor
	@echo "$(YELLOW)🔄 Reiniciando contenedor...$(NC)"
	@make down
	@make up

dev: ## Modo desarrollo (up + logs)
	@make up
	@make logs
