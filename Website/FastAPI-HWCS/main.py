from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from pathlib import Path
from utils import predict_handwriting

app = FastAPI(title="HWCS - Handwriting Classification System")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Ensure uploads directory exists
os.makedirs("uploads", exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page"""
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/predict")
async def predict(request: Request, image: UploadFile = File(...)):
    """Handle image upload and prediction"""
    try:
        # Save uploaded file
        file_path = f"uploads/{image.filename}"
        with open(file_path, "wb") as buffer:
            content = await image.read()
            buffer.write(content)

        # Make prediction
        predicted_writer = predict_handwriting(file_path)

        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)

        # Map prediction to result message
        result_messages = {
            'hasnain': "The uploaded image is written by Hasnain",
            'mehdy': "The uploaded image is written by Mehdy",
            'umair': "The uploaded image is written by Umair"
        }

        prediction_result = result_messages.get(
            predicted_writer.lower(),
            "The uploaded image is written by Unknown"
        )

        return templates.TemplateResponse(
            "result.html",
            {"request": request, "prediction_result": prediction_result}
        )

    except Exception as e:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "prediction_result": f"Error processing image: {str(e)}"
            }
        )


@app.post("/predict-demo")
async def predict_demo(request: Request, demo_image: str = Form(...)):
    """Handle demo image prediction"""
    try:
        # Construct path to demo image
        demo_path = f"static/demo_images/{demo_image}"

        if not os.path.exists(demo_path):
            return templates.TemplateResponse(
                "result.html",
                {
                    "request": request,
                    "prediction_result": "Demo image not found"
                }
            )

        # Make prediction
        predicted_writer = predict_handwriting(demo_path)

        # Map prediction to result message
        result_messages = {
            'hasnain': "The uploaded image is written by Hasnain",
            'mehdy': "The uploaded image is written by Mehdy",
            'umair': "The uploaded image is written by Umair"
        }

        prediction_result = result_messages.get(
            predicted_writer.lower(),
            "The uploaded image is written by Unknown"
        )

        return templates.TemplateResponse(
            "result.html",
            {"request": request, "prediction_result": prediction_result}
        )

    except Exception as e:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "prediction_result": f"Error processing demo image: {str(e)}"
            }
        )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "HWCS API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
