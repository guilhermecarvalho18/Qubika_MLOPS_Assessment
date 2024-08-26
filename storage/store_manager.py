import os

class StorageManager:
    def __init__(self):
        self.provider = os.getenv('STORAGE_PROVIDER', 'local')
        self.bucket_name = os.getenv('BUCKET_NAME', 'my-bucket')

    def upload_file(self, file_path, destination_path):
        if self.provider == 'aws':
            self._upload_to_s3(file_path, destination_path)
        elif self.provider == 'gcp':
            self._upload_to_gcs(file_path, destination_path)
        else:
            self._upload_to_local(file_path, destination_path)

    def _upload_to_s3(self, file_path, destination_path):
        import boto3
        s3 = boto3.client('s3')
        s3.upload_file(file_path, self.bucket_name, destination_path)

    def _upload_to_gcs(self, file_path, destination_path):
        from google.cloud import storage
        client = storage.Client()
        bucket = client.bucket(self.bucket_name)
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(file_path)

    def _upload_to_local(self, file_path, destination_path):
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        os.rename(file_path, destination_path)
