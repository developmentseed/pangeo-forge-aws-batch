from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_batch as batch
from aws_cdk import core

class PangeoForgeBatchStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC for the Batch environment (or use an existing VPC)
        vpc = ec2.Vpc(self, "VPC")

        # Create an ECS cluster
        cluster = ecs.Cluster(self, "PangeoForgeBatchCluster",
                              vpc=vpc,
                              container_insights=True)  # Enable CloudWatch Container Insights

        # Define a Batch compute environment
        compute_env = batch.ComputeEnvironment(self, "ComputeEnv",
                                               compute_resources=batch.ComputeResources(
                                                   vpc=vpc,
                                                   # other configurations as needed
                                               ),
                                               service_role=f"arn:aws:iam::{self.account}:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch")

        # Define a job queue
        job_queue = batch.JobQueue(self, "JobQueue",
                                   compute_environments=[{
                                       "computeEnvironment": compute_env,
                                       "order": 1,
                                   }])
