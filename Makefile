local/install:
	pipenv install --dev --skip-lock

local/shell:
	pipenv shell

local/lint:
	flake8 .

local/test:
	ENV=test python -m pytest

docker/build: 
	docker-compose build morse-code-translator

docker/up: default-env
	docker-compose up -d

docker/down:
	docker-compose down

default-env:
	@if [ ! -f .env ]; then cp env.template .env; fi;