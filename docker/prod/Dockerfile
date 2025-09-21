
# Build stage: includes build-essential and dev dependencies

FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS build

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    gettext \
    wait-for-it \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock:rw \
    uv sync --no-install-project

COPY . ${APP_HOME}

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock:rw \
    uv sync

FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS production

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq5 \
    gettext \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 voidlink \
    && useradd --uid 1000 --gid voidlink --shell /bin/bash --create-home voidlink

COPY --from=build --chown=voidlink:voidlink ${APP_HOME}/.venv ${APP_HOME}/.venv
COPY --from=build --chown=voidlink:voidlink ${APP_HOME} ${APP_HOME}

ENV PATH="${APP_HOME}/.venv/bin:$PATH" \
    PYTHONPATH="${APP_HOME}/.venv/lib/python3.13/site-packages:$PYTHONPATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./docker/entrypoint.sh /entrypoint
COPY ./docker/prod/start-app.sh /start-app
COPY ./docker/prod/start-worker.sh /start-celeryworker
COPY ./docker/prod/start-beat.sh /start-celerybeat
COPY ./docker/prod/start-flower.sh /start-celeryflower

RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint \
    && sed -i 's/\r$//g' /start-app && chmod +x /start-app \
    && sed -i 's/\r$//g' /start-celeryworker && chmod +x /start-celeryworker \
    && sed -i 's/\r$//g' /start-celerybeat && chmod +x /start-celerybeat \
    && sed -i 's/\r$//g' /start-celeryflower && chmod +x /start-celeryflower \
    && chown -R voidlink:voidlink ${APP_HOME}

USER voidlink

ENTRYPOINT ["/entrypoint"]