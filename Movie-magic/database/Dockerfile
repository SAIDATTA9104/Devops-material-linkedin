FROM mysql:8.0.33

ENV MYSQL_ROOT_PASSWORD=moviepass \
    MYSQL_DATABASE=moviemagic \
    MYSQL_USER=appuser \
    MYSQL_PASSWORD=apppass

COPY init.sql /docker-entrypoint-initdb.d/

RUN chmod 644 /docker-entrypoint-initdb.d/*

HEALTHCHECK --interval=15s --timeout=10s --retries=10 \
    CMD mysqladmin ping -u root -p${MYSQL_ROOT_PASSWORD} || exit 1

VOLUME /var/lib/mysql