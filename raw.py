from typing import Any
import asyncio

# WIP
class CustomWaitFor:
    def __init__(self):
      self._loop = asyncio.get_event_loop()
      self._active_futures: dict[str, asyncio.Future] = {}

    def new(self, tag: str) -> asyncio.Future:
        f = asyncio.Future(loop=self._loop)
        self._active_futures[tag] = f
        return f

    async def wait_for(self, tag: str,timeout: int = None) -> Any:
        future = self._active_futures.get(tag)

        try:
            return await asyncio.wait_for(future, timeout=timeout)
        except asyncio.TimeoutError:
            return None
        finally:
            self._active_futures.pop(tag)

    def set_result(self, tag: str, value: Any) -> None:
        f = self._active_futures.get(tag)
        f.set_result(value)

    @property
    def loop(self):
        return self._loop
    
    @loop.setter
    def loop(self, EventLoop: asyncio.AbstractEventLoop):
        self._loop = EventLoop
