# encoding: utf-8

from google_images_download import google_images_download
import formatting as frm

response = google_images_download.googleimagesdownload()


def get_query():

    query = input("What should I draw?\n\x1b[5m ->\x1b[25m ")
    return query

    if query.strip() is None:
        print("Looking for random images...")
        query = "random"
        return query


@frm.blockprinting
def get_link(in_query):
    arguments = {
        "keywords": in_query,
        "format": "jpg",
        "limit": 1,
        "no_download": True,
        "print_urls": True,
        "size": "medium",
        "aspect_ratio": "panoramic",
    }

    try:
        path = response.download(arguments)

        (dictionary, not_needed) = path
        image_link = dictionary[in_query][0]
        return image_link
        # return str(path[0][in_query]).replace("[", "").replace("]", "")

    except FileNotFoundError:
        arguments = {
            "keywords": in_query,
            "format": "jpg",
            "limit": 1,
            "no_download": True,
            "print_urls": True,
            "size": "medium",
        }

        try:
            path = response.download(arguments)
            (dictionary, not_needed) = path
            image_link = dictionary[in_query][0]
            return image_link
            # return str(path[0][in_query]).replace("[", "").replace("]", "")

        except:
            pass
