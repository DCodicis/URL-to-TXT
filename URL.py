from colorama import init, Fore, Style

# initialize colorama
init(autoreset=True)

urls = []  # empty list to store URLs

# read existing URLs from file
try:
    with open("URL List.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line and ":" in line:
                label, url = line.split(":", 1)
                urls.append((label.strip(), url.strip()))
    print(Style.BRIGHT + Fore.GREEN + "URLs loaded from file successfully!")
except FileNotFoundError:
    print(Style.BRIGHT + Fore.RED + "\nURL List.txt file not found!\n")
    print(Style.BRIGHT + Fore.YELLOW + "Warning: If you have moved this file or renamed it, please move it back to the same folder as this program, or rename it to 'URL List'.")
    print(Style.BRIGHT + Fore.YELLOW + "But if this is your first time, follow the menu below.\n")

while True:
    # display menu options
    print(Style.BRIGHT + "\nMENU:\n")
    print(Style.BRIGHT + Fore.CYAN + "1. Add URL")
    print(Style.BRIGHT + Fore.CYAN + "2. Remove URL")
    print(Style.BRIGHT + Fore.CYAN + "3. Show All URLs")
    print(Style.BRIGHT + Fore.CYAN + "4. Exit\n")

    choice = input(Style.BRIGHT + "Enter your choice (1-4): ")
    print()

    if choice == "1":
        # add a new URL to the list
        url = input(Style.BRIGHT + "Enter a URL: ")
        label = input(Style.BRIGHT + "Enter a label for the URL: ")
        urls.append((label, url))  # add the URL and label as a tuple
        print(Style.BRIGHT + Fore.GREEN + "URL added successfully!")

    elif choice == "2":
        # remove a URL from the list
        label = input(Style.BRIGHT + "Enter the label of the URL to remove: ")
        print()
        for url in urls:
            if url[0] == label:  # check if label matches
                urls.remove(url)
                print(Style.BRIGHT + Fore.GREEN + "URL removed successfully!\n")
                break
        else:
            print(Style.BRIGHT + Fore.RED + "Label not found!\n")

    elif choice == "3":
        # show all URLs
        if not urls:
            print(Style.BRIGHT + Fore.RED + "No URLs found!")
        else:
            print("{:<39}{}".format(Style.BRIGHT + Fore.YELLOW + "Label", "URL\n"))
            for url in urls:
                print("{:<30}{}".format(url[0], url[1]))

            # display URLs from file
            file_urls = []
            try:
                with open("URL List.txt", "r") as file:
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
                print(Style.BRIGHT + Fore.RED + "URL List.txt file not found!")

    elif choice == "4":
        # exit the program and write URLs to file
        if urls:
            with open("URL List.txt", "w") as file:
                for url in urls:
                    file.write(f"{url[0]}: {url[1]}\n")
            print(Style.BRIGHT + Fore.GREEN + "URLs written to file successfully!\n")
        print(Style.BRIGHT + Fore.YELLOW + "Exiting program...\n\n")
        break

    else:
        print(Style.BRIGHT + Fore.RED + "Invalid choice!")
