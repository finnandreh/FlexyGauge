
# FlexiGauge

**FlexiGauge** is a Python script for generating customizable polar gauges, allowing you to adjust various parameters to fit your data visualization needs.

## Features

- Customizable angles, increments, and labels
- Flexible styling options for fonts and colors
- Option to reverse label order

## Installation

Ensure you have Python and Matplotlib installed:

```bash
pip install matplotlib
```

## Usage

Use the `create_gauge` function with your desired parameters to create a gauge:

```python
from flexigauge import create_gauge

create_gauge(
    start_angle=270,    # Start of the gauge at 270 degrees
    end_angle=450,      # End of the gauge at 450 degrees (180-degree span)
    step_size=5,        # Label increment, e.g., 0, 5, 10, ..., 40
    min_value=0,        # Minimum value on the gauge
    max_value=40,       # Maximum value on the gauge
    reverse_labels=False, # Order of labels
    output_file='gauge.png', # Output file name
    font_size=12,       # Font size for labels
    font_weight='normal', # Font weight
    font_color='blue',  # Font color
    circle_linewidth=3, # Circle line width
    circle_color='red', # Circle color
    label_suffix=' units' # Suffix for each label
)
```

### Parameters

- **`start_angle`**: Starting angle of the gauge in degrees.
- **`end_angle`**: Ending angle of the gauge in degrees.
- **`step_size`**: Increment between each tick label.
- **`min_value`**: Minimum value to be displayed on the gauge.
- **`max_value`**: Maximum value to be displayed on the gauge.
- **`reverse_labels`**: Reverse order of labels if `True`.
- **`output_file`**: Path to save the gauge image.
- **`font_size`**: Size of the tick label font.
- **`font_weight`**: Weight of the tick label font.
- **`font_color`**: Color of the tick labels.
- **`circle_linewidth`**: Line width of the outer circle.
- **`circle_color`**: Color of the outer circle.
- **`label_suffix`**: Suffix appended to each label.

## Example

Here's an example of generating a customized gauge with values from 0 to 40:

```python
create_gauge(
    start_angle=270, 
    end_angle=450, 
    step_size=10, 
    min_value=0,
    max_value=40,
    reverse_labels=False, 
    output_file='custom_gauge.png',
    font_size=14, 
    font_weight='bold', 
    font_color='green', 
    circle_linewidth=4, 
    circle_color='black',
    label_suffix=' %'
)
```

## License

This project is licensed under the MIT License.
