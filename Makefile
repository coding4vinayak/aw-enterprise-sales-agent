# Enterprise Sales Agent Makefile

.PHONY: help install backend-install frontend-install dev backend-dev frontend-dev test backend-test frontend-test docker-up docker-down clean-db format lint security-check

# Default target
help:
	@echo "Enterprise Sales Agent - Development Commands"
	@echo ""
	@echo "Usage:"
	@echo "  make install            Install all dependencies"
	@echo "  make dev                Start development environment"
	@echo "  make test               Run all tests"
	@echo "  make docker-up          Start Docker services"
	@echo "  make docker-down        Stop Docker services"
	@echo "  make clean-db           Clean database volumes"
	@echo "  make format             Format code"
	@echo "  make lint               Lint code"
	@echo "  make security-check     Run security checks"

# Install dependencies
install: backend-install frontend-install

backend-install:
	@echo "Installing backend dependencies..."
	cd backend && pip install -r requirements.txt

frontend-install:
	@echo "Installing frontend dependencies..."
	cd frontend && npm install

# Development commands
dev: docker-up backend-dev frontend-dev

backend-dev:
	@echo "Starting backend development server..."
	cd backend && python -m uvicorn app.main:app --reload --port 8000

frontend-dev:
	@echo "Starting frontend development server..."
	cd frontend && npm run dev

# Test commands
test: backend-test frontend-test

backend-test:
	@echo "Running backend tests..."
	cd backend && pytest tests/

frontend-test:
	@echo "Running frontend tests..."
	cd frontend && npm run test

# Docker commands
docker-up:
	@echo "Starting Docker services..."
	cd infra/docker && docker-compose up -d

docker-down:
	@echo "Stopping Docker services..."
	cd infra/docker && docker-compose down

clean-db:
	@echo "Cleaning database volumes..."
	cd infra/docker && docker-compose down -v
	docker volume prune -f

# Code quality
format:
	@echo "Formatting code..."
	cd backend && ruff format . && ruff check . --fix
	cd frontend && npm run format

lint:
	@echo "Linting code..."
	cd backend && ruff check .
	cd frontend && npm run lint

security-check:
	@echo "Running security checks..."
	cd backend && bandit -r . && safety check -r requirements.txt