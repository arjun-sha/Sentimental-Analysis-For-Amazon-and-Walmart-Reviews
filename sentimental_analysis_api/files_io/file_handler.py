from minio import Minio
from sentimental_analysis_api import logger


class FileHandler:

    def __init__(self):
        pass

    @staticmethod
    def upload_file(filename, file):
        connection = Minio(
            '127.0.0.1:9000',
            access_key='admin',
            secret_key='admin@admin',
            secure=False
        )
        bucket_exists = connection.bucket_exists("filessentimentalanalysis")
        if not bucket_exists:
            connection.make_bucket("filessentimentalanalysis")
            logger.warning("Bucket created")
        else:
            logger.warning("Bucket already exists")

        upload = connection.fput_object('filessentimentalanalysis', filename, file.file.fileno())
        return {"upload_status": True, "id": upload.etag, "filename": filename}
