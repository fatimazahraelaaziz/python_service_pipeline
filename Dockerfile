ARG PYTHON_VERSION=3.13.0a4
FROM python:${PYTHON_VERSION}-alpine3.19 as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Update and upgrade packages, including expat/libexpat
RUN apk update && \
    apk upgrade && \
    apk add --no-cache libexpat expat

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy the source code(counter-service.py) into the container.
COPY service-count.py .

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on.
EXPOSE 8080

# Run the application. Logs enabled to see the output logs
CMD ["gunicorn", "service-count:app", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "--error-logfile", "-"]