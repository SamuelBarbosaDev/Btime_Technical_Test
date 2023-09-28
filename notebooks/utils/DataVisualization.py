import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.DataUnderstanding import DataUnderstanding
from sklearn.preprocessing import scale


class DataVisualization(DataUnderstanding):
    def __init__(self) -> None:
        sns.set_theme(
            context='talk',
            style='ticks',
            font_scale=.8,
            palette='tab10',
            rc={
                'figure.figsize': (12, 8),
                'axes.grid': True,
                'grid.alpha': .2,
                'axes.titlesize': 'x-large',
                'axes.titleweight': 'bold',
                'axes.titlepad': 20,
            }
        )

        self.scatter_kwargs = dict(palette='viridis', alpha=0.8, linewidth=0)

    def gráfico_barplot(
        self,
        dataframe: pd.DataFrame,
        x: str,
        y: str
    ):
        sns.barplot(
            data=dataframe,
            x=x,
            y=y
        )
        plt.show()

    def gráfico_pairplot(
        self,
        dataframe: pd.DataFrame
    ):
        sns.pairplot(dataframe)
        plt.show()

    def gráfico_heatmap(
        self,
        dataframe: pd.DataFrame
    ):
        sns.set(style='white')
        corr = dataframe.corr()
        plt.figure(figsize=(16, 10))
        sns.heatmap(
            corr, annot=True, cmap='RdBu_r', fmt='.2f', annot_kws={'size': 12}
        )
        plt.show()

    def gráfico_boxplot(
        self,
        dataframe: pd.DataFrame,
        figsize: tuple,
    ):
        dataframe = dataframe.select_dtypes(include='number')
        dataframe = dataframe.apply(scale)
        fig = plt.figure(figsize=figsize)
        sns.boxplot(data=dataframe)
        plt.xticks(rotation=60, ha='right')
        plt.show()

    def gráfico_boxplot_para_comparação_variáveis(
        self,
        dataframe: pd.DataFrame,
        figsize: tuple,
        x: str = '',
        y: str = ''
    ):
        fig = plt.figure(figsize=figsize)
        sns.boxplot(data=dataframe, x=x, y=y)
        plt.show()

    def gráfico_histplot(
        self,
        dataframe: pd.DataFrame,
        coluna: str
    ):
        sns.histplot(data=dataframe[coluna])
        plt.xticks(rotation=60, ha='right')
        plt.show()

    def gráfico_scatterplot(
        self,
        dataframe: pd.DataFrame,
        x: str,
        y: str,
        hue: list,
        titulo: str = ''
    ):
        sns.scatterplot(data=dataframe, x=x, y=y, hue=hue)
        plt.title(titulo)
        plt.show()


if __name__ == '__main__':
    data_visualization = DataVisualization()