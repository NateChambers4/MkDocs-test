import pandas as pd
import re

def extract_refinery_equipment_path_event_type(subject, body):
    refinery, equipment, path, event_type, date, time = None, None, None, None, None, None

    # Refinery extraction logic
    if 'usig' in body:
        refinery = 'Benicia'
        equipment = 'CEMS'
        path = 'usig'
    elif 'mrcsite' in body.lower() or 'mrc' in subject.lower():
        refinery = 'MRC'
    elif '[Shell]' in subject or 'Shell' in subject:
        refinery = 'Shell'
    elif 'Porter Ranch' in subject:
        refinery = 'Porter Ranch'
    elif 'Bazan' in subject:
        refinery = 'Bazan'

    # Equipment extraction logic
    if not equipment:
        equipment_match = re.search(r'(TDL|UV|MET)', subject + ' ' + body)
        if equipment_match:
            equipment = equipment_match.group(1)

    # Path extraction logic
    path_match = re.search(r'sig(\d+)|Path #?(\d+)|Site ([A-Z])|UV_(\d+)|MET_(\d+)', subject + ' ' + body)
    if path_match:
        if path_match.group(1):
            path = 'Sig ' + path_match.group(1)
        elif path_match.group(2):
            path = 'Path ' + path_match.group(2)
        elif path_match.group(3):
            path = 'Site ' + path_match.group(3)
        elif path_match.group(4):
            path = 'Path ' + path_match.group(4)  # For UV_x pattern
        elif path_match.group(5):
            path = 'Path ' + path_match.group(5)  # For MET_x pattern
        else:
            path = None  # or some default value

    # Event type extraction logic
    if 'missing data' in body.lower():
        event_type = 'Missing Data'
    elif 'usig out' in body.lower():
        event_type = 'Low Signal Ended'
    elif 'usig up' in body.lower():
        event_type = 'System Up'
    elif 'usig no data' in body.lower():
        event_type = 'No Data'
    elif 'low signal' in body.lower():
        event_type = 'Low Signal' if 'ended' not in body.lower() else 'Low Signal Ended'
    else:
        event_type_match = re.search(r'System (Down|Up)|Gas Alarm|Low Signal', subject)
        if event_type_match:
            event_type = event_type_match.group(0)

    date, time = extract_date_time_from_text(subject + ' ' + body)
    return refinery, equipment, path, event_type, date, time


# Date and time extraction logic
    date, time = extract_date_time_from_text(subject + ' ' + body)
    return refinery, equipment, path, event_type, date, time


def extract_date_time_from_text(text):
    # Original pattern
    date_time_match = re.search(r'\b(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2})', text)
    if date_time_match:
        return date_time_match.group(1), date_time_match.group(2)

    # Alternative pattern 1 (e.g., "2023-05-19 at 01:50")
    date_time_match_alt = re.search(r'(\d{4}-\d{2}-\d{2})\s+at\s+(\d{2}:\d{2})', text)
    if date_time_match_alt:
        return date_time_match_alt.group(1), date_time_match_alt.group(2)

    # Alternative pattern 2 (e.g., "mrcsite2_05 20230502 18:55")
    date_time_match_alt2 = re.search(r'mrcsite\d+_\d+\s(\d{4})(\d{2})(\d{2})\s(\d{2}:\d{2})', text)
    if date_time_match_alt2:
        date = f"{date_time_match_alt2.group(1)}-{date_time_match_alt2.group(2)}-{date_time_match_alt2.group(3)}"
        return date, date_time_match_alt2.group(4)

    return None, None

def convert_csv_to_excel(csv_file_path, excel_file_path):
    df = pd.read_csv(csv_file_path)
    extracted_info = df.apply(lambda x: extract_refinery_equipment_path_event_type(x['Subject'], x['Body']), axis=1)
    df[['Refinery', 'Equipment', 'Path(s)/Site(s)/PM', 'Event Type', 'Date', 'Time']] = pd.DataFrame(extracted_info.tolist(), index=df.index)

    df['Subject'], df['Alarm Message'] = df['Subject'], df['Body']
    formatted_df = df[['Refinery', 'Equipment', 'Path(s)/Site(s)/PM', 'Event Type', 'Date', 'Time', 'Subject', 'Alarm Message']]
    formatted_df.to_excel(excel_file_path, index=False)

# Example usage
csv_file_path = ''/mnt/data/emails.CSV'  # Replace with your CSV file path
excel_file_path = ''/mnt/data/output.xlsx'  # Replace with your desired output Excel file path

convert_csv_to_excel(csv_file_path, excel_file_path)