# AI Plays Pokemon

This project is my attempt to make AI (Gemini, specifically) play pokemon, and maybe complete.

So I start with the aim of making Gemini play the game, or atleast specific parts of it. Based on the last benchmarks, it performed poorly
, and it just spams AAAAA whenever it gets a chance (as we all Pokemon players do, right?) and nicknames it's starter AAAAAAAAA!?

> Name the Pokemon AAAAAAAA
>
> &mdash; _Gemini, 2025_

The current loop starts with optionally going through the intro sequence (specifically tailored for Pokemon Emerald, but maybe adapted to others),
then on subsequent runs, advance the main menu, and then it enters the loop by

1. Taking a screenshot
2. Send it to Gemini
3. Receiving a sequence of button presses and a description of what to do.
4. Performing the presses with a short wait inbetween
5. Waiting for a longer period
6. Loop again

The program is currently tailored to my setup, and will (mostly) probably not function on your device.

1. A Linux System
2. `mgba-qt` installed and on `$PATH`
3. `dotool` installed with `dotoold` and `dotoolc` on `$PATH`
4. Pokemon Emerald ROM (legally obtained!) in the same directory as the script.
5. Make sure pressing `F9` takes a screenshot in `mgba` (it maybe `Fn` locked or something)
6. Your Google AI API key in the `.env` file
7. And yes, keymap for `mgba`, match with what is in `helpers.py`

I may try to improve this in future. This is just an Experiment

**Legal Disclaimer**: Pokemon is a registered trademark of Nintendo/Game Freak Inc. This project is for educational purposes only. You must legally own a copy of the Pokemon game to obtain ROM files. Downloading ROMs for games you don't own is illegal in most jurisdictions. The authors of this project do not condone or promote piracy.
