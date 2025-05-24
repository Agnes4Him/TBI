# TBI
The following steps were carried out in approaching the model serving app deployment task

## Architecture Design
Infrastructure as Code tool - Terraform is used to provision a set of Amazon EC2 instances to host the API.
The instances are placed behind an application load balancer, and hosted in private subnets for security.
They are also automatically scaled up or down by an autoscaling group, based on CPU utilization.

A launch template is used to deploy an inital Nginx Docker container as a placeholder within the instances.
This is to be replaced later by the GitHub Actions CI/CD pipeline.

## API
The API is built using Python flask, and within a virtual environment. The environment is activated using pipenv and packages installed as follows:

```bash
pip install pipenv --user
pipenv shell
pipenv install
```
An accompanying unit test is run on the API. To run the API test locally. simply do the below:

```bash
cd serving/api
pytest tests
```

To run the API locally:

```bash
python3 serving/api/model.py
```

Access the application on `http://localhost:4000`

## CI/CD Pipeline
This is used to provision infrastructures and deploy the API. 
This pipeline contains two componenents: A continuous integration and deployment.

The continuous integration validates the Terraform configurations, while the deployment pipeline runs testing on the API,
builds the API Docker image, and push the image to AWS ECR. The Docker image in Terraform configurations is then updated to the relevant image.
The pipeline then runs the Terraform configurations to apply the Terraform configurations and provision all the needed infrastructures such a s networking, instances, load balancer etc.

## Monitoring
Since the API is deployed in EC2 instances that are running behind an Application Loadbalancer in AWS, there's automatically provision for detailed HTTP metrics which include:
** RequestCount - Number of requests
** HTTPCode_Target_4XX_Count - Client-side error
** HTTPCode_Target_5XX_Count - Server-side errors
** TargetResponseTime - Response time

These can be accessed at `CloudWatch > Metrics > ALB > Per Target Group or Per Load Balancer`

A dashboard is then created from this as needed, and alarms can be integrated with this for prompt notifications through Simple Notification Service (SNS).