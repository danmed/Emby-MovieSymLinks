# Movie Symlink Organizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python script to automatically scan a messy movie collection, replicate its folder structure, and create cleaned-up, renamed symbolic links. This is ideal for creating a clean and organized library for media servers like Plex, Jellyfin, or Kodi without duplicating your files.

## The Problem

Your movie download folder is probably messy. Each movie is in its own folder, but contains extra files like `.nfo`, `.txt`, sample videos, or cover art. The movie filenames themselves are often long and inconsistent.

Pointing your media server directly at this folder can result in a cluttered library. This script solves the problem by creating a clean, parallel directory structure that contains only symlinks to your actual video files, renamed in a consistent format.

## Features

-   **Recreates Folder Structure**: Mirrors the source directory's folder-per-movie organization.
-   **Creates Symbolic Links**: Organizes your library without using extra disk space.
-   **Cleans and Renames**: Renames links to a simple, consistent format: `Movie Folder Name-Resolution.ext`.
-   **Auto-detects Resolution**: Parses the original filename to find the resolution (e.g., `1080p`, `4k`, `720p`).
-   **Ignores Junk Files**: Automatically skips non-movie files based on their extension.
-   **Skips System Folders**: Ignores common system folders like `System Volume Information`, `$RECYCLE.BIN`, and hidden dot-folders.
-   **Configurable**: Easily change the list of movie extensions and ignored folders at the top of the script.
-   **Idempotent**: Safe to run multiple times. It will not overwrite existing links and will only add new ones.

## How It Works

The script reads a **source** directory and builds a clean **destination** directory.

> For example, let's say your source directory looks like this:

**BEFORE:**

<img width="565" height="330" alt="image" src="https://github.com/user-attachments/assets/cd6e02d3-5abe-412c-8b2d-3bf96ead5bfe" />



> After running the script, the new destination directory will look like this:

**AFTER:**

<img width="415" height="184" alt="image" src="https://github.com/user-attachments/assets/d7ed6244-b652-498e-837f-a067fa279d09" />


*Note: The files in `OrganizedMovies` are **symlinks** (shortcuts), not copies. The original files in `UnsortedMovies` remain untouched.*

## Requirements

-   **Python 3.6+**
-   No external libraries are needed.

## Installation

No installation is necessary. Simply download the `organize_movies.py` script to your computer.

You can clone this repository:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

Or just download the organize_movies.py file directly.

Usage

The script is run from the command line, and it requires two arguments: the path to your source directory and the path to your destination directory.
Bash

python organize_movies.py <source_directory> <destination_directory>

Important: If your file paths contain spaces, be sure to wrap them in quotes.

Examples

On macOS / Linux:
Bash

python organize_movies.py "/media/downloads/movies" "/media/plex/movies"

On Windows (using PowerShell or Command Prompt):
Bash

python organize_movies.py "C:\Users\YourUser\Downloads\Movies" "D:\Plex Library\Movies"

The script will print its progress to the terminal, indicating which folders it's processing, which links it's creating, and which files or folders it's skipping.

Configuration

You can customize the script's behavior by editing these two variables at the top of the organize_movies.py file:

    MOVIE_EXTENSIONS: A list of file extensions that the script should identify as movie files.
    Python

# A set of common movie file extensions (case-insensitive).
MOVIE_EXTENSIONS = {'.mkv', '.mp4', '.avi', '.mov', '.wmv'}

IGNORE_FOLDERS: A list of folder names that the script should completely ignore.
Python

    # A set of folder names to ignore (case-insensitive).
    IGNORE_FOLDERS = {'system volume information', '$recycle.bin'}

Important Notes

What is a Symbolic Link (Symlink)?

A symlink is a special type of file that acts as a shortcut or pointer to another file or directory. This means you can have a cleanly organized library for your media server that points to the original files without taking up any significant additional disk space.

    If you delete the symlink, the original file is safe.

    If you delete the original file, the symlink will break.

Windows Permissions

On Windows, creating symbolic links may require special permissions. If you encounter an OSError: [WinError 1314] or a similar permission-denied message, you have two options:

    Run as Administrator: Run your Command Prompt or PowerShell terminal as an Administrator.

    Enable Developer Mode: Enable Developer Mode in Windows settings (Settings > Update & Security > For developers). This allows your user account to create symlinks without needing to run as an administrator every time.

License

This project is licensed under the MIT License. See the LICENSE file for details.
