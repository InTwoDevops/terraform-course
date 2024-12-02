# LocalStack S3 Example with Terraform and Go

## 1. Start LocalStack
```bash
docker compose up -d
```

## 2. Provision EC2 Instance
```bash
docker build . -t localstack-terraform
docker run --rm -v ./:/app localstack-terraform tflocal init
# Create all resources
docker run --net=host --rm -it -v ./:/app localstack-terraform tflocal apply
# List resources from the state
docker run --rm -v ./:/app localstack-terraform tflocal state list
# Show database resource from the state
docker run --rm -v ./:/app localstack-terraform tflocal state show aws_instance.database
# CHECK THE ID OF THE INSTANCE 
# something like: id: i-2fb098f21fc9d39d9
# We want to move terrafrom code of the database to anoter subfolder or project
# if we remove it and we try to plan it will be deleted
# but if we ..
# Remove database from state
docker run --rm -v ./:/app localstack-terraform tflocal state rm "aws_instance.database"
# Now we want to impot a existing resource wihtout having to create from scratch
# and track it with terraform
docker run --net=host --rm -v ./:/app localstack-terraform tflocal import "aws_instance.database" "i-2fb098f21fc9d39d9"

```

