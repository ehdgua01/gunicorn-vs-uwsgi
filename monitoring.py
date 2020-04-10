import time
import psutil
from typing import Dict


class Monitoring(object):
    def __init__(self, pidfile: str) -> None:
        self.__stop = False

        with open(pidfile) as f:
            self.master_pid = f.read().strip()

    def measure_resource(self, interval: float) -> Dict[str, float]:
        """Averages of CPU && RAM Usages"""
        master_process = psutil.Process(int(self.master_pid))
        children = []

        cpu = 0
        mem = 0
        count = 0

        while not self.__stop:
            count += 1
            cpu += master_process.cpu_percent()
            mem += master_process.memory_info().rss
            children = master_process.children()

            for child in children:
                cpu += child.cpu_percent()
                mem += child.memory_info().rss

            time.sleep(interval)

        return {
            'cpu': (cpu / count) / (1 + len(children)),
            'mem': (mem / count) / (1 + len(children)) / (1024 * 1024),
        }

    def stop(self) -> None:
        self.__stop = True
