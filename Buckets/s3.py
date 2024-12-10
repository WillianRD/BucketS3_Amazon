import boto3
from botocore.exceptions import NoCredentialsError

# Defina suas credenciais AWS
aws_access_key_id = ''  # API KEY
aws_secret_access_key = ''  # APY KEY-SECRET
bucket_name = 'leide'  # NOME DO BUCKET
file_name = 'sa.png'  # NOME DO ARQUIVO
s3_file_name = 'sa.png'  # Nome do arquivo no S3

# Cria o cliente S3
s3_client = boto3.client('s3',

                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key)

# Função para fazer upload
def upload_to_s3(file_name, bucket, s3_file_name):
    try:
        s3_client.upload_file(file_name, bucket, s3_file_name)
        print(f"Upload do arquivo {file_name} realizado com sucesso para {bucket}/{s3_file_name}")

    except FileNotFoundError:
        print(f"O arquivo {file_name} não foi encontrado.")

    except NoCredentialsError:
        print("Credenciais não disponíveis.")


# Chamada da função de upload
upload_to_s3(file_name, bucket_name, s3_file_name)
