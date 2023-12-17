from typing import Any
import asyncio

class CustomWaitFor:
    def __init__(self):
      self._loop = asyncio.get_event_loop()
      self._active_futures: dict[str, asyncio.Future] = {}

    # def new(self, tag: str) -> asyncio.Future:
    #     future = asyncio.Future(loop=self._loop)
    #     self._active_futures[tag] = future
    #     return future

    async def wait_for(self, tag: str, timeout: int = None) -> Any:
        future = asyncio.Future(loop=self._loop)
        self._active_futures[tag] = future

        try:
            return await asyncio.wait_for(future, timeout=timeout)
        except asyncio.TimeoutError:
            return None
        finally:
            self._active_futures.pop(tag)

    def set_result(self, tag: str, value: Any) -> None:
        future = self._active_futures.get(tag)
        future.set_result(value)

    @property
    def loop(self):
        return self._loop
    
    @loop.setter
    def loop(self, EventLoop: asyncio.AbstractEventLoop):
        self._loop = EventLoop
