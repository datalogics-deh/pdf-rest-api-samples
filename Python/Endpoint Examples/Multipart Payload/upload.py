from requests_toolbelt import MultipartEncoder
import requests
import json

# By default, we use the US-based API service. This is the primary endpoint for global use.
api_url = "https://api.pdfrest.com"

# For GDPR compliance and enhanced performance for European users, you can switch to the EU-based service by uncommenting the URL below.
# For more information visit https://pdfrest.com/pricing#how-do-eu-gdpr-api-calls-work
#api_url = "https://eu-api.pdfrest.com"

upload_endpoint_url = api_url+'/upload'

# The /upload endpoint can take one or more files or urls as input and transfers them to the pdfRest server for processing.
# This sample takes 3 files and uploads it to the pdfRest service.
upload_request_data = []

# Array of tuples that contains information about the file that will be uploaded to the pdfRest server.
# The 'application/pdf' string below is known as a MIME type, which is a label used to identify the type of a file so that it is handled properly by software.
# Please see https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for more information about MIME types.
files = [
    ('file_name.pdf', open('/path/to/file', 'rb'), 'application/pdf'),
    ('file_name2.pdf', open('/path/to/file', 'rb'), 'application/pdf'),
    ('file_name.jpg', open('/path/to/file', 'rb'), 'image/jpeg')
]

# Structure the data that will be sent to POST upload request as an array of tuples
for i in range(len(files)):
    upload_request_data.append(("file", files[i]))

mp_encoder_upload = MultipartEncoder(
    fields=upload_request_data
)

# Let's set the headers that the upload endpoint expects.
# Since MultipartEncoder is used, the 'Content-Type' header gets set to 'multipart/form-data' via the content_type attribute below.
headers = {
    'Accept': 'application/json',
    'Content-Type': mp_encoder_upload.content_type,
    'Api-Key': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # place your api key here
}

print("Sending POST request to upload endpoint...")
response = requests.post(upload_endpoint_url, data=mp_encoder_upload, headers=headers)

print("Response status code: " + str(response.status_code))

if response.ok:
    response_json = response.json()
    print(json.dumps(response_json, indent = 2))
else:
    print(response.text)
