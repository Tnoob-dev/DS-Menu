import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict, Union

def general_graph(to_plot: Union[pd.Series, pd.DataFrame]) -> None:
    plt.figure(figsize=(8, 5))
    to_plot.plot(kind="bar", color="green")
    plt.xticks(rotation=45)
    plt.xlabel("Categorias")
    plt.ylabel("Precios")
    plt.title("Promedio de precios entre los diferentes tipos de platos en toda La Habana")
    plt.show()

def graph_bar_by_zone(groups: List[pd.Series], colors: List[str], zones: List[str]) -> None:
    
    fig, axes = plt.subplots(1, len(groups), figsize=(15, 5))
    
    for group_index, (group_name, direction) in enumerate(zip(groups, zones)):
        color = colors[group_index] if group_index < len(colors) else 'blue'
        axes[group_index].bar(group_name.index, group_name.values, color=color)
        axes[group_index].set_title(direction)
        axes[group_index].tick_params(axis='x', labelrotation=90,  labelright=False, labelleft=True )
    plt.show()


def graph_opening_frequences(count: Dict[str, Dict[str, int]]) -> None:
    for day, day_counts in count.items():
        keys: List[str] = list(dict(sorted(day_counts.items())).keys())
        values: List[int] = list(dict(sorted(day_counts.items())).values())
        
        
        plt.figure(figsize=(10, 5))
        plt.bar(keys, values, color="mediumpurple")
        plt.xticks(rotation=45)
        plt.xlabel("Horarios")
        plt.ylabel("Frecuencia")
        plt.title(f"Horarios de Apertura más Frecuentes los {day}")
        plt.show()
