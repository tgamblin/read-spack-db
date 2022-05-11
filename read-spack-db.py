#!/usr/bin/env spack-python

import os.path
import sys

from spack.database import Database

db_root = os.path.join(os.path.dirname(sys.argv[0]), "db")
index = os.path.join(db_root, "index.json")

# yeah this is awkward
db = Database(None, db_root)

with db.read_transaction():
    # this'll take a long time
    adiaks = db.query("adiak", installed=False, in_buildcache=True)
    for spec in adiaks:
        print(spec.tree(color=True))
        print()
