# daret 

daret is an acronym for Database Restore Tool.

What this tool seeks to achieve it to make it easy for restoring a database from huge number of backup files. Restoring each backup file, one at a time, is a challenge for many people and as such, daret wants to make it easy for performing such tasks so that you can be more focused on other things.

# Versions
The current version (1.0.0) works with restoring postgres databases.

## Requirements
daret is a commandline tool. To run effectively, the following commandline arguments are required;
<li> --dbuser. This is the name of the database user to use when restoring the database
<li> -- dumpdir. This is the path to the directory in which the dump files are. NOTE: If you have schema(s) inside the database directory (in cases of migration files), use the root directory of your database and NOT of a schema. 
<li> --schema. This is the name of the schema to use when performing the restoration. If none is given, daret will perform the restoration on ALL the schemas in the --dumpdir 
<li>--dbname. This is the name of the database for which you want daret to do the restoration.


## Run
To run daret, create a virtual environment and run 
<code>
    python daret --dbuser user --dumpdir dir --schema --schema --dbname db 
</code>


