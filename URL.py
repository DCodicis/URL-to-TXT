from colorama import init, Fore, Style
import os

# initialize colorama
init(autoreset=True)

# list to store URLs
urls = []  # empty list to store URLs

# display program creator name and version
# Please respect the work and do not change the name
# All about the version. If there is a change in the code that was created by anyone other than "DCodicis" then do not change the version
name = "DCodicis"
vertion = "1.0.1"

# create last_filename.txt file if it doesn't exist
if not os.path.exists("last_filename.txt"):
    with open("last_filename.txt", "w") as f:
        f.write("URL List.txt")

# print program title
def printTitle():
    print(Style.BRIGHT + Fore.YELLOW + "\n+-----------------------+")
    print(Style.BRIGHT + Fore.YELLOW + "|" + Style.BRIGHT + Fore.CYAN + "   Made By: "+ name + "   " + Style.BRIGHT + Fore.YELLOW + "|")
    print(Style.BRIGHT + Fore.YELLOW + "+-----------------------+")
    print(Style.BRIGHT + "          v" + vertion + "\n")

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

clearScreen()
printTitle()

# create last_filename.txt file if it doesn't exist
if not os.path.exists("last_filename.txt"):
    with open("last_filename.txt", "w") as f:
        f.write("URL List.txt")

# read last filename from file
last_filename_file = "last_filename.txt"
if os.path.exists(last_filename_file):
    with open(last_filename_file, "r") as f:
        filename = f.read().strip()
else:
    filename = "URL List.txt"

# read all filenames from all_files.txt and filter out any that don't exist
all_files = []
if os.path.exists("all_files.txt"):
    with open("all_files.txt", "r") as f:
        for line in f:
            file_name = line.strip()
            if os.path.exists(file_name):
                all_files.append(file_name)
else:
    open("all_files.txt", "w").close()

# check if the most recent filename in last_filename.txt exists in all_files.txt and add it if it doesn't exist
with open(last_filename_file, "r") as f:
    recent_filename = f.readlines()[-1].strip()

if recent_filename not in all_files:
    all_files.append(recent_filename)

with open("all_files.txt", "w") as f:
    for file_name in all_files:
        f.write(f"{file_name}\n")

# define a variable named file
file = None

while True:
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line and ":" in line:
                    label, url = line.split(":", 1)
                    urls.append((label.strip(), url.strip()))
            print(Style.BRIGHT + Fore.GREEN + "URLs loaded from file successfully!")
            break
    except FileNotFoundError:
        # display error message if file not found
        print(Style.BRIGHT + Fore.RED + f"\n{filename} file not found!\n")
        response = input(Style.BRIGHT + Fore.YELLOW + "Do you want to create a new file? (y/n): ")
        if response.lower() == "y":
            while True:
                new_filename = input(Style.BRIGHT + "Enter a new filename: ")
                if not new_filename.endswith(".txt"):
                    print(Style.BRIGHT + Fore.RED + "The filename must end with '.txt'!")
                elif os.path.exists(new_filename):
                    print(Style.BRIGHT + Fore.RED + "The file already exists!")
                else:
                    filename = new_filename
                    with open(last_filename_file, "w") as f:
                        f.write(filename)
                    try:
                        with open(filename, "w") as file:
                            for url in urls:
                                file.write(f"{url[0]}: {url[1]}\n")
                    except FileNotFoundError:
                        print(Style.BRIGHT + Fore.RED + f"\n{filename} file not found!\n")
                    break
        else:
            clearScreen()
            printTitle()
            filename = "URL List.txt"
            print(Style.BRIGHT + Fore.YELLOW + "Using default filename 'URL List.txt'.\n")




