from google_images_download import google_images_download
import os
import sys
keyword=input()
response = google_images_download.googleimagesdownload()
arguments = {
  "keywords": keyword,
  "limit": 100,
  "print_urls": True,
  "output_directory": "img",
  "extract-metadata":True,
}
paths = response.download(arguments)
print(paths)
