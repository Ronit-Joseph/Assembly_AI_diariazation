from platforms.AssemblyAI import Assembly




def get_number_of_speakers(audio_file):
    assembly = Assembly()
    api_token = "4d6452a640404001bbf16fcce4a83272"
    speaker_count = assembly.get_speaker_count(audio_file, api_token)
    return speaker_count

def test_speakers():
    assert get_number_of_speakers("test_data/FGD_1.mp3") == 5
    assert get_number_of_speakers("test_data/FGD_2_(South Asian accent).mp3") == 5
    assert get_number_of_speakers("test_data/FGD_3.mp3") == 8
    assert get_number_of_speakers("test_data/FGD_4.mp3") == 6
    
    assert get_number_of_speakers("test_data/Focus_Group_Discussion_Part_1.m4a") == 5
    assert get_number_of_speakers("test_data/Focus_Group_Discussion_Part_2.m4a") == 5
    assert get_number_of_speakers("test_data/Semi_Structured_Interview_Part_2.m4a") == 2
    assert get_number_of_speakers("test_data/8-3-07Anon.mp3") == 2
    assert get_number_of_speakers("test_data/8-3-17Anon.mp3") == 2
    assert get_number_of_speakers("test_data/Brown_Interview.m4a") == 2
#print(get_number_of_speakers("test_data/FGD_1.mp3"))