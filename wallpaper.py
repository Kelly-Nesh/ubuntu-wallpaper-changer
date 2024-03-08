#!/usr/bin/python3
import requests
import os

BASE_DIR = os.path.expanduser("~/.local/share/")
# Directory with xml that 'points' to xml file with background settings
GNOME_BACKGROUND_XML_PATH = BASE_DIR + "gnome-background-properties/"
GNOME_XML = GNOME_BACKGROUND_XML_PATH + "slideshow.xml"
# Directory with background image and xml
BACKGROUND_PATH = BASE_DIR + "backgrounds/"
# Path to background xml
BACKGROUND_XML = BACKGROUND_PATH + "background.xml"
# Path to image used as background
BACKGROUND_IMAGE = BACKGROUND_PATH + "background.jpg"

GNOME_BACKGROUND_XML_CONTENT = \
    f"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>
  <wallpaper>
    <name>{os.getenv("USER")}'s custom slideshow</name>
    <filename>{BACKGROUND_XML}</filename>
    <options>zoom</options>
  </wallpaper>
</wallpapers>
"""
BACKGROUND_XML_CONTENT =\
    f"""
<background>
  <starttime>
    <year>2024</year>
    <month>01</month>
    <day>01</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->
  <static>
    <duration>60000.0</duration>
    <file>{BACKGROUND_IMAGE}</file>
  </static>
</background>
"""


def prepare():
    """
    create directories for background images and xml files
    checks whether xml files exist
    """
    if os.path.isfile(GNOME_XML) and os.path.isfile(BACKGROUND_XML):
        return True
    for path in [GNOME_BACKGROUND_XML_PATH, BACKGROUND_PATH]:
        os.system("mkdir -p {}".format(path))


def setup():
    """
    Setup function

    This function creates the directories for the background images and xml files,
    and creates the gnome background xml and background xml files with the required content.
    """
    if prepare():
        return
    # create gnome background xml file
    with open(GNOME_XML, 'w+', encoding='utf-8') as gxml:
        gxml.write(GNOME_BACKGROUND_XML_CONTENT)

    # create background xml file
    with open(BACKGROUND_XML, 'w+', encoding='utf-8') as bgxml:
        bgxml.write(BACKGROUND_XML_CONTENT)


def main():
    """
    Creates a background image for the Gnome desktop background slideshow.

    This function uses the requests library to download an image from the
    https://picsum.photos/2500 endpoint, and saves the image to the
    ~/.local/share/backgrounds/background.jpg file.

    Returns:
        None

    """
    # create background image
    res = requests.get("https://picsum.photos/2500")
    with open(BACKGROUND_IMAGE, "wb") as bg:
        bg.write(res.content)


if __name__ == "__main__":
    setup()
    main()
