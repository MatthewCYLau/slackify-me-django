resource "google_sql_database_instance" "main" {
  name             = "main-postgresql-instance"
  database_version = "POSTGRES_13"
  region           = "europe-west2"
  deletion_protection = false

  settings {
    tier = "db-f1-micro"
  }
}