dev:
	uv run python urlshortener/manage.py runserver

migrations:
	uv run python urlshortener/manage.py makemigrations

migrate:
	uv run python urlshortener/manage.py migrate

lint:
	uv run ruff check urlshortener

lint-fix:
	uv run ruff check urlshortener --fix