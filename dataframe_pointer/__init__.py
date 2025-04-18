import pandas as pd


# TODO: create test cases

df_pointers = {}

@pd.api.extensions.register_dataframe_accessor('pointer')
class PointerAcessor:

    def __init__(self, df):
        self._df = df

    def __call__(self):
        return _create_dataframe_pointer(self._df)


def _create_dataframe_pointer(df):
    new_pointer = _DFPointer(df)
    if hash(new_pointer) in df_pointers:
        return df_pointers[hash(new_pointer)]
    df_pointers[hash(new_pointer)] = new_pointer
    return new_pointer


class _DFPointer:
    """A df pointer acts as a pointer to a dataframe.

    It can be used as an element within a dataframe without breaking .groupby and .unique
    
    The .df property is a copy of the relevant dataframe.
    _DFPointer objects which point to identical dataframes are the __same__ object.
    """

    def __init__(self, df):
        self._df = df.copy()

    def __hash__(self):
        return hash(tuple((col, tuple(self.df[col])) for col in self._df.columns))

    @property
    def df(self):
        """DataFrame assoicated with this pointer."""
        return self._df.copy()

    def __str__(self):
        return f"dataframe pointer: {self._df}"

    def __repr__(self):
        return f"dataframe pointer: {hash(self)}"

