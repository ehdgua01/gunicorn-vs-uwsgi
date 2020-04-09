import time
import psutil
from typing import Dict


class Monitoring(object):
    def __init__(self, pidfile: str) -> None:
        self.__stop = False

        with open(pidfile) as f:
            self.master_pid = f.read().strip()

    def measure_resource(self, interval: float) -> Dict[str, float]:
        """CPU && RAM Usages"""
        master_process = psutil.Process(int(self.master_pid))
        children = master_process.children()
        cpu = 0
        mem = 0

        while not self.__stop:
            cpu += master_process.cpu_percent()
            mem += master_process.memory_percent()

            for p in children:
                cpu += p.cpu_percent()
                mem += p.memory_percent()

            time.sleep(interval)

        return {
            'cpu': cpu,
            'mem': mem,
        }

    def stop(self) -> None:
        self.__stop = True
