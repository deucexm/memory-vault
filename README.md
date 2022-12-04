# memory-vault

An editable database of cheats used with older (10+ years) console games.

## Installation and Use

Memory-Vault is built using Docker.  It doesn't connect externally yet (or have any of the relevant data), so the process is simple:

- install Docker if needed
- clone repo to desired location and `cd` your way in
- `docker-compose up -d --build`

The interface should then be available at http://localhost:8000.

## History

Built specifically for a programming bootcamp portfolio project in December 2022, Memory-Vault's roots stretch back to around 2005 when I first started collecting data.  Over the years I built up an unwieldy collection of cheats in a variety of formats across multiple drives, some forgotten, some subject to mechanical failure; and the loss of progress as well as the sheer weight of material made it difficult to seriously consider doing anything else.

Learning how to properly leverage databases and tailor the input data to ensure a consistent output opened an amazing number of doors to potential project ideas, and this came to mind almost immediately.  It is a long overdue housekeeping effort and a revitalization of something I never imagined would see the light of day again.