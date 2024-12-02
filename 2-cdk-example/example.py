from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance

class MyTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Set up the AWS provider
        AwsProvider(self, "AWS",
            access_key="test",
            secret_key="test",
            region="us-east-1",
            endpoints=[
                {
                    "s3": "http://host.docker.internal:4566",
                    "sts": "http://host.docker.internal:4566",
                }
            ]
        )

        # Define the EC2 instance
        Instance(self, "ExampleInstance",
            ami="ami-0c55b159cbfafe1f0",
            instance_type="t2.micro",
            tags={"Name": "TerraformExample"}
        )


app = App()
MyTerraformStack(app, "my-terraform-stack")
app.synth()

