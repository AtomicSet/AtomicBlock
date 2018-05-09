import os


def path(file: str) -> str:
    """
    Provide absolute path to requested files

    Args:
        file (str): input file name

    Returns:
        str: The absolute path to the input file
    """
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "..",
        "raw",
        file
    )
