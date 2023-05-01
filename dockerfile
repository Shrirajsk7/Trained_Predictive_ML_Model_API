FROM python:3.9

RUN pip install joblib
RUN pip install python-multipart

WORKDIR /app

COPY requirements.txt /app

# Upgrade pip and install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . /app


EXPOSE 8000
