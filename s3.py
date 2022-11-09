import boto3

# This reusable function creates an S3 bucket
def CreateBucket(name):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=name)
    return True

# This reusable function deletes an S3 bucket
def DeleteBucket(name):
    s3_client = boto3.client('s3')
    s3_client.delete_bucket(Bucket=name)
    return True

# This is the 'enforcing encryption' function
def EnforceS3Encryption(name):
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    bucket = s3.Bucket(name)
    print(f"Encrypting {bucket.name}")
    response = s3_client.put_bucket_encryption(
        Bucket=bucket.name,
        ServerSideEncryptionConfiguration={
            'Rules': [
        {
          'ApplyServerSideEncryptionByDefault': {
            'SSEAlgorithm': 'AES256'
          }
        }
      ]
    }
  )
    print(response)

# this will tie up all the 3 functions together
if __name__ == "__main__":
  Name = '98989test-bucket-for-encyrption' #unique bucket name
  CreateBucket(Name)
  EnforceS3Encryption(Name)
  # DeleteBucket(Name)
