# pyEDSM – a Python Wrapper for EDSM’s API #

The current state might very well be the final one, depending on what I might 
need in the future for command-line usage.

This was born as supplemental scripts for my [VoiceAttack 
profiles](https://alternerdtive.github.io/VoiceAttack-profiles) and as I’ve had 
to make some plugins for that in the meantime anyway I will move all this to 
.Net for use in those.

tl;dr: if you want more features here, your best bet is to fork or open a pull 
request.

## Implementation Progress ##

- [x] Status
- [ ] Commander
- [ ] Logs
  - [ ] get-logs
  - [x] get-position
  - [ ] set-comment
  - [ ] get-comment
  - [ ] get-comments
- [ ] System
  - [x] bodies
  - [ ] estimated-value
  - [ ] stations
  - [ ] market
  - [ ] shipyard
  - [ ] outfitting
  - [ ] factions
  - [ ] traffic
  - [ ] deaths
- [ ] Systems
  - [x] system
  - [x] systems
  - [ ] sphere-systems
  - [ ] cube-systems
- [ ] Journal

~~Current goal is to implement most parts of the System and Systems API as well 
as some of the Commander and Logs API. Everything else is _not planned_ at the 
moment.~~ See above!

Throw money at me and I’ll do what you want :)

Whatever is currently implemented is likely to change on a whim until there’s 
a first release. You have been warned.

## Things You Probably Want to Use ##

Have a look at [`edsm/models.py`](edsm/models.py) or [my `elite-scripts` 
repo](https://github.com/alterNERDtive/elite-scripts) that I made this for. 
Basically you create a new `System`/`Commander` object (usually by name) and 
start using properties; that will query EDSM in the background.

Oh, the tests in `edsm/test_*.py` might be interesting, too.

## Things You Probably Don’t Want to Use ##

You can also find the raw API stuff in `edsm/*Api.py`. You probably don’t want 
to use that directly, but hey, all the power to you.

## Need Help / Want to Contribute? ##

If you run into any problems, please look at the 
[develop](https://github.com/alterNERDtive/pyEDSM/tree/develop) branch and see 
if it’s fixed there already.

If you have no idea what I was saying in that last paragraph and / or the things 
mentioned there don’t fix your problem, please [file an 
issue](https://github.com/alterNERDtive/pyEDSM/issues). Thanks! :)

You can also [say “Hi” on Discord](https://discord.gg/7wKEDDr) if that is your 
thing.
