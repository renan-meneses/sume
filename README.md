# Sume

Sistema voltado a buscar previsões do tempo

<p align="center">
  <img width="340" height="160" src="https://entrecontos.files.wordpress.com/2019/02/aarvore.png">
</p>
## Pré-requisitos
- Python Python 3.10.8
- Flask 2.1.3
- pymongo 4.2.0

## Montagem do ambiente de desenvolvimento

### Amebiente Docker 

    ```sh
docker-compose up -p
```

### Ambiente Local

Criar banco mongo(caso nao tenhao instalado na maquina):

   ```sh
docker-compose up -p mongo
```

Criar env: 
```sh
python3.10 -m venv venv
```

Acessar:

```sh
source venv/bin/activate
```
intalar a dependencias:

```sh
pip install --upgrade pip && pip install -r src/requirements.txt
```

rodar aplicação:

```sh
 python src/app.py
```
### Instalar dependências de sistema
