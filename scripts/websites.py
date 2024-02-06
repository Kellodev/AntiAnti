import webbrowser

def get_url(user_input):
    if user_input == "1":
        url = "https://www.youtubeunblocked.live"
    elif user_input == "2":
        url = "https://www.kadama.com"
    else:
        url = ""
        print("[ERROR] Invalid input")
    return url

def main():
    website = input("What website?: \n[1] Any website (PROXY)\n[2] School hacks (KADAMA)\n")
    url = get_url(website)

    if url:
        webbrowser.open(url)
    else:
        print("[ERROR] Invalid input")

if __name__ == "__main__":
    main()