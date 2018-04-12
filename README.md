# Catalogo de Soluciones Abiertas

Micro CMS para datos.gob.mx que condensa la información de herramientas open source utiles para el consumo, administración y creación de datos abiertos.

## Requerimientos
- Python 3.5.2
- Django 2.0.1
- Postgres 9.5

# Modo desarrollo
Para correr el proyecto en modo desarrollo se debe clonar el repositorio:

```sh
git clone git@github.com:opintel/catalogo-herramientas-dgm.git
```

Posteriormente dentro de la carpeta del proyecto se deben instalar las dependencias:
```sh
cd dgm_tools
pip install -r requirements.txt
```

Por ultimo configurar las variables de ambiente necesarias:
```sh
export DATABASE_USER=catalogo
export DATABASE_NAME=catalogo
export DATABASE_PASSWORD=catalogo
export DATABASE_HOST=0.0.0.0
export DEBUG=True
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```

# Implementacion Kubernetes

Para implementar en un cluster de kubernetes correr los siguientes comandos (kubernetes 1.9):

#### Creación de deployments

```sh
kubectl apply -f kubernetes/volumen-claim-soluciones.yml
kubectl apply -f kubernetes/soluciones-postgres-deploy.yml
kubectl apply -f kubernetes/soluciones-deploy.yml
```

#### Creación de servicios
```sh
kubectl apply -f kubernetes/soluciones-postgres-service.yml
kubectl apply -f kubernetes/soluciones-service.yml
```

### Notas
La configuración y montado de volumenes puede variar dependendiendo de la versión de kubernetes. Para mas detalles consultar la documentación de [kubernetes](https://kubernetes.io/docs/concepts/storage/volumes/).

El [Catalogo](https://datos.gob.mx/soluciones-abiertas/) live esta productivo.
