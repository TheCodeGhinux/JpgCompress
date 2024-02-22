from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from compress import compress_image

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/compress/")
async def compress(request: Request, input_file: UploadFile = File(...), n_clusters: int = 8):
    contents = await input_file.read()
    compressed_image, _ = compress_image(contents, n_clusters=n_clusters)
    with open("static/compressed_image.jpg", "wb") as f:
        f.write(compressed_image)
    return templates.TemplateResponse("index.html", {"request": request, "result": "Compressed_image.jpg"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
