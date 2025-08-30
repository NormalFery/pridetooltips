import json
import shutil
from pathlib import Path
from random import choice as random_choice
from string import ascii_lowercase


def create_pack_metadata(path: Path, description: str, pack_format: int = 37):
    """
    Generate a `pack.mcmeta` file with metadata about the resource pack.

    Parameters:
        path (Path): The path to save the `pack.mcmeta` file.
        description (str): The description of the pack.
        pack_format (int): The format version of the pack.
    """
    mcmeta_content = {
        "pack": {"pack_format": pack_format,
                 "supported_formats": {"min_inclusive": pack_format, "max_inclusive": 9999},
                 "description": description}}
    with path.open("w", encoding="utf-8") as file:
        # noinspection PyTypeChecker
        json.dump(mcmeta_content, file, indent=2)


def compress_and_remove_directory(directory: Path, zip_name: str = None):
    """
    Compress a directory into a .zip file and remove the original directory.

    Parameters:
        directory (Path): Directory to compress and remove.
        zip_name (str): Optional name for the .zip file.
    """
    if not directory.is_dir():
        raise ValueError(f"{directory} is not a directory or does not exist.")
    zip_path = directory.with_suffix('.zip') if zip_name is None else directory.parent / f"{zip_name}.zip"
    shutil.make_archive(str(zip_path.with_suffix('')), 'zip', str(directory))
    shutil.rmtree(directory)


def generate_random_word(length: int) -> str:
    """
    Generate a random lowercase word of a specified length.

    Parameters:
        length (int): The length of the word to generate. Must be a non-negative integer.

    Returns:
        str: A randomly generated word consisting of lowercase ASCII letters.

    Raises:
        ValueError: If the specified length is negative.
    """
    if length < 0:
        raise ValueError("Length must be a non-negative integer.")

    return ''.join(random_choice(ascii_lowercase) for _ in range(length))


def modrinth_markdown_template(template_path: Path, output_path: Path, context: dict) -> None:
    """
    Render a markdown file template by applying string formatting with a context dictionary.

    Parameters:
        template_path (Path): Path to the template markdown file.
        output_path (Path): Path where the rendered file should be written.
        context (dict): Dictionary of variables to fill into the template.
    """
    template = template_path.read_text(encoding="utf-8")
    rendered = template.format(**context)
    output_path.write_text(rendered, encoding="utf-8")
