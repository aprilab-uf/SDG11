import os
import uuid
import argparse
'''
Description:
Provides CLI to rename all videos in a provided directory with names matching dataset convention.

TO USE:
python rename_files.py -d /path/to/directory -b action_environment_diverOrientation

EXAMPLE:
python rename_files.py -d /home/Documents/gestureVideos -b OKAY_REEF_HORIZONTAL
'''

def rename_files_in_directory(directory, base_name):
    """Renames all files in the given directory with a specified base name and a random 10-character hash."""
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            _, fileext = os.path.splitext(filename)  # Keep the original file extension
            hash_value = uuid.uuid4().hex[:10]  # Generate a 10-character hash
            new_filename = f"{base_name}_{hash_value}{fileext}"  # Apply new base name
            new_file_path = os.path.join(directory, new_filename)

            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} → {new_filename}")

def main():
    parser = argparse.ArgumentParser(description="Rename all files in a directory with a specified base name and a random 10-character hash.")
    parser.add_argument("-d", "--directory", type=str, required=True, help="Path to the directory containing files to rename.")
    parser.add_argument("-b", "--base", type=str, required=True, help="New base name for the files.")

    args = parser.parse_args()
    rename_files_in_directory(args.directory, args.base)

if __name__ == "__main__":
    main()
