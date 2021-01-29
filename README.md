# osu-map-downloader
Download osu! beatmaps from download links stored in a text file

You need:
* text file (map_links.txt) where your osu! beatmap links are stored (e.g. https://osu.ppy.sh/beatmapsets/1012634/download)
* Python 3 with `browser-cookie3` and `requests` libraries installed

Notes:
1. Make sure you are signed in to your account from Chrome or Firefox
2. browser-cookie3 uses cookies in your browser (your login and password for osu!. So, script automatically signes you in osu! when you run it)
3. If there is something wrong with the link, the link is saved in errors.txt (try manually downloading or run script again for those links because I don't know why, but sometimes code downloads some links in errors.txt after rerunning script)

TODO:
1. add a script to scan osu songs folder, find links for beatmaps and put them to map_links.txt
2. add some GUI

Any feature requests are welcome!
