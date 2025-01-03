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