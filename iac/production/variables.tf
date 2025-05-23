variable region {
  type        = string
  default     = "us-east-1"
}


variable instance_type {
  type        = string
  default     = "t2-micro"
}

variable vpc_cidr {
  type        = string
  default     = "10.0.0.0/16"
}
