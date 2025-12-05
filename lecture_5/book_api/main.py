from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root_read():
    html_content = "<h1>Hi world</h1>"
    return HTMLResponse(content=html_content)