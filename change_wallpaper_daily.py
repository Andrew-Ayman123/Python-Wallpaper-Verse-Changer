# Import necessary modules
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import ctypes
import ctypes.util
from datetime import datetime
import json
import textwrap


def get_bible_verse(backup_text) -> str:
    try:
        # Get the current date
        date = datetime.now()

        # Make a request to the dailyverses.net website for the verse of the day
        res: requests.Response = requests.get(
            f"https://dailyverses.net/ar/{date.year}/{date.month}/{date.day}/")
        res.raise_for_status()

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(res.content, 'html.parser')

        # Extract the verse text and reference from the HTML
        text = soup.find('span', {'class': 'v1'}).text
        text += "\n("+soup.find('a', {'class': 'vc'}).text+")"

        # Return the verse text and reference as a string
        return text
    except:
        return backup_text


def write_image(jsonSettings, text, output_path) -> str:
    # Open the image file
    image = Image.open(jsonSettings["imagePath"])

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the font and font size
    font = ImageFont.truetype(
        jsonSettings["fontFamily"], jsonSettings["fontSize"])

    text_wrapped = textwrap.fill(text, jsonSettings["verseWidth"])
    text_wrapped = text_wrapped.replace("(", "\n(")
    # Get the size of the text
    text_size = draw.textsize(text_wrapped, font=font, direction="ltr")

    # Calculate the position to write the text
    x = (image.width - text_size[0]) * jsonSettings["xRatio"]
    y = (image.height - text_size[1]) * jsonSettings["yRatio"]

    # Write the text on the image
    draw.text((x, y), text_wrapped,
              fill=jsonSettings["fontColor"], font=font, align='center')

    # Save the modified image to a file

    image.save(output_path)
    image.close()
    # Return the path to the output image file
    return output_path


def change_wallpaper(image_path):
    # Set the wallpaper image as the current desktop background using the Windows API
    image_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def loadSettings() -> dict:
    try:
        with open("./settings.json", encoding="utf-8")as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(e)
        return {
            "fontFamily": "./DUBAI-BOLD.TTF",
            "fontColor": "#dddddd",
            "fontSize": 36,
            "xRatio": 0.5,
            "yRatio": 0.85,
            "verseWidth": 150,
            "imagePath": "./original.png",
            "taskName": "Change Wallpaper Bible Verse",
            "backUpText": "يَا رَبُّ، قَدِ ٱخْتَبَرْتَنِي وَعَرَفْتَنِي. أَنْتَ عَرَفْتَ جُلُوسِي وَقِيَامِي. فَهِمْتَ فِكْرِي مِنْ بَعِيدٍ.\n(اَلْمَزَامِيرُ ١٣٩:‏١-‏٢)"
        }


def main():
    # Run the main function when the script is executed

    jsonSettings = loadSettings()
    # Get the verse of the day
    text = get_bible_verse(jsonSettings["backUpText"])

    if(jsonSettings["backUpText"] != text):
        print("sadas")
        jsonSettings["backUpText"] = text

        with open("./settings.json", "w", encoding="utf-8") as json_file:
            # Write the dictionary to the JSON file
            json.dump(jsonSettings, json_file, ensure_ascii=False)

    outputPath = "./daily_wallpaper.png"
    # Write the verse text on the wallpaper image and save to a file
    output_path = write_image(jsonSettings, text, outputPath)

    # Set the modified image as the desktop background
    change_wallpaper(output_path)


if __name__ == "__main__":
    main()
