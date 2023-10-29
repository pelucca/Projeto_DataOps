import os
from dotenv import load_dotenv

load_dotenv()   #função que chama as variaveis do ambiente do sistema operacional do .env

#caminhos de configurações das variáveis do ambiente de trabalho
configs_work = {
    'people':{
        "endpoint": os.environ.get('people_endpoint'),
        "raw_path": os.environ.get('people_raw_path'),
        "meta_path": os.environ.get('people_meta_path'),
        "path_work": os.environ.get('people_path_work')
    },    
    'planets':{
        "endpoint": os.environ.get('planets_endpoint'),
        "raw_path": os.environ.get('planets_raw_path'),
        "meta_path": os.environ.get('planets_meta_path'),
        "path_work": os.environ.get('planets_path_work')
    }, 
    'films':{
        "endpoint": os.environ.get('films_endpoint'),
        "raw_path": os.environ.get('films_raw_path'),
        "meta_path": os.environ.get('films_meta_path'),
        "path_work": os.environ.get('films_path_work')
    }
}

# caminho de config do data warehouse para gravação do csv
configs_dw = {
        "meta_path": os.environ.get('dw_meta_path'),
        "dw_path": os.environ.get('dw_path')
}

# caminhos dos logs de erros (se houver)
logs_file = os.environ.get('logs_file')
id_file = os.environ.get('id_file')