from minio import Minio


import minio
minioClient  = Minio('10.22.7.227:9000', 
				access_key='123456', 
				secret_key='12345678', 
				secure='True')

try:
    minioClient.make_bucket("mybucket", location="us-east-1")
except ResponseError as err:
    print(err)
# for bucket in minio.list_buckets():
# 	print(bucket.name)
#  Minio('play.minio.io:9000',
#                   access_key='Q3AM3UQ867SPQQA43P2F',
#                   secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
#                   secure=True)