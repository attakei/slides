FROM python:3.8-slim as build

RUN mkdir -p /build/out
WORKDIR /build
COPY pyproject.toml confgen.py config.ini /build/
RUN pip install poetry \
    && poetry install \
    && poetry run confgen -o /build/out

FROM httpd:2.4

# Migrate resources
RUN mkdir -p /opt/preview \
    && echo "Include /opt/preview/*.conf" >> /usr/local/apache2/conf/httpd.conf
COPY --from=build /build/out/ /opt/preview/
COPY site/ public/ /opt/preview/public/