{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class TaskManager:\
    def __init__(self):\
        self.tasks = []\
        self.next_id = 1\
\
    def get_all_tasks(self):\
        return self.tasks\
\
    def get_task(self, task_id):\
        return next((task for task in self.tasks if task['id'] == task_id), None)\
\
    def create_task(self, task_data):\
        task_data['id'] = self.next_id\
        self.next_id += 1\
        self.tasks.append(task_data)\
\
    def update_task(self, task_id, updated_data):\
        task = self.get_task(task_id)\
        if not task:\
            return None\
        task.update(updated_data)\
        return task\
\
    def delete_task(self, task_id):\
        task = self.get_task(task_id)\
        if task:\
            self.tasks.remove(task)\
            return True\
        return False\
}