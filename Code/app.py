#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

from glue_pipeline.glue_pipeline_stack import GluePipelineStack
from lambda_pipeline.lambda_pipeline_stack import LambdaPipelineStack
from data_deployment.data_deployment_stack import DataDeploymentstack
from glue_database.glue_database_stack import GlueDatabaseStack


# Define environment
env_USA = Environment(account="<Account-id>", region="ap-south-1")

# Define deployment order with correct environment and consistent naming
lambda_stack       = LambdaPipelineStack(app, "LambdaPipelineStack", env=env_USA)
glue_db_stack      = GlueDatabaseStack(app, "GlueDatabaseStack", env=env_USA)
glue_pipeline_stack = GluePipelineStack(app, "GluePipelineStack", env=env_USA)
data_deploy_stack  = DataDeploymentStack(app, "DataDeploymentStack", env=env_USA)

# Stack dependencies to ensure proper execution order
glue_db_stack.add_dependency(lambda_stack)
glue_pipeline_stack.add_dependency(glue_db_stack)
data_deploy_stack.add_dependency(glue_pipeline_stack)

# Add project tags for all resources
Tags.of(app).add("ProjectOwner", "Data Engineer")
Tags.of(app).add("Project", "Big-Data-Pipeline")
