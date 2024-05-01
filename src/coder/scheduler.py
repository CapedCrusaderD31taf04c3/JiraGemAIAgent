# -*- coding: utf-8 -*-
# Copyright 2024 JiraGemAIAgent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from logger.custom_logger import Logger

import queue
import threading
import time


class SubprocessWorkScheduler:
    """
    A class that creates subpross and schedule them
    """
    def __init__(self):
        """
        constructor
        """
        self.work_queue = queue.Queue()
        self.is_running = False
        self.lock = threading.Lock()

    def add_task(self, func, *args, **kwargs):
        """
        Adding Task to the queue
        """
        self.work_queue.put((func, args, kwargs))
        if not self.is_running:
            self.start()

    def start(self):
        """
        Starting the execution of thread
        """
        self.is_running = True
        threading.Thread(target=self._execute_tasks).start()

    def _execute_tasks(self):
        """
        Executing the Task
        """
        while not self.work_queue.empty():
            with self.lock:
                task = self.work_queue.get()
                func, args, kwargs = task
                try:
                    func(*args, **kwargs)
                    time.sleep(5)
                except Exception as err:
                    Logger.error(message=f"Error Occurred - {str(err)}")
            self.work_queue.task_done()
        self.is_running = False

class Scheduler:
    """
    A class for creating single instance of SubprocessWorkScheduler safely
    """
    runner = SubprocessWorkScheduler()
