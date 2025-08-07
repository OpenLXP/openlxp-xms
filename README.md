# Enterprise Course Catalog: OpenLXP-XMS
The Experience Management Service (XMS) is a part of the OpenLXP Enterprise Course Catalog (ECC) platform. It is  the backend responsible for managing courses/catalogs.

XMS is the user interface facilitating modification and augmentation of records by learning experience owners and managers.

This Django web application enables experience owners/managers to modify/augment experience metadata via (i.e., the "admin portal") REST API. It utilizes the Django admin UI for system configuration and management.

## Prerequisites
### Install Docker & docker-compose
#### Windows & MacOS
- Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) (docker compose included)


#### Linux
You can download Docker Compose binaries from the
[release page](https://github.com/docker/compose/releases) on this repository.

Rename the relevant binary for your OS to `docker-compose` and copy it to `$HOME/.docker/cli-plugins`

Or copy it into one of these folders to install it system-wide:

* `/usr/local/lib/docker/cli-plugins` OR `/usr/local/libexec/docker/cli-plugins`
* `/usr/lib/docker/cli-plugins` OR `/usr/libexec/docker/cli-plugins`

(might require making the downloaded file executable with `chmod +x`)

### Python
`Python >=3.9` : Download and install it from here [Python](https://www.python.org/downloads/).


## 1. Clone the project
Clone the Github repository
```
git clone https://github.com/OpenLXP/openlxp-xms.git
```   

## 2. Set up your environment variables
- Create a `.env` file in the root directory
- The following environment variables are required:

| Environment Variable      | Description |
| ------------------------- | ----------- |
| AWS_ACCESS_KEY_ID         | The Access Key ID for AWS  |
| AWS_SECRET_ACCESS_KEY     | The Secret Access Key for AWS  |
| AWS_DEFAULT_REGION        | The region for AWS |
| CSRF_COOKIE_DOMAIN            | The domain to be used when setting the CSRF cookie. This can be useful for easily allowing cross-subdomain requests to be excluded from the normal cross site request forgery protection. |
| CSRF_TRUSTED_ORIGINS            | A list of trusted origins for unsafe requests |
| DB_HOST                   | The host name, IP, or docker container name of the database |
| DB_NAME                   | The name to give the database |
| DB_PASSWORD               | The password for the user to access the database |
| DB_ROOT_PASSWORD          | The password for the root user to access the database, should be the same as `DB_PASSWORD` if using the root user |
| DB_USER                   | The name of the user to use when connecting to the database. When testing use root to allow the creation of a test database |
| DJANGO_SUPERUSER_EMAIL    | The email of the superuser that will be created in the application |
| DJANGO_SUPERUSER_PASSWORD | The password of the superuser that will be created in the application |
| DJANGO_SUPERUSER_USERNAME | The username of the superuser that will be created in the application |
| ENTITY_ID                 | The Entity ID used to identify this application to Identity Providers when using Single Sign On | 
| LOG_PATH                  | The path to the log file to use |
| SECRET_KEY_VAL            | The Secret Key for Django |
| SP_PRIVATE_KEY            | The Private Key to use when this application communicates with Identity Providers to use Single Sign On |
| SP_PUBLIC_CERT            | The Public Key to use when this application communicates with Identity Providers to use Single Sign On |


## 3. Deployment
1. Create the OpenLXP Docker network.
    Open a terminal and run the following command in the root directory of the project.
    ```
    docker network create openlxp
    ```

2. Run the docker compose command below to deploy XMS with its resources. 
    ```
    docker-compose up -d --build
    ```

## 4. Configuration for XMS
1. Navigate over to `http://localhost:8000/admin/` in your browser and login to the Django Admin page with the admin credentials set in your `.env` (`DJANGO_SUPERUSER_EMAIL` & `DJANGO_SUPERUSER_PASSWORD`)

2. <u>CONFIGURATIONS</u>
    - Configure Experience Management Service (XMS)
        1. Click on `Xms connections` > `Add Xms connection`
            - Enter configurations below:

                - `Target xis metadata api`: Metadata API Endpoint to connect to on an XIS instance.

                - `XIS catalogs api`: Catalogs API Endpoint to connect to on an XIS instance.

3. <u>OPENLXP AUTHENTICATION</u>
    - Configure Security Assertion Markup Language (SAML)
        1. Click on `Saml configurations` > `Add saml configurations`
            - Enter configurations below:

                - `Name`: The name that will be used to identify the IdP in the URL.

                - `Entity id`: The unique name provided by the IdP.

                - `Url`: The connection URL to connect to the IdP at.

                - `Cert`: The public cert used to connect to the IdP.

                - `Attribute mapping`: The JSON formatted mapping to convert attributes provided by the IdP, to a User in this system.

## 5. Removing Deployment
To destroy the created resources, simply run the docker-compose command below in your terminal:
    
    
    docker-compose down

## Troubleshooting
- If the container builds but crashes, or error logs a bunch of unrecognized commands, the issue is usually incorrect line endings. Most IDEs/Text Editors allow changing the line endings, but the dos2unix utility can also be used to change the line endings of `start-app.sh` and `start-server.sh` to LF.


- A good basic troubleshooting step is to use `docker-compose down` and then `docker-compose up --build` to rebuild the app image; however, this will delete everything in the database.

- XMLSEC
    - If the build fails when pip tries to install xmlsec, the issue is usually missing libraries.

    - The xmlsec package includes instructions for installing the libraries on common platforms in the [documentation](https://github.com/mehcode/python-xmlsec/blob/master/README.rst#install)

## Testing

To run the automated tests on the application run the command below

Test coverage information will be stored in an htmlcov directory

```bash
docker-compose --env-file .env run app sh -c "coverage run manage.py test && coverage html && flake8"
```

## Authentication

The environment variables `SP_PUBLIC_CERT`, `SP_PRIVATE_KEY` , and `SP_ENTITY_ID` must be defined (if using docker-compose the variables can be passed through).

Information on the settings for the authentication module can be found on the [OpenLXP-Authentication repo](https://github.com/OpenLXP/openlxp-authentication).


## Authorization

The setting `OPEN_ENDPOINTS` can be defined in the django settings file.
It is a list of strings (regex notation may be used) for URLs that should not check for authentication or authorization.

## License

 This project uses the [MIT](http://www.apache.org/licenses/LICENSE-2.0) license.
