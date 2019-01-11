from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {
  "keywords": "Peters two keys",
  "limit": 100,
  "print_urls": True,
  "usage_rights": "labeled-for-reuse",
  "output_directory": "img",
  "extract-metadata":True,
}
paths = response.download(arguments)
print(paths)
