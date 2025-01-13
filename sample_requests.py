import requests
# Request fails validation
base_data = {
    "tool": "downgrade",
    "task": "healthchecks",
    "status": "error",
    "duration": 160
    }
r0 = requests.post('http://127.0.0.1:5000/api/tasks', json=base_data)
print(r0.content)

# Request passes validation 1
base_data = {
   "tool": "downgrade",
    "task": "healthchecks",
    "status": "completed",
    "duration": 170
    }
r1 = requests.post('http://127.0.0.1:5000/api/tasks', json=base_data)
print(r1.content)

# Request passes validation 2
base_data = {
   "tool": "upgrade",
    "task": "healthchecks",
    "status": "succeeded",
    "duration": 160
    }
r2 = requests.post('http://127.0.0.1:5000/api/tasks', json=base_data)
print(r2.content)

# Request passes validation 3
base_data = {
   "tool": "upgrade",
    "task": "healthchecks",
    "status": "failed",
    "duration": 150
    }
r3 = requests.post('http://127.0.0.1:5000/api/tasks', json=base_data)
print(r3.content)
