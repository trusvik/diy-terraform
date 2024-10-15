module "website" {
   source = "https://github.com/trusvik/diy-terraform"
   bucket_name = var.bucket_name
}