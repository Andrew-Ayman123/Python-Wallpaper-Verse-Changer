<div align="center">

  <h1> Wallpaper Bible Verse Daily Changer</h1>
  <img src="https://madewithlove.now.sh/eg?heart=true" alt="Made with love in Egypt">
  <h3> Generates a customized wallpaper image every day with a bible verse from dailyverses.net written over a background image of your choice. The wallpaper is automatically set as your desktop background at a scheduled time.
</h3>
</div>

## :star2: About The Project
**Features:** 
- Browse and select a custom background image
- Configure font settings, size, width, color and verse position  
- Live preview of updates  
- Save settings to automatically generate the wallpaper daily 
- Prompt to save unsaved changes before closing
- Uses Windows Task Scheduler to run script at scheduled time
  
**Screenshots:** 
- The GUI When it first opens by default
<img src="screen_shots/1.png"  height="400"/>

- The default image but with some edits in size, position and color
<img src="screen_shots/2.png"  height="400"/>

- When another image is selected by the "Browse" button
<img src="screen_shots/3.png"  height="400"/>

- My bacground changed when "Save" is pressed
<img src="screen_shots/4.png"  height="400"/>

- A task is successfully created in my Task Scheduler
<img src="screen_shots/5.png"  height="400"/>


  
## :space_invader: Built With
- ![python]
- GUI: ![qt]
- PIL (for editing and writing on the image)
- requests (for downloading the verse page)
- BeautifulSoup (for web scraping the verse)
- win32com (for communicating with windows task schedular)
- json (to read settings json file)

## :toolbox: Installation
1. Run `change_wallpaper_gui.py` to start the application
2. Select a background image and set the font, size, color and text position
3. Click "Save" to:
   - Create a scheduled task in Windows Task Scheduler to run the `change_wallpaper_daily.py` daily
   - Save your settings to `settings.json`
   - Generate the wallpaper image 
4. The application will show a preview of the wallpaper 
5. Any unsaved changes will prompt you to save or discard before exiting
6. Upon exit, the temporary wallpaper image is deleted




## :confetti_ball: Credits

- [Arabic bible text from dailyverses.net](https://dailyverses.net/ar)

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[qt]: https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white
