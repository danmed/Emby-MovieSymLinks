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
