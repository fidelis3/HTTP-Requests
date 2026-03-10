# HTTP Requests Practice (Python)

This repository contains small Python scripts that demonstrate:

- Basic HTTP `GET` requests with `requests`
- Downloading and saving text/image files from the web
- Working with public APIs
- Converting API JSON responses into Pandas DataFrames

## Project Files

- `http_demo.py`: Requests an IBM webpage and an image, prints response details, and saves `image.png`.
- `download.py`: Downloads a sample text file and saves it as `example1.txt`.
- `randomUserApi.py`: Uses the `randomuser` package to generate fake user data and prints a DataFrame.
- `fruityVyceApi.py`: Calls the Fruityvice API (archived URL), parses JSON, and prints DataFrames.

## Requirements

- Python 3.9+
- Packages:
	- `requests`
	- `pandas`
	- `Pillow`
	- `randomuser`
	- `ipython` (used for notebook-style display import in `http_demo.py`)

Install dependencies:

```bash
pip install requests pandas pillow randomuser ipython
```

## Run The Scripts

From the project folder:

```bash
python http_demo.py
python download.py
python randomUserApi.py
python fruityVyceApi.py
```

## What Each Script Does

### `http_demo.py`

- Sends a request to `https://www.ibm.com/`
- Sends a request for an image file
- Prints status code, partial HTML, request headers, and content type
- Writes the image response to `image.png`

Output artifacts:

- `image.png`

### `download.py`

- Downloads `Example1.txt` from IBM course storage
- Saves it into the current working directory as `example1.txt`

Output artifacts:

- `example1.txt`

### `randomUserApi.py`

- Generates 10 random users
- Prints names, emails, and image URLs
- Builds a Pandas DataFrame with user details (`Name`, `Gender`, `City`, `State`, `Email`, `DOB`, `Picture`)

### `fruityVyceApi.py`

- Fetches all fruits data from Fruityvice (via archived endpoint)
- Parses JSON response
- Prints:
	- Raw list-based DataFrame
	- Flattened DataFrame using `pd.json_normalize()`

