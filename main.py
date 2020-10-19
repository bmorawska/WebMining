from datetime import datetime, timedelta
import pandas as pd
from tqdm import tqdm

# https://www.cs.waikato.ac.nz/~ml/weka/arff.html
# https://www.tutorialspoint.com/weka/weka_file_formats.htm


def date_formatter(date: str) -> (str, str):
    date_object = datetime.strptime(date[0:20], r"%d/%b/%Y:%H:%M:%S")
    offset = date[21:]
    sign = offset[0]
    offset_hour = int(offset[1:3])
    offset_min = int(offset[3:5])
    if sign == '-':
        date_object = date_object - timedelta(hours=offset_hour, minutes=offset_min)
    elif sign == '+':
        date_object = date_object + timedelta(hours=offset_hour, minutes=offset_min)

    if day_hour_separated:
        formatted_date_day = date_object.strftime("%d-%m-%Y")
        formatted_date_hour = date_object.strftime("%H:%M:%S")
        return formatted_date_day, formatted_date_hour

    formatted_date = date_object.strftime("%d-%m-%Y %H:%M:%S")
    return "\'" + formatted_date + "\'"


FILENAME = 'short.csv'
OUTPUT_FILENAME = 'data.arff'
GRAPHIC_FILES = 'jpg|gif|bmp|xmb|png|jpeg|mpg'
day_hour_separated = True

with open(FILENAME) as f:
    lines = f.readlines()

log = []
for line in tqdm(lines):
    ip_end = line.find("- -")
    ip = line[0:ip_end - 1]

    date_end = line.find("]")
    date_start = line.find("[")

    if day_hour_separated:
        day, hour = date_formatter(line[date_start + 1:date_end])
    else:
        date = date_formatter(line[date_start + 1:date_end])

    head_start = line.find('\"')
    head_end = line.rfind('\"')
    head = line[head_start + 1:head_end]

    head_parts = head.split(sep=' ')
    method = head_parts[0]
    address = head_parts[1].replace(',', '').replace(' ', '').replace('%', '').lower()

    try:
        protocol = head_parts[2]
    except IndexError:
        protocol = "None"

    if protocol == '':
        protocol = "None"

    # protocol = protocol.lower().replace('v', '')

    status_and_bytes = line[head_end + 2:]
    status_and_bytes_parts = status_and_bytes.split(sep=' ')
    status = int(status_and_bytes_parts[0])
    bytes = status_and_bytes_parts[1]
    if bytes == '-\n':
        bytes = 0
    else:
        bytes = int(status_and_bytes_parts[1])

    if day_hour_separated:
        row = [day, hour, method, address, protocol, status, bytes]
    else:
        row = [date, method, address, protocol, status, bytes]

    log.append(row)

if day_hour_separated:
    data = pd.DataFrame(data=log, columns=['day', 'hour', 'method', 'address', 'protocol', 'status', 'bytes'])
else:
    data = pd.DataFrame(data=log, columns=['date', 'method', 'address', 'protocol', 'status', 'bytes'])

data = data[data.status == 200]
data = data[~data.address.str.contains(GRAPHIC_FILES)]

if day_hour_separated:
    data.to_csv(OUTPUT_FILENAME, columns=['day', 'hour', 'method', 'address', 'protocol'], index=False, header=False)
else:
    data.to_csv(OUTPUT_FILENAME, columns=['date', 'method', 'address', 'protocol'], index=False, header=False)

print('Dodaję nagłówek...')

if day_hour_separated:
    header = '@RELATION nasa.arff\n\n' \
             '@ATTRIBUTE day DATE "dd-MM-yyyy"\n' \
             '@ATTRIBUTE hour DATE "HH:mm:ss"\n' \
             '@ATTRIBUTE method {GET,HEAD,POST}\n' \
             '@ATTRIBUTE address STRING\n' \
             '@ATTRIBUTE protocol {HTTP/1.0,None,HTTP/V1.0}\n\n' \
             '@DATA'
else:
    header = '@RELATION nasa.arff\n\n' \
             '@ATTRIBUTE date DATE "dd-MM-yyyy HH:mm:ss"\n' \
             '@ATTRIBUTE method {GET,HEAD,POST}\n' \
             '@ATTRIBUTE address STRING\n' \
             '@ATTRIBUTE protocol {HTTP/1.0,None,HTTP/V1.0}\n\n' \
             '@DATA'

with open(OUTPUT_FILENAME, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header.rstrip('\r') + '\n' + content)

print('Skończone.')