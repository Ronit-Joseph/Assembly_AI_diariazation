from platforms.AssemblyAI import Assembly
from decouple import config


def assembly_api_call(audio_file):
    assembly = Assembly()
    assemblyAI_API_Key = config('ASSEMBLYAI_API_KEY')
    res = assembly.transcribe_and_diarize(audio_file=audio_file, api_token=assemblyAI_API_Key)
    return res

#print(assembly_api_call("data/audio_sample_1.mp3"))
#uncomment above line if you want this file to print the json formatted output

