# Amazon ECR (Elastic Container Registry) Repository Terraform Module

This module is responsible for creating an ECR repository in AWS in compliance with company standards.

## What does this module do?
----------------------------
This module creates the following resources in the targeted AWS account:
- Amazon ECR repository
- Amazon ECR lifecycle repository policy

## Module Variables
-------------------
### Required Variables
**namespace**
- name or abbreviation of the organization (should be set to "loupe")

**stage**
- the environment that the IAM role will be deployed in
- *type*: string

**environment**
- the AWS region that the module will be deployed in
- *type*: string

**app_name**
- the name of the application the resource will be part of
- *type*: string

**loupe_tags**
- a map of additional tags to assign to resources
- *type*: object({ Team = string })

### Optional Variables
**image_tag_immutability**
- the tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`
- *type*: string
- *default*: `IMMUTABLE`

## Module Outputs
-------------------
**repository_arn**
- The full ARN of the created ECR repository.

**repository_url**
- The URL of the created ECR repository.

**registry_id**
- The ID of the created ECR registry.

## Module Usage
---------------
```
module "loupe_ecr_repository" {
    source  = "spacelift.io/loupetheapp/terraform-aws-ecr-repository/aws"
    version = "3.0.0"

    namespace        = "loupe"
    stage            = "dev"
    environment      = "use1"
    app_name         = "admin-tool"

    image_tag_mutability    = "MUTABLE"

    loupe_tags = {
      Team = "Backend"
    }
  }
```
