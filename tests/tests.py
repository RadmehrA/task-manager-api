{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pytest\
import json\
from app import app\
\
@pytest.fixture\
def client():\
    with app.test_client() as client:\
        yield client\
\
def test_get_empty_tasks(client):\
    response = client.get('/tasks')\
    assert response.status_code == 200\
    assert response.json == []\
\
def test_create_task(client):\
    task = \{'title': 'New Task', 'description': 'A new task description'\}\
    response = client.post('/tasks', data=json.dumps(task), content_type='application/json')\
    assert response.status_code == 201\
    assert response.json['title'] == 'New Task'\
\
def test_get_task(client):\
    # First, create a task\
    task = \{'title': 'Task 1', 'description': 'Task description'\}\
    client.post('/tasks', data=json.dumps(task), content_type='application/json')\
\
    # Now, retrieve it\
    response = client.get('/tasks/1')\
    assert response.status_code == 200\
    assert response.json['title'] == 'Task 1'\
\
def test_update_task(client):\
    # Create a task\
    task = \{'title': 'Task to Update', 'description': 'Description'\}\
    client.post('/tasks', data=json.dumps(task), content_type='application/json')\
\
    # Update the task\
    updated_task = \{'title': 'Updated Task'\}\
    response = client.put('/tasks/1', data=json.dumps(updated_task), content_type='application/json')\
    assert response.status_code == 200\
    assert response.json['title'] == 'Updated Task'\
\
def test_delete_task(client):\
    # Create a task\
    task = \{'title': 'Task to Delete', 'description': 'Description'\}\
    client.post('/tasks', data=json.dumps(task), content_type='application/json')\
\
    # Delete the task\
    response = client.delete('/tasks/1')\
    assert response.status_code == 200\
    assert response.json['result'] is True\
}