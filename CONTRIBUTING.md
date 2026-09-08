# Updating the project

Preserve source baselines. Put geometry or simulation changes in a new revision directory, with the reason and expected effect. Edit chapter files and rerun `python tools/build_manual.py` to refresh the combined manual. For calculation changes, edit the appropriate assumptions, rerun `python tools/calculate.py`, `python tools/verify.py` and `python -m unittest discover -s tests -v`.

Never commit credentials or machine-specific working outputs. Record actual supplier data, test instruments and conditions. Do not relabel simulated results as measurements. State current normalization with every force/current result. Include enough input data for another person to reproduce the conclusion.
