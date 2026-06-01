from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def event_generator():
    while True:
        await asyncio.sleep(2)
        yield "data: {\"message\": \"New notification from Nova\"}\n\n"

@app.get("/events")
def get_events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
