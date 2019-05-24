# Jira to Wunderlist Integration

A bi-directional syncing tool to copy and update tasks from Jira to Wunderlist.

## Requirements

-   Python3
-   Wunderlist
-   Jira

## Installation

Clone this repository.

## Setup

Create a `.env` file or set environment variables:

-   `JIRA_URL`
-   `JIRA_USERNAME`
-   `JIRA_API_KEY`
- TODO: KEYS FOR WUNDERLIST DESCRIPTION

## Installation

clone the repository and run:

```Shell
pip3 install .
```

## Running the Script

Run the script by executing:

```Shell
python3 sync.py <Wunderlist-ListName>
```

or

```Shell
python3 -m jira_to_wunderlist.sync <Wunderlist-ListName>
```

## Future Improvements

-   [x] Turn this into a package with an entry_point for use anywhere.
-   [ ] Enable bi-directional syncing
-   [ ] Better Error-trapping for missing environment variables
