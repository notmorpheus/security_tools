# security_tools

## Rate Limit Tester(s)
To test the rate limits of an API endpoint.

## Why? 
1. Python's `requests` module is slow and is not ideal when trying to make burst requests, crucial in testing rate limits of an endpoint. 
2. This tool utilizes Python's aiohttp library to make asynchronous HTTP requests