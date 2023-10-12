import matplotlib.pyplot as plt
def create_img(text,location):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Add text to the axis
    # text = "Hello, Matplotlib!"
    ax.text(0.5, 0.5, text, fontsize=12, ha='center')

    # Set axis limits (optional)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove axis labels and ticks (optional)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Save the figure as an image
    plt.savefig(location, dpi=300, bbox_inches='tight')

    # Display the image (optional)
    # plt.show()

