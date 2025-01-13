build:
	docker-compose -f docker-compose.yml build $(c)
up:
	docker-compose -f docker-compose.yml up -d $(c)
test:
	pytest --cov=task_status tests/
deploy:
	helm install task-status ./deployment/task_status

