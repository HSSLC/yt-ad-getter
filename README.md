# yt-ad-getter
download youtube advertisement video
99.9% unnecessary program

## requires
requests

## usage
1. open development tool(F12)
2. switch to network panel
3. when youtube.com get redirect(without page whole reload), network will capture a fetch called "player"
4. copy the content of "player" and save as "player.txt"
5. call this program with arg "parent folder of player.txt"
6. this program will download all format of that page's advertisement video
