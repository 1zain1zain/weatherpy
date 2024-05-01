

#### Description
This is a Python app built with FastAPI, a microframework.

#### Note: Don't forget to add your API_KEY to the environment!
```bash
set API_KEY=your_api_key_here
or
$env:API_KEY="your_api_key_here"
```

```bash
# To run the tests
# 1. create a virtual environment, 2. activate it and 3. invoke pytest
$ python -m venv .venv
$ .venv\Scripts\activate
$ python -m pytest
```

```bash
# To run the app
$ uvicorn
```

```bash
Use curl to test the endpoint from your cli. 
Or use Postman or Insomnia if you prefer a GUI.

- - - - - -

# curl example to GET the payload for lat=42.278046&lon=-83.738220 
> $ curl http://localhost:8000/weather/42.278046,-83.738220

JSON response example: 
{ message: { fahrenheit: temp, condition: condition } }   
```


#### Major Dependencies
1. [FastAPI](https://github.com/tiangolo/fastapi) official repository.
2. [uvicorn](https://github.com/encode/uvicorn) is required to run the app.
3. [Python](https://www.python.org/downloads/) is required.

<p align="left">
  This app is built with FastAPI. FastAPI is a microframework for Python.
  <a href="https://fastapi.tiangolo.com/" target="blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png/" width="30" alt="FastAPI Logo" /></a>
</p>
