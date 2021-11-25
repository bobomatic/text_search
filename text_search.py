"""Takes a directory and searches for all unique files containing the search text.
"""
import sys
import os


def search(args):
	files_containing_search_term = []
	folder = args[1]
	search_term = args[2]

	for root, dirs, files in os.walk(folder):
		for name in files:
			file = os.path.join(root, name)
			with open(file, 'r') as f:
				try:
					for line in f:
						if search_term in line:
							files_containing_search_term.append(file)
							break
				except UnicodeDecodeError:
					# print(f"ignoring {file}")
					continue

	print(f"List of files containing the phrase '{search_term}': {files_containing_search_term}")


if __name__ == '__main__':
	if len(sys.argv) == 3:
		sys.exit(search(sys.argv[0:]))
	else:
		print("Please provide a source directory and a search term")