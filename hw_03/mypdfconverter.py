import argparse
from pdfminer.high_level import extract_text
import os

parser = argparse.ArgumentParser(description='Accept docx or pdf and convert to txt.')
parser.add_argument('file', help='Enter file name: ')
args = parser.parse_args()

if (args.file.endswith('.pdf') or args.file.endswith('.docx')) and os.path.exists(args.file) == True:
  text = extract_text(args.file)
  print(text)
else:
  print('Не могу принять файл')

