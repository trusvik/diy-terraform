
# Exercise: Terraform S3 Bucket Module
## Objective
Create a reusable Terraform module that provisions an AWS S3 bucket. You will then utilize this module in two separate Terraform configurations to create buckets for both testing and production environments.

## Step 1: Set Up Your Terraform Module
Create a new directory named s3_module. Inside this directory, create a file named main.tf. This file will define the S3 bucket resource. Remember not to hard-code the bucket name.
##Step 2: Create Two Instances of the Module
Create two new directories as "siblings" to the s3_module directory. Name these directories test and prod. In each directory, create a main.tf file where you use the module to create buckets for your production and test environments, respectively.
