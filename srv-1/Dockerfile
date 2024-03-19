FROM python:3.12-slim

RUN apt-get update && \
    \
    apt-get install -y \
        curl \
        bash \
        libpq-dev \
    && \
    \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/man/

COPY ./ /backend

WORKDIR /backend

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir  -r requirements.txt

CMD ["./entry.sh"]