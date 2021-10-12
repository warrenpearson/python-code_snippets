import boto3


class S3ObjectRenamer:
    def rename(self, old_path):
        new_path = self.fix_path(old_path)
        print(f"{old_path} → {new_path}")

        s3_bucket = "insight-esg-classifiers"
        s3 = boto3.resource('s3')

        copy_source = {
            'Bucket': s3_bucket,
            'Key': old_path
        }
        s3.meta.client.copy(copy_source,
                            Bucket=s3_bucket,
                            Key=new_path)

        print(f"aws s3 ls \"{s3_bucket}/{old_path}\"")
        print(f"aws s3 ls \"{s3_bucket}/{new_path}\"")

    def fix_path(self, old_path):
        new_path = old_path.replace("|", "_")
        return new_path


if __name__ == "__main__":
    paths = [
        ""
    ]

    for path in paths:
        S3ObjectRenamer().rename(path)
