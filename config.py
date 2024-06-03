import os
import json
import boto3
from botocore.exceptions import ClientError

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def get_secret():
        secret_name = "yousecret"
        region_name = "eu-west-3"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            raise e

        secret = get_secret_value_response['SecretString']
        secret_dict = json.loads(secret)
        db_username = secret_dict['username']
        db_password = secret_dict['password']
        db_host = "yourHostDb"
        db_name = "mydb"
        return db_username, db_password, db_host, db_name
        print(db_name)

    db_username, db_password, db_host, db_name = get_secret()
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_username}:{db_password}@{db_host}:5432/{db_name}"
