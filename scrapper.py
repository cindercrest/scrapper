from datetime import datetime
import sys
from bs4 import BeautifulSoup
import requests
import json

def main():
  if len(sys.argv) != 2:
    sys.exit("Usage: python script.py Url")
  url = sys.argv[1]
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
          "AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/120.0.0.0 Safari/537.36"
      )
  }
  #Makning get Request
  try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    sys.exit(f"Connection failed: {e}")
  #Parsing it using html parser
  soup = BeautifulSoup(response.text, "html.parser")
  print(f"Successfully connected to Webpage!")
  
  #scraping
  scraped_data = []
  
  #Scraping Headers
  for header in soup.find_all(['h1','h2','h3']):
      text = header.get_text(strip=True)
      if text:
          scraped_data.append({"type":"heading","content":text})
  #links
  for a in soup.find_all("href" if False else "a",href=True):
      link_text = a.get_text(strip=True)
      link_url = a["href"]
      if link_text and link_url.startswith("http"):
          scraped_data.append({"type":"link","text":link_text,"url":link_url})
  #saving to local machine in file
  output_file = "scraped_output.json"
  with open(output_file,"w",encoding="utf-8") as f:
      json.dump(scraped_data,f,indent=4)
  print(f"Saved {len(scraped_data)} items to {output_file}")

if __name__ == "__main__":
  main()
