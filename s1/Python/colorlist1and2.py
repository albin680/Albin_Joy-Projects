color_list_1 = ['Red', 'Green','Blue', 'white','orange']
color_list_2 = ['Green', 'orange', 'Black', 'white']
result_colors = [color for color in color_list_1 if color not in color_list_2]
print("colors from color_list_1 not contained in color_list_2:", result_colors)
