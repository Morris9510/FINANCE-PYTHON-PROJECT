# Stock Prediction Project For WallStreetBets Gamblers

## Overview

This project focuses on fetching and analyzing stock market data, with an emphasis on the historical stock prices of a specific company (e.g., NVIDIA Corporation - NVDA). The project utilizes Python, leveraging libraries like `yfinance` for data retrieval, `pandas` for data manipulation, and `matplotlib` for data visualization.

## Installation

### Prerequisites

- Python 3.x
- pip
- Django
- virtualenv (optional, but recommended)

### Setting Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
Installing Dependencies
bash
Copy code
# Install the required Python packages
pip install -r requirements.txt
Usage
To run the project, execute the main script after activating the virtual environment:

bash
Copy code
python main.py
This script will fetch historical stock data and perform basic data analysis, visualizing the stock's closing prices over time.

Saving Data to CSV
To save the fetched data to a CSV file,change the relevant line in main.py to true. This will generate a file named stock_data.csv in the project directory.

Contact
For any queries or suggestions, feel free to contact morris9510@gmail.com

Acknowledgments
Special thanks to the yfinance library for providing an easy way to access Yahoo Finance data.
This project was inspired by the need for accessible financial data analysis tools for retail investors.
```
