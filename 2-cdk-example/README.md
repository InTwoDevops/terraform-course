# LocalStack S3 Example with Terraform and Go

## 1. Start LocalStack
```bash
docker compose up -d
```

## 2. Provision EC2 Instance
```bash
docker build . -t localstack-terraform-cdk
docker run --rm -it -v ./example.py:/app/main.py localstack-terraform-cdk
cdktf get && cdktf synth && cdktf deploy
```

