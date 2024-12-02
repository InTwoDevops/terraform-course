# LocalStack S3 Example with Terraform and Go

## 1. Start LocalStack
```bash
docker compose up -d
```

## 2. Provision EC2 Instance
```bash
docker build . -t localstack-terraform
docker run --rm -v ./:/app localstack-terraform tflocal init
docker run --net=host --rm -v ./:/app localstack-terraform tflocal plan
docker run --net=host --rm -v ./:/app localstack-terraform tflocal apply
```

