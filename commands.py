def get_postgres_command(user, dbname, backup_file_path):
    return "psql -U {} -d {} -f {}".format(user, dbname, backup_file_path)