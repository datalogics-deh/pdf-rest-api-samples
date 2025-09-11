from requests_toolbelt import MultipartEncoder
import requests
import json

# By default, we use the US-based API service. This is the primary endpoint for global use.
api_url = "https://api.pdfrest.com"

# For GDPR compliance and enhanced performance for European users, you can switch to the EU-based service by uncommenting the URL below.
# For more information visit https://pdfrest.com/pricing#how-do-eu-gdpr-api-calls-work
#api_url = "https://eu-api.pdfrest.com"

flatten_transparencies_pdf_endpoint_url = api_url+'/flattened-transparencies-pdf'

# The /flattened-transparencies-pdf endpoint can take a single PDF file or id as input.
# This sample demonstrates setting quality to 'medium'.
# We have preset 'high', 'medium', and 'low' quality levels available for use. These preset levels do not require the 'profile' parameter.
mp_encoder_flattenTransparenciesPdf = MultipartEncoder(
    fields={
        'file': ('file_name.pdf', open('/path/to/file', 'rb'), 'application/pdf'),
        'output' : 'example_flattenedPdf_out',
        'quality': 'medium',
    }
)

# Let's set the headers that the flattened-transparencies-pdf endpoint expects.
# Since MultipartEncoder is used, the 'Content-Type' header gets set to 'multipart/form-data' via the content_type attribute below.
headers = {
    'Accept': 'application/json',
    'Content-Type': mp_encoder_flattenTransparenciesPdf.content_type,
    'Api-Key': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # place your api key here
}

print("Sending POST request to flattened-transparencies-pdf endpoint...")
response = requests.post(flatten_transparencies_pdf_endpoint_url, data=mp_encoder_flattenTransparenciesPdf, headers=headers)

print("Response status code: " + str(response.status_code))

if response.ok:
    response_json = response.json()
    print(json.dumps(response_json, indent = 2))
else:
    print(response.text)

# If you would like to download the file instead of getting the JSON response, please see the 'get-resource-id-endpoint.py' sample.
