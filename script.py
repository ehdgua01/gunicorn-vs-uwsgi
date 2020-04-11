import sys
import time
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

from monitoring import Monitoring


async def request():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('http://127.0.0.1:80') as response:
                return await response.text()
        except Exception:
            return False


def request_by_count(count: int):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(asyncio.gather(*[
        request() for _ in range(count)
    ]))


if __name__ == '__main__':
    pidfile = sys.argv[1]
    request_count = int(sys.argv[2])
    monitoring = Monitoring(pidfile)

    with ThreadPoolExecutor() as executor:
        future = executor.submit(monitoring.measure_resource, .1)
        start_time = time.time()
        result = request_by_count(request_count)
        print(f"Latency: {time.time() - start_time}")
        print(f"Errors: {result.count(False)}")
        monitoring.stop()
        print(f"Report: {future.result()}")
