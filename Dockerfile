ARG BASE_REGISTRY=registry1.dso.mil
ARG BASE_IMAGE=ironbank/redhat/python/python39
ARG BASE_TAG=3.9

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}
USER root

RUN yum update -y && yum install -y libxml2-devel xmlsec1 xmlsec1-openssl openssl libtool-ltdl pkg-config gcc gcc-c++ && \
    # Copy/extract openlxp-ecc-xms source code
    mkdir -p /tmp/openlxp-xms

WORKDIR /tmp/openlxp-xms/
COPY openlxp-xms.tar.gz .

RUN tar -xvf ./openlxp-xms.tar.gz --strip-components=1 && \
    cp ./requirements.txt ./start-app.sh ./start-server.sh /tmp/ && \
    # Requirements for xms   
    if [ ! -f /tmp/debug.log ]; then touch /tmp/debug.log ; fi && \
    chmod a=rwx /tmp/debug.log && \
    chmod +x /tmp/start-server.sh && \
    chmod +x /tmp/start-app.sh && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod -s /usr/bin/write && \
    chmod -s /var/lib/tpm2-tss/system/keystore && \
    # remove unnnecessary files
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/test_apple.py && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/__pycache__/test_keycloak.cpython-39.pyc && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/__pycache__/test_apple.cpython-39.pyc && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/testkey.pem && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/test_keycloak.py && \
    chown -R 1001:1001 /tmp/openlxp-xms/

WORKDIR /tmp/openlxp-xms/
RUN yum clean all

USER 1001

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
