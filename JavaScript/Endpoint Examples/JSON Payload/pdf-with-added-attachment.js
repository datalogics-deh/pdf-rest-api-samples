var axios = require("axios");
var FormData = require("form-data");
var fs = require("fs");

// By default, we use the US-based API service. This is the primary endpoint for global use.
var apiUrl = "https://api.pdfrest.com";

/* For GDPR compliance and enhanced performance for European users, you can switch to the EU-based service by uncommenting the URL below.
 * For more information visit https://pdfrest.com/pricing#how-do-eu-gdpr-api-calls-work
 */
//var apiUrl "https://eu-api.pdfrest.com";

var pdf_upload_data = fs.createReadStream("/path/to/pdf_file");

var pdf_upload_config = {
  method: "post",
  maxBodyLength: Infinity,
  url: apiUrl + "/upload",
  headers: {
    "Api-Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // Replace with your API key
    "Content-Filename": "pdf_filename.pdf",
    "Content-Type": "application/octet-stream",
  },
  data: pdf_upload_data, // set the data to be sent with the request
};

// send request and handle response or error
axios(pdf_upload_config)
  .then(function (pdf_upload_response) {
    var pdf_uploaded_id = pdf_upload_response.data.files[0].id;

    var attachment_upload_data = fs.createReadStream(
      "/path/to/attachment_file"
    );

    var attachment_upload_config = {
      method: "post",
      maxBodyLength: Infinity,
      url: apiUrl + "/upload",
      headers: {
        "Api-Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // Replace with your API key
        "Content-Filename": "attachment_filename.xml",
        "Content-Type": "application/octet-stream",
      },
      data: attachment_upload_data, // set the data to be sent with the request
    };

    axios(attachment_upload_config)
      .then(function (attachment_upload_response) {
        console.log(JSON.stringify(attachment_upload_response.data));
        var attachment_uploaded_id =
          attachment_upload_response.data.files[0].id;

        var attach_config = {
          method: "post",
          maxBodyLength: Infinity,
          url: apiUrl + "/pdf-with-added-attachment",
          headers: {
            "Api-Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // Replace with your API key
            "Content-Type": "application/json",
          },
          data: {
            id: pdf_uploaded_id,
            id_to_attach: attachment_uploaded_id,
          }, // set the data to be sent with the request
        };

        // send request and handle response or error
        axios(attach_config)
          .then(function (attach_response) {
            console.log(JSON.stringify(attach_response.data));
          })
          .catch(function (error) {
            console.log(error);
          });
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
