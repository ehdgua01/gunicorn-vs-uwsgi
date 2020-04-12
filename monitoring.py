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
        t1 = time.time()

        while not self.__stop:
            try:
                cpu += master_process.cpu_percent()
                mem += master_process.memory_info().rss
                children = master_process.children()

                for child in children:
                    cpu += child.cpu_percent()
                    mem += child.memory_info().rss
            except Exception:
                pass

            time.sleep(interval)

        t2 = time.time() - t1

        return {
            'cpu': (cpu / t2) / (1 + len(children)),
            'mem': (mem / t2) / (1 + len(children)) / (1024 * 1024),
        }

    def stop(self) -> None:
        self.__stop = True
