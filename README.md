# TBI
The following steps were carried out in approaching this model deployment task

## Architecture Design
Infrastructure as Code tool - Terraform is used to provision a set of Amazon EC2 instances to host the API.
The instances are placed behind an application load balancer, and hosted in private subnets for security.
They are also automatically scaled up or down by an autoscaling group, based on CPU utilization.

A launch template is used to deploy an inital Nginx Docker container as a placeholder within the instances.
This is to be replaced later by the GitHub Actions CI/CD pipeline.

## API
The API is built using Python flask, and within a virtual environment. The environment is activated using and packages installed using:

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

Run the API locally using:

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