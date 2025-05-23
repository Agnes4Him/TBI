variable instance_type {
  type        = string
  default     = ""
}

variable ec2_sg_id {
  type        = string
  default     = ""
}

variable private_subnet_ids {
  type        = list()
  default     = []
}

variable target_group_arn {
  type        = string
  default     = ""
}



