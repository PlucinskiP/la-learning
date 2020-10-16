terraform {
  required_version = ">=0.13.3"
  backend "s3" {
    region  = "us-east-1"
    profile = "default"
    key     = "terraformstatefile"
    bucket  = "tf-state-bucket-pp"
  }
}

# 6 line key just name for a file, can be anything
