import pandas as pd
import chardet
import html

properties_data = pd.read_csv("./data/raw/data.csv")

properties_data['Locality name'] = properties_data['Locality name'].apply(lambda x: html.unescape(x))

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']

print(properties_data)
#print(detect_encoding("./data/raw/data.csv"))
#print(html.unescape("Hennuy&#xE8;res"))