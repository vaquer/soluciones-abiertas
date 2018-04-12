FROM alpine:3.5
MAINTAINER Francisco Vaquero <f.vaquero@opianalytics.com>

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

RUN mkdir dgm_tools && apk update && \
    apk add --no-cache --virtual build-deps gcc musl-dev git jpeg-dev zlib-dev && \
    apk add python3 \
            python3-dev \
            postgresql-dev \
            linux-headers pcre-dev && \
    python3 -m ensurepip

ADD . dgm_tools/

RUN pip3 install --upgrade pip setuptools && pip3 install -r dgm_tools/requirements.txt && \
    chmod 777 dgm_tools/start.sh
    # which uwsgi

EXPOSE 8000
EXPOSE 9191

ENTRYPOINT [ "./dgm_tools/start.sh" ]
