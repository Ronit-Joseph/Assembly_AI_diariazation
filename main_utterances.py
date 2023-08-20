from platforms.ClarityAI import Clarity
from platforms.AssemblyAI import Assembly


def main(
    platform: str,
    audio_file: str,
    min_speakers: int,
    max_speakers: int,
    assemblyAI_API_Key: str = "",
):
    

    if platform == "AssemblyAI":
        assembly = Assembly()
        res = assembly.get_utterance(
            audio_file=audio_file, api_token=assemblyAI_API_Key
        )
        return res

    else:
        return "Platform not supported. "


if __name__ == "__main__":
    utterances = main(
        platform="AssemblyAI",
        audio_file="data/audio_sample_1.mp3",
        min_speakers=2,
        max_speakers=10,
        assemblyAI_API_Key="4d6452a640404001bbf16fcce4a83272",
    )
    #print(utterances)
    for i in range(len(utterances)-1):
        current_speaker = utterances[i]['speaker']
        next_speaker = utterances[i+1]['speaker']
        
        start = utterances[i]['start'] /1000.0
        end = utterances[i+1]['end'] /1000.0
        
        print(f"Speaker start: {current_speaker} end: {next_speaker}")
        print(f"Start timestamp: {start}, End timestamp: {end}\n")
    
    
