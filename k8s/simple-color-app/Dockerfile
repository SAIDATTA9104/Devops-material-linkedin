FROM python:3.9-slim

WORKDIR /app
# Create a non-root user and switch to it
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Copy files and install dependencies
COPY color-app.py .
RUN pip install --no-cache-dir --user flask

# Ensure user's local bin is in PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

EXPOSE 5000
CMD ["python", "color-app.py"]