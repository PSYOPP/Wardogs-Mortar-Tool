# Mortar Tool

Artillery and mortar calculator for the game Wardogs. Quickly find the
distance and direction to send artillery down range.

![Wardogs](https://img.shields.io/badge/game-Wardogs-orange)

## What it does

Paste your gun position and target position (straight from the in-game
*Mark Coordinates* chat line) and the tool gives you:

- **RNG** - range to target in metres
- **DIR** - bearing in degrees, clockwise from map North
- A compass tape, RNG ladder, and relative-position mini map
- A badge telling you which weapon can make the shot

Two weapon modes:

| Mode | Envelope |
|---|---|
| **L81 Mortar** | up to ~700 m |
| **Artillery Tank** | 750 m minimum, ~2,700 m maximum |

In artillery mode the mini map grows to fit the shot. History entries can be
labeled with symbols and reloaded with a click.

## Quick tutorial

1. **Mark your gun.** Open the map and zoom all the way in on your gun
   position (zoomed out you lose decimal precision). Right-click it and
   choose *Mark Coordinates*; the chat box opens with the numbers.
2. **Move them over.** Press `Ctrl+A` to select all, then `Ctrl+X` to cut
   the coordinates onto your clipboard, and paste into the
   **Gun position** box.
3. **Mark your target.** Same routine: zoom in, *Mark Coordinates*,
   `Ctrl+A`, `Ctrl+X`, paste into the **Target position** box.
4. **Read the shot.** The tool shows RNG (metres), DIR (degrees clockwise
   from map North), and a badge telling you which weapon can reach.
5. **Fire.** In game: middle-click the target on the map to drop the white
   diamond, centre the diamond in your view, set the RNG slider to the
   calculated range, and fire. Between two notches? Split the difference.

Tips:

- Paste straight from chat; any extra text around the numbers is ignored.
- Both pairs pasted into one box? They split automatically into gun and target.
- Mini map looks mirrored? Tick *Map Y axis points down*.
- Label past shots in History with a symbol and reload them with a click.

## The math

Plain Pythagoras on map coordinates. One map unit = 100 m:

```
range = sqrt(dX^2 + dY^2) x 100
bearing = atan2(dX, dY)
```

The same math works for both guns; only the usable range envelope differs.

## Running

Download `Mortar_Tool_Final.zip` from
[Releases](https://github.com/PSYOPP/Wardogs-Mortar-Tool/releases), unzip,
and run `Mortar_Tool_Final.exe`. Requires Windows 10/11 with WebView2
(preinstalled on Windows 11).

### Building from source

```
pip install pywebview pyinstaller
pyinstaller --noconfirm --clean --name Mortar_Tool_Final --windowed --onedir --add-data "Mortar_Tool.html;." Mortar_Tool.py
```

## Files

- `Mortar_Tool.html` - the whole app (single file, no dependencies)
- `Mortar_Tool.py` - desktop launcher (pywebview window)

## Credits

Math and range figures from the Wardogs community (SC Haulers' tutorial,
SwoleBenji's video, wardogshub and wardogs.zone calculators).
