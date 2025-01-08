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

## [2025-01-04] - Benjamin Leidig
### created `integration.ipynb`
- **Description:** Added code to programmatically integrated data from each raw data source.
- **Additional Information:** NA.