# News-Author-Extraction

### Usage:
```uvicorn main:app --host 0.0.0.0 --port 3578```

Send POST request to localhost:3578/api/v1/pontianak with 1 parameter named "text".

### Output:
```
{
    'result': {
        'text': \<your text input: str\>
        'author': \<result: str\>
    },
    'status': \<binary\>
    'error-message': \<str\> (Only shown when status is error (0).)
}
```
