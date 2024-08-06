import matplotlib.colors as mcolors

def generate_color_mapping(size):
    base_colors = [
        '#eee4da', '#ede0c8', '#f2b179', '#f59563', '#f67c5f',
        '#f65e3b', '#edcf72', '#edcc61', '#edc850', '#edc53f',
        '#edc22e', '#3c3a32'
    ]

    def interpolate_color(color1, color2, factor):
        c1 = mcolors.hex2color(color1)
        c2 = mcolors.hex2color(color2)
        return mcolors.to_hex([c1[i] * (1 - factor) + c2[i] * factor for i in range(3)])

    color_mapping = {}
    num_colors = len(base_colors)
    
    for exp in range(1, size*size + 1):
        number = 2 ** exp
        if exp < num_colors:
            color_mapping[number] = base_colors[exp - 1]
        else:
            segment = (exp - num_colors) % (num_colors - 1)
            prev_color = base_colors[(exp - num_colors) // (num_colors - 1)]
            next_color = base_colors[(exp - num_colors) // (num_colors - 1) + 1]
            color_mapping[number] = interpolate_color(prev_color, next_color, segment / (num_colors - 1))
    
    return color_mapping