# Changelog
All notable changes to this project will be documented in this file.<br />
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.2.2 - 2019-4-25
### Fixed
- PyPI not installing packages with the right name using when using `pip`
## 0.2.1 - 2019-4-25
### Fixed
- Metadata not being packaged with PyPI
## 0.2.0 - 2019-4-25
### Added
- Two demos to demonstrate basic usage
- A changelog file
- A `setup.cfg` and a `setup.py`
### Changed
- The start and end dates of Era instances are now `datetime.datetime` 
rather than `datetime.date` for consistency
- A Wareki instance with no arguments given when created, defaults 
to the current time (i.e. `datetime.now()`
- `str()` of a Wareki instance now provides a long date using the 
Japanese calendar rather than just the string representation of a 
normal datetime object
## 0.1.0 - 2019-4-19
Initial version