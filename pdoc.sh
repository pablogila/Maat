# This script is used to update Maat documentation automatically.
# Requires pdoc, install it with `pip install pdoc`.
# Run this script as `source pdoc.sh`.

# Extract the version number from constants.py
version="$(grep -oP 'version\s*=\s*\K.*' ./maat/constants.py | tr -d "'")"
# Update README.md header with the version number
sed -i "s/^# Maat.*/# Maat $version/" README.md
# Generate the documentation
pdoc ./maat/ -o ./docs --mermaid --math --footer-text="Maat $version documentation"
