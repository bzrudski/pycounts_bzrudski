import matplotlib.pyplot as plt

from collections import Counter
from matplotlib.figure import Figure

def plot_words(word_counts: Counter, n: int = 10) -> Figure:
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig
