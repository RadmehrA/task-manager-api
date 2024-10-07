{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify, request, abort\
from tasks import TaskManager\
\
app = Flask(__name__)\
task_manager = TaskManager()\
\
@app.route('/tasks', methods=['GET'])\
def get_tasks():\
    return jsonify(task_manager.get_all_tasks()), 200\
\
@app.route('/tasks/<int:task_id>', methods=['GET'])\
def get_task(task_id):\
    task = task_manager.get_task(task_id)\
    if not task:\
        abort(404)\
    return jsonify(task), 200\
\
@app.route('/tasks', methods=['POST'])\
def create_task():\
    if not request.json or 'title' not in request.json:\
        abort(400)\
    new_task = \{\
        'title': request.json['title'],\
        'description': request.json.get('description', "")\
    \}\
    task_manager.create_task(new_task)\
    return jsonify(new_task), 201\
\
@app.route('/tasks/<int:task_id>', methods=['PUT'])\
def update_task(task_id):\
    if not request.json:\
        abort(400)\
    updated_task = task_manager.update_task(task_id, request.json)\
    if not updated_task:\
        abort(404)\
    return jsonify(updated_task), 200\
\
@app.route('/tasks/<int:task_id>', methods=['DELETE'])\
def delete_task(task_id):\
    result = task_manager.delete_task(task_id)\
    if not result:\
        abort(404)\
    return jsonify(\{'result': result\}), 200\
\
if __name__ == '__main__':\
    app.run(debug=True)\
}