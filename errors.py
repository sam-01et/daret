def clear_errors(o):
    if o.args.dumpdir is None:
        raise RuntimeError("You must specify argument which points to the folder where your database dump files are") 
    if o.args.dbuser is None:
        raise RuntimeError("You must specify dbuser argument")  
    if o.args.dbname is None:
        raise RuntimeError("You must specify the name of the database")