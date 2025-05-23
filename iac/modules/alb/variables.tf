variable "public_subnet_ids" {
    type = list()
    default = []
}

variable "alb_sg_id" {
    type = string 
    default = ""
}

variable "vpc_id" {
    type = string
    default = ""
}
