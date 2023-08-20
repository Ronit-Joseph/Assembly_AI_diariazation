import gspread
from oauth2client.service_account import ServiceAccountCredentials
from platforms.AssemblyAI import Assembly



# Set up the credentials
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "/home/ronit/Documents/Whisper_diarization_gitlab/gsheet_credentials/graphene-dev-3a0d886afd92.json", scope)

# Authenticate with the Google Sheets API
client = gspread.authorize(credentials)

#create the spreadsheet
#new_spreadsheet = client.create("validation_for_clarity")

# Open the Google Sheets document
spreadsheet = client.open("validation_for_clarity")



# # Create the worksheet if it doesn't exist
#worksheet = spreadsheet.add_worksheet(title="audio_samples_and_speaker_info_sheet", rows="1000", cols="8")

# # Select the desired worksheet
worksheet = spreadsheet.worksheet("audio_samples_and_speaker_info_sheet")

# assembly = Assembly()
# utterances = assembly.get_utterance(
# audio_file="data/audio_sample_1.mp3", api_token="4d6452a640404001bbf16fcce4a83272")

# for i in range(len(utterances)-1):
#     current_speaker = utterances[i]['speaker']
#     next_speaker = utterances[i+1]['speaker']
    
#     start = utterances[i]['start'] /1000.0
#     end = utterances[i+1]['end'] /1000.0
    
#     print(f"Speaker start: {current_speaker} end: {next_speaker}")
#     print(f"Start timestamp: {start}, End timestamp: {end}\n")
    
#     row = [f"Speaker start: {current_speaker} end: {next_speaker}",f"Start timestamp: {start}", f"End timestamp: {end}"]
#     worksheet.append_row(row)
# print("Data added to the Google Sheet.")




values = worksheet.get_all_values()

# Print the values
for row in values:
    print(row)


































# # Get the list of worksheets
# worksheet_list = spreadsheet.worksheets()

# # Iterate over the worksheets and print their titles
# for a in worksheet_list:
#     print(a.title)

# # Print information about the worksheet
# print("Worksheet Title:", worksheet.title)
# print("Row Count:", worksheet.row_count)
# print("Column Count:", worksheet.col_count)






# row = [f"Speaker start: {current_speaker} end: {next_speaker}",
#            f"Start timestamp: {start}", f"End timestamp: {end}""]
#     sheet.append_row(row)
# print("Data added to the Google Sheet.")