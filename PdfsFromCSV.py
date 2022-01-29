import csv
import sys
import requests
import os
import pandas as pd

folder_location = r'scraped_pdfs'
df = pd.read_csv('books.csv')
for row in df["book url"] :
    if 'http' in row:
        try:

            response = requests.get(row)
            pdf=open(row.split('/')[-1], "wb")
            pdf.write(response.content, folder_location)
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))            
            
            continue
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
            
            continue
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
            continue
        except KeyboardInterrupt:
            print("Someone closed the program")


