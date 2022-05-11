# Fetch a database index

url = "https://cache.e4s.io/build_cache/index.json"

all: run

db:
	mkdir db

db/index.json: db
	curl -L $(url) -o db/index.json

download: db/index.json

run: db/index.json
	./read-spack-db.py

clean:
	rm -rf db
