# Build stage
FROM python:3.9-slim as builder

WORKDIR /app
COPY src/requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.9-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
COPY src/color-app.py .

# Set color via environment variable
ENV BG_COLOR="lightblue"  
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["python", "color-app.py"]