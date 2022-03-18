# Enterprise Course Catalog: OPENLXP-XMS


# Prerequisites
`Python >=3.7` : Download and install python from here [Python](https://www.python.org/downloads/).

`Docker` : Download and install Docker from here [Docker](https://www.docker.com/products/docker-desktop).

`XML Security Headers` : Download and install XML Security Headers for your operating system (`libxml2-dev` and `libxmlsec1-dev` in some linux distros).


## Environment Variables

The list of required variables is below

`DB_NAME` - The name to give the database

`DB_USER` - The name of the user to use when connecting to the database.
When testing use root to allow the creation of a test database

`DB_PASSWORD` - The password for the user to access the database

`DB_ROOT_PASSWORD` - The password for the root user to access the database, should be the same as `DB_PASSWORD` if using the root user

`DB_HOST` - The host name, IP, or docker container name of the database

`DJANGO_SUPERUSER_USERNAME` - The username of the superuser that will be created in the application

`DJANGO_SUPERUSER_PASSWORD` - The password of the superuser that will be created in the application

`DJANGO_SUPERUSER_EMAIL` - The email of the superuser that will be created in the application

`AWS_ACCESS_KEY_ID` - The Access Key ID for AWS

`AWS_SECRET_ACCESS_KEY` - The Secret Access Key for AWS

`AWS_DEFAULT_REGION` - The region for AWS

`SECRET_KEY_VAL` - The Secret Key for Django

`LOG_PATH` - The path to the log file to use

`ENTITY_ID` - The Entity ID used to identify this application to Identity Providers when using Single Sign On 

`SP_PUBLIC_CERT` - The Public Key to use when this application communicates with Identity Providers to use Single Sign On

`SP_PRIVATE_KEY` - The Private Key to use when this application communicates with Identity Providers to use Single Sign On

`CERT_VOLUME` - The path to the certificate (on the host machine) to use when connecting to AWS


# Installation

1. Clone the Github repository:

    https://github.com/OpenLXP/openlxp-xms.git

2. Open terminal at the root directory of the project.
    
    example: ~/PycharmProjects/openlxp-xms 

3. Run command to install all the requirements from requirements.txt 
    
    docker-compose build.

4. Once the installation and build are done, run the below command to start the server.
    
    docker-compose up

5. Once the server is up, go to the admin page:
    
    http://localhost:8000/admin (replace localhost with server IP)


# Configuration

1. On the Admin page, log in with the admin credentials 


2. `Add xms configuration`: Configure Experience Management Service (XMS):

    `Target xis metadata api`: Metadata API Endpoint to connect to on an XIS instance.

    `XIS catalogs api`: Catalogs API Endpoint to connect to on an XIS instance.


3. `Add Saml configuration`: Configure Security Assertion Markup Language (SAML):
    
    `Name`: The name that will be used to identify the IdP in the URL.

    `Entity id`: The unique name provided by the IdP.

    `Url`: The connection URL to connect to the IdP at.

    `Cert`: The public cert used to connect to the IdP.

    `Attribute mapping`: The JSON formatted mapping to convert attributes provided by the IdP, to a User in this system.


4. `Add sender email configuration`: Configure the sender email address from which conformance alerts are sent.


5. `Add receiver email configuration` : 
Add an email list to send conformance alerts. When the email gets added, an email verification email will get sent out. In addition, conformance alerts will get sent to only verified email IDs.


# Troubleshooting

A good basic troubleshooting step is to use `docker-compose down` and then `docker-compose up --build` to rebuild the app image; however, this will delete everything in the database.

## XMLSEC

If the build fails when pip tries to install xmlsec, the issue is usually missing libraries.

The xmlsec package includes instructions for installing the libraries on common platforms in the [documentation](https://github.com/mehcode/python-xmlsec/blob/master/README.rst#install)

## Line Endings

If the container builds but crashes or logs an error of unrecognized commands, the issue is usually incorrect line endings.

Most IDEs/Text Editors allow changing the line endings, but the dos2unix utility can also be used to change the line endings of `start-app.sh` and `start-server.sh` to LF.


# Update

To update an existing installation: 

1. Pull the latest changes using git

2. Restart the application using `docker-compose restart`

# Testing

To run the automated tests on the application run the command below

Test coverage information will be stored in an htmlcov directory

```bash
docker-compose --env-file .env run app sh -c "coverage run manage.py test && coverage html && flake8"
```

# Authentication

The environment variables `SP_PUBLIC_CERT`, `SP_PRIVATE_KEY` , and `SP_ENTITY_ID` must be defined (if using docker-compose the variables can be passed through).

Information on the settings for the authentication module can be found on the [OpenLXP-Authentication repo](https://github.com/OpenLXP/openlxp-authentication).


# Authorization

The setting `OPEN_ENDPOINTS` can be defined in the django settings file.
It is a list of strings (regex notation may be used) for URLs that should not check for authentication or authorization.