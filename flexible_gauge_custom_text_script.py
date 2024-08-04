
import matplotlib.pyplot as plt
import numpy as np

def create_gauge(start_angle=0, end_angle=180, step_size=5, reverse_labels=False, output_file='gauge.png',
                 font_size=10, font_weight='bold', font_color='black', circle_linewidth=2, circle_color='black',
                 label_suffix='°C'):
    """
    Create a gauge with customizable parameters.

    Parameters:
    - start_angle (int): The starting angle of the gauge in degrees.
    - end_angle (int): The ending angle of the gauge in degrees.
    - step_size (int): The increment in tick labels.
    - reverse_labels (bool): Whether to reverse the order of the labels.
    - output_file (str): The file path to save the generated gauge image.
    - font_size (int): Font size of the tick labels.
    - font_weight (str): Font weight of the tick labels (e.g., 'bold', 'normal').
    - font_color (str): Font color of the tick labels.
    - circle_linewidth (float): Line width of the outer circle.
    - circle_color (str): Color of the outer circle.
    - label_suffix (str): Custom suffix to append to each label.
    """
    num_ticks = (end_angle - start_angle) // step_size + 1
    tick_labels = [f"{i}{label_suffix}" for i in range(0, num_ticks * step_size, step_size)]

    if reverse_labels:
        tick_labels.reverse()

    angle_range = np.linspace(np.radians(start_angle), np.radians(end_angle), num_ticks)

    # Create the plot with custom labels and angles
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2.0)

    # Remove grid and axes
    ax.grid(False)
    ax.set_axis_off()

    # Draw ticks and labels
    for angle, label in zip(angle_range, tick_labels):
        ax.text(angle, 1.2, label, horizontalalignment='center', verticalalignment='center',
                fontsize=font_size, weight=font_weight, color=font_color)

    # Draw the outer circle
    outer_circle = plt.Circle((0, 0), 1.3, transform=ax.transData._b, fill=False,
                              linewidth=circle_linewidth, color=circle_color)
    ax.add_artist(outer_circle)

    # Save the plot as a PNG file
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)

# Example usage
create_gauge(
    start_angle=270, 
    end_angle=450, 
    step_size=5, 
    reverse_labels=True, 
    output_file='flexible_gauge_with_custom_text.png',
    font_size=12, 
    font_weight='normal', 
    font_color='blue', 
    circle_linewidth=3, 
    circle_color='red',
    label_suffix=' units'
)
