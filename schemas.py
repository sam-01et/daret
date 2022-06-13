import os, stat
class DaretSchema:
    def __init__(self) -> None:
        pass

    @classmethod
    def list(self, dbfolder):
        def unwanted(p):
            return p.startswith(".") or os.path.isfile(os.path.join(dbfolder, p))
        return [schema for schema in os.listdir(dbfolder) if not unwanted(schema)]

    @classmethod
    def dump_files(self, dbfolder, schema):
        path = os.path.join(dbfolder, schema)

        if not os.path.exists(path):
            raise FileNotFoundError("Given schema name does not exist")

        filepaths = [os.path.join(path, schema_file) for schema_file in os.listdir(path)]
        filepaths = list(filter(lambda x: (x.endswith(".sql")), filepaths)) 
        file_statuses = [(os.stat(filepath), filepath) for filepath in filepaths] 
        files = ((status[stat.ST_MTIME], filepath) for status, filepath in file_statuses if stat.S_ISREG(status[stat.ST_MODE]))
        return [f for t, f in sorted(files)]