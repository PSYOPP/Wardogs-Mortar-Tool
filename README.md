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
