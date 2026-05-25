# Multi-stage build for Python PDF processing tools
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final runtime stage
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd -m -u 1000 worker

# Copy dependencies from builder
COPY --from=builder --chown=worker:worker /root/.local /home/worker/.local

# Set environment variables
ENV PATH=/home/worker/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

# Copy application code
COPY --chown=worker:worker scripts/ ./scripts/

# Switch to non-root user
USER worker

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=1 \
    CMD python -m py_compile scripts/*.py || exit 1

# Default command
ENTRYPOINT [ "python" ]
CMD [ "--version" ]
