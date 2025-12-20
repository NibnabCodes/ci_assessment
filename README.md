# Computer Infrastructure Assignment - Winter 2025  

[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Serif+Display&size=36&pause=1000&color=2DF71F&width=435&lines=Yfinance+Assessment)](https://git.io/typing-svg)

![Alt text](images/stock_market.png) 

## Overview 📈  

This repository contains my submission for the *Computer Infrastructure assessment*. The project is structured as a Jupyter Notebook that works through a series of practical problems designed to demonstrate understanding of core computer infrastructure concepts using Python.  

This project automates the collection and visualisation of recent stock market data for the five FAANG companies: Meta (Facebook), Apple, Amazon, Netflix, and Google. Using the yfinance Python package, the project downloads hourly stock price data for the previous five days and saves it locally in a structured format.

The repository contains functions to retrieve and store the data, generate a combined plot of closing prices for all five stocks, and run the full workflow from a single executable Python script. In addition, the project includes a GitHub Actions workflow that automatically runs the script every Saturday morning. 

All functionality is documented and demonstrated in a Jupyter Notebook, which explains the implementation of each step, including data collection, plotting, scripting, and automation.

## Key Features ✨

- Automated data collection using a public financial API

- Timestamped data storage for reproducibility

- Combined visualisation of multiple stocks

- Executable Python script

- Fully automated weekly updates via GitHub Actions

- Clear documentation and explanation of every step

## Repository Structure 📂  

├── data/                 # Automatically generated CSV files
├── plots/                # Automatically generated PNG plots
├── images/               # Images used in README
├── faang.py              # Executable Python script
├── requirements.txt      # Python dependencies
├── .github/workflows/    # GitHub Actions workflow
├── notebook.ipynb        # Main Jupyter Notebook
└── README.md             # Project documentation

- The data/ folder stores timestamped CSV files containing hourly FAANG stock data.

- The plots/ folder stores timestamped PNG files of closing price plots.

- The faang.py script allows the full workflow to be executed from the command line.

- The GitHub Actions workflow automates execution and version control updates.

## Technologies 🛠️ 

This project uses the following tools and technologies:

- Python 3 – Core programming language

- Jupyter Notebook – Interactive documentation and analysis

- yfinance – Downloading historical stock data

- pandas – Data manipulation and storage

- matplotlib – Data visualisation

- Git & GitHub – Version control

- GitHub Actions – Workflow automation

- Linux shell commands – File permissions and execution

All dependencies are listed in requirements.txt.

**See tasks.ipynb for further information on the libraries**

## How to Setup Environment ⚙️  

To download and run this repository locally, ensure the following tools are installed on your system.

1. **Git**

Git is required to clone the repository and manage version control.

Download the latest version of Git from:
https://git-scm.com/downloads

Follow the installer instructions for your operating system.

2. **GitHub Account**

A GitHub account is required to access and clone the repository.

Create a free GitHub account at:
https://github.com/signup

3. **Anaconda (Recommended)**

Anaconda is recommended because it includes Python, Jupyter Notebook, and most of the libraries used in this project.

Installation steps:

1. Download Anaconda from:
https://www.anaconda.com/download

2. Run the installer and click Next through the setup screens.

3. When prompted with Advanced Options, ensure the following are selected:

- ✅ Add Anaconda to the PATH environment variable

- ✅ Make this version your default Python

## How to Download Repository 📥  

To download the repository, follow these steps:

1. Open a terminal or command prompt

2. Navigate to the directory where you want to store the project

3. Clone the repository using Git:

git clone https://github.com/NibnabCodes/ci_assessment.git

4. Move into the project directory:

*cd ci_assessment*

## How to Run the Project ▶️

There are two ways to run this project.  

**Option 1: Run the Jupyter Notebook**  

This option allows you to view explanations and outputs together.

1. Launch Jupyter Notebook:  

*jupyter notebook*

2. Open the project notebook file  

3. Run all cells in order  

This will:

- Download FAANG stock data

- Save a timestamped CSV file to the data/ folder

- Generate and save a plot to the plots/ folder  

**Option 2: Run the Executable Script**

The entire workflow can also be executed from the command line using the faang.py script.

Ensure the script is executable:  

*chmod +x faang.py*

Run the script:

*./faang.py*  

This will:

- Download hourly FAANG stock data for the past five days

- Save the data as a CSV file

- Generate and save a closing price plot  

**Automated Execution (GitHub Actions)**

The project also runs automatically using GitHub Actions.

- The workflow executes every Saturday morning (UTC)

- It runs faang.py

- New data and plots are committed and pushed automatically

No manual action is required for automation.

## References 📖

Please see <u>problems.ipynb</u> for references used.