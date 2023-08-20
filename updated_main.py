from platforms.AssemblyAI import Assembly
from decouple import config


def main(audio_file: str):
    assembly = Assembly()
    assemblyAI_API_Key = config('ASSEMBLYAI_API_KEY')
    res = assembly.transcribe_and_diarize(audio_file=audio_file, api_token=assemblyAI_API_Key)
    return res


if __name__ == "__main__":
    r = main(
        audio_file="data/audio_sample_1.mp3",
    )
    print(r)
