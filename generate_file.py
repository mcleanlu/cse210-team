# Utility to create a new python file.
# Usage: $ python generate_file.py


# Get inputs (file name, authors, assignment name)
file_name = input("What is the file name? ").strip()

authors = input("Who will work on it? (default: 'Luke, Carter') ").strip()
if authors == "":
    authors = "Luke McLean, Carter Kearns"

assignment = input("What assignment is this for? (default: 'Week ? Teach') ").strip()
if assignment == "":
    assignment = "Week ? Teach"

# Fill out template
template = f"""\"""
{file_name}

Author(s): {authors}
Assignment: {assignment}
\"""

def main():
    print("{file_name}")

if __name__ == "__main__":
    main()
"""

# Create and write to file
with open(file_name, "w+") as f:
    f.write(template)
    print(f"Generated file {file_name}!")
