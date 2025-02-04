FROM oraclelinux:9

RUN  dnf -y install oracle-instantclient-release-23ai-el9 && \
     dnf -y install oracle-instantclient-basic oracle-instantclient-devel oracle-instantclient-sqlplus && \
     rm -rf /var/cache/dnf

WORKDIR /app

RUN dnf install -y python3 python3-pip && \
    dnf clean all

RUN useradd -r -s /bin/false app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R app:app /app

USER app

CMD ["init.sh"]