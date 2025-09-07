export COMPOSE_FILE := "compose.yml"

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

# runserver: Start development server.
runserver:
    @echo "Starting development server..."
    @docker compose up -d --remove-orphans
    uv run ./manage.py tailwind runserver

test:
    @echo "Running tests..."
    @docker compose up -d --remove-orphans
    DJANGO_ENV=testing uv run ./manage.py test
    @echo "Django Tests Completed"
    @echo "Running playwright tests..."
    DJANGO_ENV=testing uv run pytest ./tests/playwright

test-headed:
    @echo "Running headed tests..."
    @docker compose up -d --remove-orphans
    DJANGO_ENV=testing uv run pytest ./tests/playwright --headed #--slowmo 1000

# prune: Remove containers and their volumes.
prune *args:
    @echo "Killing containers and removing volumes..."
    @docker compose down -v "{{args}}"

# logs: View container logs
logs *args:
    @docker compose logs -f "{{args}}"

# manage: Executes `manage.py` command.
manage *args:
    uv run python ./manage.py "{{args}}"

format:
    @echo "Formatting Code..."
    uv run ruff check --fix
    uv run ruff format