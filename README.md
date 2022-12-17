# memory-vault

An editable database of cheats used with older (10+ years) console games.

## Installation and Use

Memory-Vault is built using a basic Django/SQLite setup in its current form, as even at its largest theoretical extent the project is not expected to reach a size that would benefit from something like Postgres.

To use it locally:
- clone the repository
- install a virtualenv with `python -m venv venv` (or similar)
- activate your virtualenv
- install requirements with `pip install -r requirements.txt`
- start the server with `python manage.py runserver`

To use it remotely:
- (todo: docker instructions)

## History

Built specifically for a programming bootcamp portfolio project in December 2022, Memory-Vault's roots stretch back to around 2005 when I first started collecting data.  Over the years I built up an unwieldy collection of cheats in a variety of formats across multiple drives, some forgotten, some subject to mechanical failure; and the loss of progress as well as the sheer weight of material made it difficult to seriously consider doing anything else.

Learning how to properly leverage databases and tailor the input data to ensure a consistent output opened an amazing number of doors to potential project ideas, and this came to mind almost immediately.  It is a long overdue housekeeping effort and a revitalization of something I never imagined would see the light of day again.