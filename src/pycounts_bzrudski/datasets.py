from importlib import resources
import pathlib

def get_flatland() -> pathlib.Path:
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.Path
        Path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    with resources.path("pycounts_bzrudski.data", "flatland.txt") as f:
        data_file_path = f
    return data_file_path
