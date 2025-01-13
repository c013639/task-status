build:
	docker-compose -f docker-compose.yml build $(c)
up:
	docker-compose -f docker-compose.yml up -d $(c)
pytest:
	mkdir test/
	pytest --cov=task_status tests/
sample-requests:
	python3 sample_requests.py
deploy:
	helm install task-status ./deployment/task_status

