# Merge intervals

A demo project which takes a space-separated list of possibly overlapping intervals and transforms it into a list of non-overlapping intervals.

* **Example input:** `1,3 5,6 3,9 13,20`
* **Example output:** `1,9 13,20`

## Usage

The main program is called `merge.py` and is simply fed with a list of intervals as arguments.
Each interval consists of a start and end value, separated via comma `,`.

```bash
$ python merge.py -h
usage: merge.py [-h] interval [interval ...]

Merge probably overlapping intervals into non-overlapping intervals.

positional arguments:
  interval    list of intervals to merge (example: 1,3 3,9)

optional arguments:
  -h, --help  show this help message and exit
```
