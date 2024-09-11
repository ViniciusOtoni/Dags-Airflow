# 🔥 Dags-Airflow 🔥

Este repositório contém a implementação de pipelines de dados utilizando o **Apache Airflow** em um ambiente Docker, seguindo a arquitetura Medallion (Bronze, Silver, Gold). Esse projeto foi desenvolvido para demonstrar como criar e gerenciar pipelines ETL de forma eficiente, escalável e organizada com o Airflow!

![Airflow Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Apache-airflow-logo.png/1920px-Apache-airflow-logo.png)

---

##  O que é o Apache Airflow?

O Apache Airflow é uma plataforma open-source usada para orquestrar workflows. O Airflow utiliza DAGs (Directed Acyclic Graphs) que definem o fluxo de execução das tarefas, permitindo o gerenciamento de pipelines complexos com facilidade.

### Principais recursos:
- **Escalabilidade**: Orquestração de pipelines em grande escala.
- **Agendador poderoso**: Automatização de workflows através de trigger.
- **Interatividade**: Interface web para monitoramento, logs e execução de tarefas.
  
---

## ⚙️ O que são DAGs?

Cada DAG representa um pipeline de tarefas. As tarefas dentro de uma DAG são executadas em uma ordem específica, dependendo das suas dependências e configurações de agendamento.

Nesse projeto, as DAGs orquestram tarefas ETL para cada camada da arquitetura.

---

## 🏛️ Arquitetura Medallion (Bronze, Silver, Gold):

O modelo Medallion é uma arquitetura comum usada em pipelines de dados. Ele separa os dados em diferentes camadas, promovendo a limpeza e transformação progressiva conforme os dados avançam de uma camada para outra.

- **Bronze**: Camada bruta de dados, onde são armazenados os dados não processados.
- **Silver**: Camada intermediária de dados, onde os dados são limpos e transformados.
- **Gold**: Camada de dados refinados, prontos para consumo para criação de ML e dashboards.

---

## 🛠️ Estrutura do Projeto:

```bash
├── dags/
│   ├── dag_bronze.py   
│   └── dag_silver.py   
│   └── dag_gold.py   
├── ETL/
│   ├── bronze/
│   │   └── main.py  # Classe ETL   
│   ├── silver/
│   │   └── main.py   # Classe ETL  
│   ├── gold/
│      └── main.py    # Classe ETL  
│
├── data/ # Diretório de armazenamento dos dados.
│   ├── d01_raw/
│   ├── d02_bronze/
│   ├── d03_silver/
│   ├── d04_gold/
│
├── docker-compose.yaml # Arquivo de configuração do Docker Compose para o Airflow      
└── README.md           
```
---

## 🐳 Docker Compose:

O projeto utiliza o Docker Compose para orquestrar os containers necessários para executar o Airflow localmente. O arquivo docker-compose.yaml define a infraestrutura mínima necessária, contendo os serviços do scheduler, webserver, e Postgres como banco de dados backend.


- **Scheduler**: Responsável pelo processo de execução das DAGs.
- **Webserver**: Interface web para monitoramento e controle.
- **Postgres**: Banco de dados para armazenamento de metadados.
- **Volumes**: Configuração de volumes para persistência de dados, importação de módulos entre arquivos e logs.

### Exemplo de execução:

```bash
docker-compose up --build
```

Irá subir todos os serviços nescessários... (Imagens, Containers, Volumes)

---

## Requisitos Projeto:

### 1.Pré-requisitos:

- **Docker**: Instalação do Docker.

### 2.Execução do Projeto:

**Clone:**

```bash
git clone https://github.com/ViniciusOtoni/Dags-Airflow.git
```

**Subir serviços**
```bash
docker-compose up --build
```

Acesse o Airflow na porta 8080 localmente.