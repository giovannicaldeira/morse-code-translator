# morse-code-translator

## Description

This project is a morse code translator developed using `python` with `Flask-SocketIO`.


## Technologies and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Pipenv](https://github.com/pypa/pipenv)


## Files structure

### Main structure

Item | Type | Description
--- | --- | ---
`app` | directory | contains only application files
`tests` | directory | contains only test files
`docs` | directory | contains only docs files
`.flake8` | file | flake8 coding style definitions
`env.template` | file | sample of env vars
`run.py` | file | the application`s entrypoint

### App directory structure

Directory | Description
--- | ---
`common` | common libraries like `log.py`
`controllers` | main path of controllers, like `morse.py`
`handlers` | handlers functions used by sockets
`static` | path to javascript and css files used by html
`templates` | main path of html files to be rendered


## How to install, run, test

### Local commands

Installing local dependencies
```shell
    make local/install
```

Setting local environment
```shell
    make local/shell
```

Running local tests
```shell
    make local/test
```

Running local lint
```shell
    make local/lint
```

### Docker commands

Building docker image
```shell
    make docker/build
```

Executing application
```shell
    make docker/up
```

Stoping application
```shell
    make docker/down
```

## How to test

Execute the following commands:
```shell
    make docker/build
    make docker/up
```

After this you can access the translator on: `http://localhost:5001/`

Use one blank space to separate letters and two blank spaces to separate words. For example:

```--- .-.. .-  -- ..- -. -.. ---```
