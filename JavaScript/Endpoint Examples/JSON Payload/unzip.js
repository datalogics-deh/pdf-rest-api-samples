var axios = require("axios");
var FormData = require("form-data");
var fs = require("fs");

var upload_data = fs.createReadStream("/path/to/file");

var upload_config = {
  method: "post",
  maxBodyLength: Infinity,
  url: "https://api.pdfrest.com/upload",
  headers: {
    "Api-Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // Replace with your API key
    "Content-Filename": "filename.zip",
    "Content-Type": "application/octet-stream",
  },
  data: upload_data, // set the data to be sent with the request
};

// send request and handle response or error
axios(upload_config)
  .then(function (upload_response) {
    console.log(JSON.stringify(upload_response.data));
    var uploaded_id = upload_response.data.files[0].id;

    var unzip_config = {
      method: "post",
      maxBodyLength: Infinity,
      url: "https://api.pdfrest.com/unzip",
      headers: {
        "Api-Key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // Replace with your API key
        "Content-Type": "application/json",
      },
      data: { id: uploaded_id }, // set the data to be sent with the request
    };

    // send request and handle response or error
    axios(unzip_config)
      .then(function (unzip_response) {
        console.log(JSON.stringify(unzip_response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
