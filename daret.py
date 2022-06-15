from asyncio.log import logger
import pexpect, getpass

from commands import get_postgres_command
from args import DaretArgs
from errors import clear_errors
from schemas import DaretSchema

DB_PASSWORD_MSG = "Database User Password:"

class Daret:
    def __init__(self):
        self.dump_files = None
        self.args = DaretArgs().get_args()
        clear_errors(self) 

    def prepare(self):
        try:
            if self.args.schema is None:
                if DaretSchema.no_schema_directory_present(self.args.dumpdir):
                    self.dump_files = DaretSchema.dump_files(self.args.dumpdir, None)
                else:
                    for schema in DaretSchema.list(self.args.dumpdir):
                        self.dump_files += DaretSchema.dump_files(self.args.dumpdir, schema)
            else:
                self.dump_files = DaretSchema.dump_files(self.args.dumpdir, self.args.schema)
        except FileNotFoundError as e:
            logger.error(e)
        

    def command(self, userPassword):
        dbuser, dbname = self.args.dbuser, self.args.dbname
        if self.dump_files is None:
            raise Exception("Dump files could not be loaded.")

        for dump_file_path in self.dump_files:
            cmd = get_postgres_command(dbuser, dbname, dump_file_path)
            child = pexpect.spawn(cmd)
            child.expect('Password for user {}:'.format(dbuser))
            child.sendline(userPassword)

            print(child.before.decode())
            child.interact()
        print('Completed')


if __name__ == '__main__':
    daret = Daret()
    userPassword = getpass.getpass(DB_PASSWORD_MSG)
    daret.prepare()
    daret.command(userPassword)