terraform {
  required_version = ">= 1.2.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}

provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-082b1f4237bd816a1"
  instance_type = "t2.micro"
  tags = {
    Name = "EC2WithTerraform"
  }
}