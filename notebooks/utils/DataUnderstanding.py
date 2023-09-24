import pandas as pd


class DataUnderstanding():
    def verificando_as_dimensões_do_dataframe(
        self,
        dataframe: pd.DataFrame
    ):
        dataframe = dataframe.shape
        print(f'Linhas: {dataframe[0]} \nColunas: {dataframe[1]}')

    def descrição(
        self,
        dataframe: pd.DataFrame,
        percentiles=[.10, .15, .25, .75, .85, .95, .99],
        vertical=False
    ):
        if vertical:
            dataframe = (
                dataframe
                .describe(percentiles=percentiles)
                .T
                .round(decimals=2)
            )
        else:
            dataframe = (
                dataframe
                .describe(percentiles=percentiles)
                .round(decimals=2)
            )
        return dataframe

    def descrição_object(
        self,
        dataframe: pd.DataFrame,
        vertical=False
    ):
        if vertical:
            dataframe = dataframe.describe(include=['object']).T
        else:
            dataframe = dataframe.describe(include=['object'])
        return dataframe

    def verificando_tipos(
        self,
        dataframe: pd.DataFrame
    ):
        dataframe = (
            dataframe.dtypes
            .to_frame('Tipos')
        )
        return dataframe

    def verificando_valores_nulos(
        self,
        dataframe: pd.DataFrame
    ):
        valores_nulos = dataframe.isnull().sum()
        percent_missing = (valores_nulos / len(dataframe))
        dataframe = pd.DataFrame(
            {
                'Quantidade': valores_nulos,
                'Porcentagem': percent_missing
            }
        )
        dataframe = dataframe.style.format('{:.2%}', subset=['Porcentagem'])
        return dataframe

    def verificando_valores_duplicados(
        self,
        dataframe: pd.DataFrame
    ):
        valores_repetidos = dataframe.apply(lambda x: x.duplicated()).sum()
        percent_missing = (valores_repetidos / len(dataframe))
        dataframe = pd.DataFrame(
            {
                'Quantidade': valores_repetidos,
                'Porcentagem': percent_missing
            },
            index=dataframe.columns
        )

        dataframe = dataframe.style.format('{:.2%}', subset=['Porcentagem'])
        return dataframe

    def frequencia_da_repetição_dos_valores(
        self,
        dataframe: pd.DataFrame,
        coluna: str
    ):
        dataframe = dataframe[coluna].value_counts().reset_index()
        return dataframe

    def verificando_correlação(
        self,
        dataframe: pd.DataFrame
    ):
        dataframe = dataframe.corr()
        return dataframe


if __name__ == '__main__':
    data_understanding = DataUnderstanding()
