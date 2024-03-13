# bynet_installer
export snow_url="https://bynetprod.service-now.com/api/x_bdml_nimbus/v1/nimbus_api/"
export api_key="123"

curl -X GET "$snow_url/get_packages" -H "x-api-key: $api_key" -G "?aws_account_id=$aws_account_id"

חשוב להשתמש בקוד בזהירות.
Explanation:

curl: The command to use curl.
-X GET: Specifies the HTTP method as GET.
https://<hots>/api: The URL of your API endpoint. Replace <hots> with the actual hostname.
-H "x-api-key: 123": Sets the header "x-api-key" with the value "123".
-G: Instructs curl to URL-encode the parameters in the following string.
"?aws_account_id=abc123": Defines the parameter "aws_account_id" with the value "abc123" appended to the URL with a question mark.
This command sends a GET request to the specified URL with the "x-api-key" header and the "aws_account_id" parameter
