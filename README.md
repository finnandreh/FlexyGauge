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

Use the `create_gauge` function with your desired parameters:

```python
from flexigauge import create_gauge

create_gauge(
    start_angle=270, 
    end_angle=450, 
    step_size=5, 
    reverse_labels=True, 
    output_file='gauge.png',
    font_size=12, 
    font_weight='normal', 
    font_color='blue', 
    circle_linewidth=3, 
    circle_color='red',
    label_suffix=' units'
)
```

### Parameters

- **`start_angle`**: Starting angle of the gauge in degrees.
- **`end_angle`**: Ending angle of the gauge in degrees.
- **`step_size`**: Increment between each tick label.
- **`reverse_labels`**: Reverse order of labels if `True`.
- **`output_file`**: Path to save the gauge image.
- **`font_size`**: Size of the tick label font.
- **`font_weight`**: Weight of the tick label font.
- **`font_color`**: Color of the tick labels.
- **`circle_linewidth`**: Line width of the outer circle.
- **`circle_color`**: Color of the outer circle.
- **`label_suffix`**: Suffix appended to each label.

## Example

Here's an example of generating a customized gauge:

```python
create_gauge(
    start_angle=270, 
    end_angle=450, 
    step_size=10, 
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
