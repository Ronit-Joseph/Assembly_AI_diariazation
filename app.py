from fastapi import FastAPI, UploadFile, File
from platforms.AssemblyAI import Assembly

app = FastAPI()
assembly = Assembly()

@app.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    api_token: str = "4d6452a640404001bbf16fcce4a83272",
    min_speakers: int = 2,
    max_speakers: int = 5,
    platform: str = "AssemblyAI"
):
    # Save the uploaded audio file to a local temporary location
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Transcribe the audio using AssemblyAI
    transcription = assembly.transcribe_and_diarize(
        audio_file=file_path,
        api_token=api_token
    )

    # Return the transcription as JSON response
    return transcription
