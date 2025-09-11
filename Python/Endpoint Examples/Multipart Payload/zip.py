from requests_toolbelt import MultipartEncoder
import requests
import json

# By default, we use the US-based API service. This is the primary endpoint for global use.
api_url = "https://api.pdfrest.com"

# For GDPR compliance and enhanced performance for European users, you can switch to the EU-based service by uncommenting the URL below.
# For more information visit https://pdfrest.com/pricing#how-do-eu-gdpr-api-calls-work
#api_url = "https://eu-api.pdfrest.com"

zip_endpoint_url = api_url+'/zip'

# The /zip endpoint can take one or more file or ids as input and compresses them into a .zip.
# This sample takes 2 files and compresses them into a zip file.
zip_request_data = []

# Array of tuples that contains information about the 2 files that will be compressed into a .zip
# The 'application/pdf' string below is known as a MIME type, which is a label used to identify the type of a file so that it is handled properly by software.
# Please see https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for more information about MIME types.
files = [
    ('file_name.pdf', open('/path/to/file', 'rb'), 'application/pdf'),
    ('file_name.tif', open('/path/to/file', 'rb'), 'image/tiff'),
    ('file_name.bmp', open('/path/to/file', 'rb'), 'image/bmp')
]

# Structure the data that will be sent to POST zip request as an array of tuples
for i in range(len(files)):
    zip_request_data.append(("file", files[i]))

zip_request_data.append(('output', 'example_zip_out'))

mp_encoder_zip = MultipartEncoder(
    fields=zip_request_data
)

# Let's set the headers that the zip endpoint expects.
# Since MultipartEncoder is used, the 'Content-Type' header gets set to 'multipart/form-data' via the content_type attribute below.
headers = {
    'Accept': 'application/json',
    'Content-Type': mp_encoder_zip.content_type,
    'Api-Key': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # place your api key here
}

print("Sending POST request to zip endpoint...")
response = requests.post(zip_endpoint_url, data=mp_encoder_zip, headers=headers)

print("Response status code: " + str(response.status_code))

if response.ok:
    response_json = response.json()
    print(json.dumps(response_json, indent = 2))
else:
    print(response.text)

# If you would like to download the file instead of getting the JSON response, please see the 'get-resource-id-endpoint.py' sample.
