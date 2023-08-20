from platforms.ClarityAI import Clarity
from platforms.AssemblyAI import Assembly


def main(
    platform: str,
    audio_file: str,
    min_speakers: int,
    max_speakers: int,
    assemblyAI_API_Key: str = "",
):
    if platform == "ClarityAI":
        clarity = Clarity()
        res = clarity.transcribe_and_diarize(
            audio_file=audio_file, min_speakers=min_speakers, max_speakers=max_speakers
        )
        return res

    elif platform == "AssemblyAI":
        assembly = Assembly()
        res = assembly.transcribe_and_diarize(
            audio_file=audio_file, api_token=assemblyAI_API_Key
        )
        return res

    else:
        return "Platform not supported. Please chose between `AssemblyAI` and `Clarity`"


if __name__ == "__main__":
    r = main(
        platform="AssemblyAI",
        audio_file="data/audio_sample_1.mp3",
        min_speakers=2,
        max_speakers=5,
        assemblyAI_API_Key="4d6452a640404001bbf16fcce4a83272",
    )
    print(r)
