# MobilePhoneChoiceAssistant
System, which supports choosing mobile phone adjusted to user's needs.

## Requirements

```bash
pipenv install
```

## Usage

Run the following in virtualenv:
```bash
python -m assistant
```

To enable virtualenv run:
```bash
pipenv shell
```
or
```bash
pipenv run COMMAND
```

## Updating knowledge base

To generate [the `knowledge_base.pl`](prolog_assistant/knowledge_base.pl) file
translate a csv file with the following columns:

```
model
memory
display_diagonal
display_width
display_height
display_number_of_colors
storage
touch_screen
NFC
water_resistant
dual_sim
battery_capacity
android_version
cpu_frequency
cpu_n_cores
gps
agps
glonass
galileo
quick_charge
has_jack
usb_c
sim_types
back_camera_matrix
front_camera_matrix
price
```

using the `translator` module from within a python virtualenv:

```bash
python -m assistant translate input.csv > prolog_assistant/knowledge_base.pl
```

The values in input file should be:
 - `NA` if not available or not applicable
 - list of values: `[13.0, 5.0]` if there are multiple valid values
 - `1` for _true_, `0` for _false_
 - int or float where applicable (e.g. `5`, `5.1`)
 - `"`-escaped, `,`-separated `sim`, `micro`, `nano` values for `sim_types` column
 - in `mAh` for `battery_capacity`
 - in `MB` for `memory` and `storage`
 - in inches for `display_diagonal`
 - in `px` for `display_width` and `display_height`
 - in `Mpx` for `back_camera_matrix` and `front_camera_matrix`
