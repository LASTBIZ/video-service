from google.cloud import storage


class StorageStream():
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket("lastmbiz-storage")

    def download_video(self, path):
        blob = self.bucket.blob(f"images/{path}")

        name = blob.name.split("/")[1]
        blob.download_to_filename(f"../files/{name}")
