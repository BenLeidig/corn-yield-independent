# Changelog

----------------------------------------------------------------------------------------------------------------------

## [YYYY-MM-DD] - Contributor Name
### Commit Message (lower case)
- **Description:** A brief explanation of the change.
- **Additional Information:** More detailed information, if necessary (e.g., reasons for the change, affected files, methods, or NA).

----------------------------------------------------------------------------------------------------------------------

## [2025-01-02] - Benjamin Leidig
### acquired yield data
- **Description:** Created `CHANGELOG.md`, `acquisition.ipynb`, `api_key.txt`, `yield_raw.csv`, and `.gitignore` as well as the necessary code to programmatically acquire yield data using the USDA NASS API.
- **Additional Information:** `api_key.txt` was added to the changelog for security and legal purposes.

## [2025-01-02] - Benjamin Leidig
### acquired price received data
- **Description:** Added code to programmatically acquire price received data using the USDA NASS API in `acquisition.ipynb`.
- **Additional Information:** Fixed a line of code in the cell that saves `yield_raw.csv` to use less computer storage. Also added `data/raw` to the gitignore.

## [2025-01-04] - Benjamin Leidig
### acquired weather data
- **Description:** Added code to programmatically acquire weather data using CSV web links in `acquisition.ipynb`.
- **Additional Information:** Also, fixed an error when fetching the price received data via the USDA NASS API.

## [2025-01-04] - Benjamin Leidig
### code comments to `acquisition.ipynb`
- **Description:** Added code comments to `acquisition.ipynb`.
- **Additional Information:** NA.

## [2025-01-04] - Benjamin Leidig
### created `acquisition.py`
- **Description:** Moved `acquisition.ipynb` to `doc/notebooks` and created `acquisition.py`, which contains only code.
- **Additional Information:** Added loading signals to ensure user confidence in program processing.

## [2025-01-08] - Benjamin Leidig
### created `integration.ipynb`
- **Description:** Added code to programmatically integrated data from each raw data source.
- **Additional Information:** NA.

## [2025-01-08] - Benjamin Leidig
### created `integration.py`
- **Description:** Created python file for `integration.ipynb`.
- **Additional Information:** Fixed date of previous push. Added code comments in `integration.ipynb` and the exportation of the integrated dataset into `data/raw`.

## [2025-01-14] - Benjamin Leidig
### fixed bug in `acquisition.py`
- **Description:** Used a different algorithm to fetch all historical weather in `acquisition.py` to patch a bug that made all of `state_name` `ILLINOIS`.
- **Additional Information:** Added some other work (`cleaning.ipynb`) that will elaborate upon in a future push.

## [2025-01-15] - Benjamin Leidig
### cleaned dataset
- **Description:** Created `cleaning.ipynb` and `cleaning.py` that explore dataset nullity and clean the data of interest. Timeframe was readjusted and code comments will be added later.
- **Additional Information:** Saved cleaning visualizations to `results/cleaning`.

## [2025-01-15] - Benjamin Leidig
### code comments to `cleaning.ipynb`
- **Description:** Added code comments to `cleaning.ipynb`.
- **Additional Information:** Shortened and improved some code in `cleaning.ipynb` and `cleaning.py`. Also, fixed the date of the previous change description in the `CHANGELOG.md`.