#!/usr/bin/env python3
import os
import re
import sys
import argparse

# --- Configuration ---
# A set of common movie file extensions (case-insensitive).
MOVIE_EXTENSIONS = {'.mkv', '.mp4', '.avi', '.mov', '.wmv'}

# A set of folder names to ignore (case-insensitive).
IGNORE_FOLDERS = {'system volume information', '$recycle.bin'}


def get_resolution(filename):
    """
    Extracts video resolution from a filename using regular expressions.
    Looks for patterns like 1080p, 720p, 2160p, 4K, etc.
    """
    # Regex to find common resolution patterns (e.g., 720p, 1080p, 2160p, 4k)
    # It's case-insensitive.
    match = re.search(r'(\d{3,4}p|4k|2160p)', filename, re.IGNORECASE)
    if match:
        return match.group(1).lower()
    return None

def create_movie_symlinks(source_dir, dest_dir):
    """
    Scans a source directory, recreates its subfolder structure in a
    destination directory, and creates organized symlinks to movie files.
    """
    print(f"🎬 Starting scan of source folder: {source_dir}")
    print(f"    Writing to destination folder: {dest_dir}\n")

    # Ensure the main destination folder exists
    try:
        os.makedirs(dest_dir, exist_ok=True)
    except OSError as e:
        print(f"❌ Error creating destination directory '{dest_dir}': {e}")
        return

    # Iterate through items (files and folders) in the source directory
    for folder_name in os.listdir(source_dir):
        # --- NEW: Check if the folder should be ignored ---
        if folder_name.lower() in IGNORE_FOLDERS or folder_name.startswith('.'):
            print(f"Ignoring system/hidden folder: '{folder_name}'")
            continue

        source_subfolder = os.path.join(source_dir, folder_name)

        # Process only if it's a directory
        if not os.path.isdir(source_subfolder):
            continue

        print(f"Processing folder: '{folder_name}'")

        # Recreate the subfolder in the destination
        dest_subfolder = os.path.join(dest_dir, folder_name)
        os.makedirs(dest_subfolder, exist_ok=True)

        # Scan for movie files inside the source subfolder
        for filename in os.listdir(source_subfolder):
            # Check for a valid movie extension
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in MOVIE_EXTENSIONS:
                continue # Skip non-movie files

            # Extract the resolution from the filename
            resolution = get_resolution(filename)
            if not resolution:
                print(f"  - ⚠️  Could not find resolution for '{filename}'. Skipping.")
                continue

            # Construct the new symlink name
            # Format: FolderName-Resolution.ext
            new_link_name = f"{folder_name}-{resolution}{file_ext}"

            # Define the full paths for the original file and the new symlink
            original_file_path = os.path.join(source_subfolder, filename)
            symlink_path = os.path.join(dest_subfolder, new_link_name)

            # Create the symbolic link if it doesn't already exist
            if not os.path.lexists(symlink_path):
                try:
                    os.symlink(original_file_path, symlink_path)
                    print(f"  - ✅  Created link: '{new_link_name}'")
                except OSError as e:
                    print(f"  - ❌  Failed to create symlink for '{filename}': {e}")
            else:
                print(f"  - ℹ️   Link '{new_link_name}' already exists. Skipping.")

    print("\n✨ Scan complete!")

def main():
    """Main function to parse arguments and run the script."""
    parser = argparse.ArgumentParser(
        description="Scan a movie folder, recreate its structure, and create named symlinks to video files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("source_dir", help="The source directory containing your movie folders.")
    parser.add_argument("dest_dir", help="The destination directory where symlinks will be created.")

    args = parser.parse_args()

    # Verify that the source directory exists
    if not os.path.isdir(args.source_dir):
        print(f"Error: Source directory not found at '{args.source_dir}'")
        sys.exit(1)

    create_movie_symlinks(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()
