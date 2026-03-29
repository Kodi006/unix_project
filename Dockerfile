# Stage 1: Builder
FROM python:3.10-slim as builder

WORKDIR /app
COPY wiki/requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Final image
FROM python:3.10-slim

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY wiki/ /app/

# Expose port and run Gunicorn
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wiki.wsgi:application"]
