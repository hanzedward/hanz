def main():
    year = int(input("Enter the year: "))
    genre = input("Enter the genre: ")
    album = input("Enter the album: ")
    title = input("Enter the song title: ")
    artist = input("Enter the artist: ")

    print("-------------------------")
    print("SONG DETAILS")
    print("-------------------------")
    print(f"Year Released: {year}")
    print(f"Genre: {genre}")
    print(f"Album: {album}")
    print(f"Title: \"{title}\"")
    print(f"Artist: {artist}")

if __name__ == "__main__":
    main()