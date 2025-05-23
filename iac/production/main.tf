module "networking" {
  source = "./modules/networking"
  vpc_cidr = var.vpc_cidr
}

module "security" {
  source               = "./modules/security"
  vpc_id               = module.networking.vpc_id
}

module "alb" {
  source            = "./modules/alb"
  vpc_id            = module.networking.vpc_id
  public_subnet_ids = module.networking.public_subnet_ids
  alb_sg_id         = module.security.alb_sg_id
}

module "compute" {
  source               = "./modules/compute"
  instance_type = var.instance_type
  vpc_id               = module.networking.vpc_id
  private_subnet_ids   = module.networking.private_subnet_ids
  ec2_sg_id            = module.security.ec2_sg_id
  target_group_arn     = module.alb.target_group_arn
}

module "ecr" {
  source = "./modules/ecr"
}