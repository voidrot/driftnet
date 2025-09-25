export COMPOSE_FILE := "compose.yaml"

## Just does not yet manage signals for subprocesses reliably, which can lead to unexpected behavior.
## Exercise caution before expanding its usage in production environments.
## For more information, see https://github.com/casey/just/issues/2473 .


# Default command to list all available commands.
default:
    @just --list

# build: Build python image.
build:
    @echo "Building python image..."
    @docker compose build

# up: Start up containers.
up:
    @echo "Starting up containers..."
    @docker compose up -d --remove-orphans

# down: Stop containers.
down:
    @echo "Stopping containers..."
    @docker compose down

# run: Start development server.
run:
    @echo "Starting development server..."
    @docker compose up -d --remove-orphans
    uv run ./manage.py tailwind runserver

# format: Format code using ruff and djlint.
format:
    @echo "Formatting Code..."
    -uv run ruff check --fix --unsafe-fixes
    -uv run ruff format
    -uv run djlint . --reformat

# make-migrations: Create new migrations based on the changes detected to your models. Optionally takes app name as argument.
make-migrations *args:
    @echo "Making migrations..."
    @docker compose up -d --remove-orphans
    uv run python ./manage.py makemigrations {{args}}

# migrate: Apply migrations to the database. Optionally takes app name as argument.
migrate *args:
    @echo "Applying migrations..."
    @docker compose up -d --remove-orphans
    uv run python ./manage.py migrate {{args}}

# test: run unit tests
test $DJANGO_ENV="testing":
    @echo "Running tests..."
    @docker compose up -d --remove-orphans
    uv run python ./manage.py migrate
    uv run pytest -q

e2e $DJANGO_ENV="testing":
    @echo "Running end-to-end tests..."
    @docker compose up -d --remove-orphans
    pytest -q e2e
