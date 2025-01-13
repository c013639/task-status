
from flask import Flask, request, jsonify
import logging
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from marshmallow import Schema, fields, ValidationError
from dotenv import load_dotenv
import os

load_dotenv()

class TaskStatus:
    def __init__(self):
        self.app = Flask(__name__)
        self.logger = self.setup_logging()
        # Define a Prometheus Gauge metric for task duration
        self.task_duration_gauge = Gauge('task_duration', 'Duration of tasks', ['tool', 'task', 'status'])
        self.app.add_url_rule('/api/tasks', 'task_status', self.task_status, methods=['POST'])
        self.app.add_url_rule('/metrics', 'metrics', self.metrics, methods=['GET'])

    def setup_logging(self):
        ## Configure logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger((__name__))
        return logger


    def task_status(self):
        request_data = request.json
        self.logger.info(f"Request Method: {request.method}")
        self.logger.info(f"Request URL: {request.url}")
        self.logger.info(f"Request Headers: {request.headers}")
        if request.method == "POST":
            self.logger.info(f"Request Data: {request_data}")

        # Validate request body against schema data types
        class BaseSchema(Schema):
          tool = fields.String(required=True)
          task = fields.String(required=True)
          status = fields.String(required=True)
          duration = fields.Integer(required=True)

        schema = BaseSchema()
        try:
            result = schema.load(request_data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        tool = request_data.get('tool')
        task = request_data.get('task')
        status = request_data.get('status')
        duration = request_data.get('duration')

        # validate status field possible values
        if status not in ['completed', 'failed', 'succeeded']:
            return jsonify({'error': 'Invalid status value'}), 400

        # Update the Prometheus Gauge metric
        self.task_duration_gauge.labels(tool=tool, task=task, status=status).set(duration)

        return jsonify({'message': 'Task received successfully'}), 200

    def metrics(self):
      self.logger.info(f"Sending the task_duration metrics to the prometheus")
      return generate_latest(self.task_duration_gauge), 200, {'Content-Type': CONTENT_TYPE_LATEST}

    def run(self):
        port = int(os.getenv('FLASK_PORT', 5000))
        self.app.run(host='0.0.0.0', port=5000)

task_status = TaskStatus()

if __name__ == '__main__':
    task_status.run()
