max by (tool) (task_duration)
# Task Status Flask Application

## Overview

Task Status is a Flask-based web application designed to receive task status from external systems. This application provides a simple interface for receiving the tasks exposed on "/api/tasks".
Prometheus client exposed on "/metrics" fetches the task_duration metrics from task status API endpoint.

## Features

- Receive new task with “tool,task,status,duration" where status field can be only of completed, failed, succeeded values.
- Duration field stores duration time in seconds.

## Sample Request

   ```curl -X POST http://127.0.0.1:5000/api/tasks -H "Content-Type: application/json" -d '{"tool": "downgrade",  "task": "healthchecks",  "status": "completed",  "duration": 170}
   ```

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- python3.11 or later, pip3
- docker
- make
- pytest

### Installation

- **Run inside container**

   ```
   #!/bin/bash
   git clone https://github.com/c013639/task-status.git
   cd task_status
   make build
   make up
   make pytest
   make test
   make deploy
   ```

  **make build**
   This will build the python task_status and prometheus docker build images

  **make up**
   This is to run the task_status application and prometheus image

   **make test**
   To test the application with sample json data.

  **make pytest**
   To test the application with certain use cases using pytest

  **make deploy**
   Deploy the application in the kubernetes cluster.

- **Run directly on local machine**
   ```
   python3 custom_prom.py
   python3 sample_requests.py

   ```