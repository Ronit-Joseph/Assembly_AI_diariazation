import requests
import time
from clarity.utils.formatter import JSONFormatter
import json

class Assembly:
    def __init__(self) -> None:
        pass

    def read_file(self, filename, chunk_size=5242880):
    # Open the file in binary mode for reading
        with open(filename, 'rb') as _file:
            while True:
                # Read a chunk of data from the file
                data = _file.read(chunk_size)
                # If there's no more data, stop reading
                if not data:
                    break
                # Yield the data as a generator
                yield data

    def upload_file(self, api_token, path):
        """
        Upload a file to the AssemblyAI API.

        Args:
            api_token (str): Your API token for AssemblyAI.
            path (str): Path to the local file.

        Returns:
            str: The upload URL.
        """
        print(f"Uploading file: {path}")

        # Set the headers for the request, including the API token
        headers = {'authorization': api_token}
        
        # Send a POST request to the API to upload the file, passing in the headers
        # and the file data
        response = requests.post('https://api.assemblyai.com/v2/upload',
                                headers=headers,
                                data=self.read_file(path))

        # If the response is successful, return the upload URL
        if response.status_code == 200:
            return response.json()["upload_url"]
        # If the response is not successful, print the error message and return
        # None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    
    def create_transcript(self, api_token, audio_url):
        """
        Create a transcript using AssemblyAI API.

        Args:
            api_token (str): Your API token for AssemblyAI.
            audio_url (str): URL of the audio file to be transcribed.

        Returns:
            dict: Completed transcript object.
        """
        print("Transcribing audio... This might take a moment.")

        # Set the API endpoint for creating a new transcript
        url = "https://api.assemblyai.com/v2/transcript"

        # Set the headers for the request, including the API token and content type
        headers = {
            "authorization": api_token,
            "content-type": "application/json"
        }

        # Set the data for the request, including the URL of the audio file to be
        # transcribed
        data = {
            "audio_url": audio_url,
            "speaker_labels": True,
        }

        # Send a POST request to the API to create a new transcript, passing in the
        # headers and data
        response = requests.post(url, json=data, headers=headers)

        # Get the transcript ID from the response JSON data
        transcript_id = response.json()['id']

        # Set the polling endpoint URL by appending the transcript ID to the API endpoint
        polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

        # Keep polling the API until the transcription is complete
        while True:
            # Send a GET request to the polling endpoint, passing in the headers
            transcription_result = requests.get(polling_endpoint, headers=headers).json()

            # If the status of the transcription is 'completed', exit the loop
            if transcription_result['status'] == 'completed':
                break

            # If the status of the transcription is 'error', raise a runtime error with
            # the error message
            elif transcription_result['status'] == 'error':
                raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

            # If the status of the transcription is not 'completed' or 'error', wait for
            # 3 seconds and poll again
            else:
                time.sleep(3)

        return transcription_result
    
    
    def get_utterances_respnse(self, api_token, audio_url):
        """
        Create a transcript using AssemblyAI API.

        Args:
            api_token (str): Your API token for AssemblyAI.
            audio_url (str): URL of the audio file to be transcribed.

        Returns:
            dict: Completed transcript object.
        """
        print("Transcribing audio... This might take a moment.")

        # Set the API endpoint for creating a new transcript
        url = "https://api.assemblyai.com/v2/transcript"

        # Set the headers for the request, including the API token and content type
        headers = {
            "authorization": api_token,
            "content-type": "application/json"
        }

        # Set the data for the request, including the URL of the audio file to be
        # transcribed
        data = {
            "audio_url": audio_url,
            "speaker_labels": True,
        }

        # Send a POST request to the API to create a new transcript, passing in the
        # headers and data
        response = requests.post(url, json=data, headers=headers)
        utterances = response.json()['utterances']
        return utterances    
        
    
    def transcribe_and_diarize(self, audio_file, api_token):
        upload_url = self.upload_file(api_token, audio_file)
        transcript = self.create_transcript(api_token, upload_url)
        formatter = JSONFormatter()
        return formatter.format_outputs(transcript)     
    
    
    

    def get_utterance(self, audio_file, api_token):
        upload_url = self.upload_file(api_token, audio_file)
        transcript = self.create_transcript(api_token, upload_url)
        utterances = transcript['utterances']
        return utterances
    
    def get_speaker_count(self, audio_file, api_token):
        upload_url = self.upload_file(api_token, audio_file)
        transcript = self.create_transcript(api_token, upload_url)
        utterances = transcript['utterances']
        speaker_count = len(set(utterance['speaker'] for utterance in utterances))
        return speaker_count

        
        