while True:
    # display menu options
    print(Style.BRIGHT +"\nYou are in: " + Fore.YELLOW+ filename)
    print(Style.BRIGHT + "\nMENU:\n")
    print(Style.BRIGHT + Fore.CYAN + "1. Add URL")
    print(Style.BRIGHT + Fore.CYAN + "2. Add New URL List")
    print(Style.BRIGHT + Fore.CYAN + "3. Remove URL")
    print(Style.BRIGHT + Fore.CYAN + "4. Show All URLs")
    print(Style.BRIGHT + Fore.CYAN + "5. Change URL List")
    print(Style.BRIGHT + Fore.CYAN + "6. Exit\n")

    choice = input(Style.BRIGHT + "Enter your choice (1-5): ")
    print()

    if choice == "1":
        clearScreen()
        printTitle()

        # add a new URL to the list
        url = input(Style.BRIGHT + "Enter a URL: ")
        label = input(Style.BRIGHT + "Enter a label for the URL: ")
        urls.append((label, url))  # add the URL and label as a tuple

        # save URLs to file
        if urls:
            with open(filename, "w") as file:
                for url in urls:
                    file.write(f"{url[0]}: {url[1]}\n")
        clearScreen()
        printTitle()
        print(Style.BRIGHT + Fore.GREEN + "\nURL added successfully!\n")

    elif choice == "2":
        clearScreen()
        printTitle()

        # add a new URL list
        while True:
            filename = input(Style.BRIGHT + "Enter a filename for the new URL list (include '.txt' extension): ")
            if filename in last_filename_file:
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.RED + f"The filename '{filename}' already exists in the recent history!")
            elif os.path.exists(filename):
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.RED + "The file already exists!")
            else:
                urls = []
                with open(filename, "w") as file:
                    print(Style.BRIGHT + Fore.YELLOW + f"New URL list '{filename}' created successfully!")
                    while True:
                        url = input(Style.BRIGHT + "\nEnter a URL or 'q' to quit: ")
                        if url.lower() == "q":
                            break
                        label = input(Style.BRIGHT + "Enter a label for the URL: ")
                        urls.append((label, url))  # add the URL and label as a tuple
                        file.write(f"{label}: {url}\n")
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.GREEN + "URLs added successfully!")
                with open(last_filename_file, "w") as f:
                    f.write(filename)
                break



    elif choice == "3":
        clearScreen()
        printTitle()

        # show all URLs
        if not urls:
            clearScreen()
            printTitle()
            print(Style.BRIGHT + Fore.RED + "No URLs found!")
        else:
            print("{:<39}{}".format(Style.BRIGHT + Fore.YELLOW + "Label", "URL\n"))
            for url in urls:
                print("{:<30}{}".format(url[0], url[1]))

            # remove a URL from the list
            label = input(Style.BRIGHT + "\nEnter the label of the URL to remove: ")
            print()
            for url in urls:
                if url[0] == label:  # check if label matches
                    urls.remove(url)
                    clearScreen()
                    printTitle()
                    print(Style.BRIGHT + Fore.GREEN + "URL removed successfully!\n")
                    break
            else:
                clearScreen()
                printTitle()
                print(Style.BRIGHT + Fore.RED + "Label not found!\n")

            # display URLs from file
            file_urls = []
            try:
                with open(filename, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line and ":" in line:
                            label, url = line.split(":", 1)
                            if (label.strip(), url.strip()) not in urls:
                                file_urls.append((label.strip(), url.strip()))
            except FileNotFoundError:
                clearScreen()
                printTitle()
                # display error message if file not found
                print(Style.BRIGHT + Fore.RED + f"{filename} file not found!")


    elif choice == "4":
        clearScreen()
        printTitle()

        # show all URLs
        if not urls:
            clearScreen()
            printTitle()
            print(Style.BRIGHT + Fore.RED + "No URLs found!")
        else:
            print("{:<39}{}".format(Style.BRIGHT + Fore.YELLOW + "Label", "URL\n"))
            for url in urls:
                print("{:<30}{}".format(url[0], url[1]))

            # display URLs from file
            file_urls = []
            try:
                with open(filename, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line and ":" in line:
                            label, url = line.split(":", 1)
                            if (label.strip(), url.strip()) not in urls:
                                file_urls.append((label.strip(), url.strip()))
                        if file_urls:
                            print(Fore.MAGENTA + "\nURLs from file:")
                            for url in file_urls:
                                print("{:<30}{}".format(url[0], url[1]))
            except FileNotFoundError:
                # display error message if file not found
                print(Style.BRIGHT + Fore.RED + "URL List.txt file not found!")

    elif choice == "5":
        clearScreen()
        printTitle()

        # exit the program
        print(Style.BRIGHT + Fore.YELLOW + "\n\nGood Bay...\n\n")
        break

    else:
        clearScreen()
        printTitle()

        # display error message if choice is invalid
        print(Style.BRIGHT + Fore.RED + "Invalid choice!")
