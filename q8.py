def valid_URL(URL):
    """

    :param URL: the text that we want to check if it is a valid URL
    :return: True if it is a Valid URL, False otherwise
    """
    URL = str(URL)
    if URL.startswith("http://") and (URL.__contains__(".com") or URL.__contains__(".co") or URL.__contains__(".gov")):
        print("This is a valid URL")
    else:
        print("This is not a valid URL")

print(valid_URL("http://abd.com"))