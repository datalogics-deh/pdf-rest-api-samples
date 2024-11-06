
using Newtonsoft.Json.Linq;
using System.Text;

using (var httpClient = new HttpClient { BaseAddress = new Uri("https://api.pdfrest.com") })
{
    using (var uploadRequest = new HttpRequestMessage(HttpMethod.Post, "upload"))
    {
        uploadRequest.Headers.TryAddWithoutValidation("Api-Key", "xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx");
        uploadRequest.Headers.Accept.Add(new("application/json"));

        var uploadByteArray = File.ReadAllBytes("/path/to/file");
        var uploadByteAryContent = new ByteArrayContent(uploadByteArray);
        uploadByteAryContent.Headers.TryAddWithoutValidation("Content-Type", "application/octet-stream");
        uploadByteAryContent.Headers.TryAddWithoutValidation("Content-Filename", "filename.zip");


        uploadRequest.Content = uploadByteAryContent;
        var uploadResponse = await httpClient.SendAsync(uploadRequest);

        var uploadResult = await uploadResponse.Content.ReadAsStringAsync();

        Console.WriteLine("Upload response received.");
        Console.WriteLine(uploadResult);

        JObject uploadResultJson = JObject.Parse(uploadResult);
        var uploadedID = uploadResultJson["files"][0]["id"];
        using (var unzipRequest = new HttpRequestMessage(HttpMethod.Post, "unzip"))
        {
            unzipRequest.Headers.TryAddWithoutValidation("Api-Key", "xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx");
            unzipRequest.Headers.Accept.Add(new("application/json"));

            unzipRequest.Headers.TryAddWithoutValidation("Content-Type", "application/json");


            JObject parameterJson = new JObject
            {
                ["id"] = uploadedID,
            };

            unzipRequest.Content = new StringContent(parameterJson.ToString(), Encoding.UTF8, "application/json"); ;
            var unzipResponse = await httpClient.SendAsync(unzipRequest);

            var unzipResult = await unzipResponse.Content.ReadAsStringAsync();

            Console.WriteLine("Processing response received.");
            Console.WriteLine(unzipResult);
        }
    }
}
