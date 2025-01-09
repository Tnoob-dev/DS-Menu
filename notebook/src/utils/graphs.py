import matplotlib.pyplot as plt
import random

def general_graph(to_plot):
    plt.figure(figsize=(8, 5))
    to_plot.plot(kind="bar", color="green")
    plt.xticks(rotation=45)
    plt.xlabel("Category")
    plt.ylabel("Price")
    plt.title("Promedio de precios entre los diferentes tipos de platos en toda La Habana")
    plt.show()

def graph_bar_by_zone(groups: list, colors: list, zones: list):
    
    fig, axes = plt.subplots(1, len(groups), figsize=(15, 5))
    
    for group_index, (group_name, direction) in enumerate(zip(groups, zones)):
        color = colors[group_index] if group_index < len(colors) else 'blue'
        axes[group_index].bar(group_name.index, group_name.values, color=color)
        axes[group_index].set_title(direction)
        # axes[group_index].set_xlabel("Category")
        # axes[group_index].set_ylabel("Price")
        axes[group_index].tick_params(axis='x', labelrotation=90,  labelright=False, labelleft=True )
        
    plt.show()