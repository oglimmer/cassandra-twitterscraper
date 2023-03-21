
# setup

* start `docker compose up --build -d`
* wait until all comomponents are up. Check via `docker compose logs -f` - this might take several minutes.

# init

* use `SEARCH_TERMS="tesla,elon-musk" INIT=false docker compose up --build taskgen` to create the search terms for tesla and elon-musk

# start the scraper

* use `docker compose up --build -d scraper`

# UI

Go to http://localhost/
