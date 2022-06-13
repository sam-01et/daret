import argparse

class DaretArgs:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='Auto Restoration of database backups')
        parser.add_argument('--dbuser', help='Name of the user with access to the database')
        parser.add_argument('--dumpdir', help='Name of the database folder')
        parser.add_argument('--schema', help='Name of the schema for which to perform the recovery. If not specified, it does for all the schemas')
        parser.add_argument('--dbname', help='Name of the database for which to do the recovery')
        self.args = parser.parse_args()
    
    def get_args(self):
        return self.args