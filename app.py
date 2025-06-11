from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from extract import extract_resume_data
import shutil

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def form():
    return """
    <html>
        <body>
            <h2>Upload Resume</h2>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open("uploaded_resume.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    data = extract_resume_data("uploaded_resume.pdf")
    return {"Extracted Data": data}
