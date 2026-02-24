## Wifaq Ul Madaris Result Automation

Every year when the result is announced the wifaq site gets so much traffic that it doesn't respond but with errors until the traffic is reduced.

This rough script automates the searching of the result per roll number, just to make it easy to get the result via cli.

https://www.wifaqulmadaris.org/Results/Infradi

### How to use

#### Tools

`Python 3`

`NodeJS v24 or above`

#### Execution

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt` 

- Modify the following variables:
  - roll_no
  - level (darja)
  - year (hijri)

- run the following command:
  - `python3 get_result.py`

- run the following command to open the result in browser:
  - `npm install -g open-cli`
  - `open-cli result_18037`

- take snapshot or save as PDF.

### TODOs
- Combine them all into one command
