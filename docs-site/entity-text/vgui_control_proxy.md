A `vgui_control_proxy` changes one control of a world screen, a [`vgui_screen`](vgui_screen.md), for every player when
you trigger it. It can change the text or value of the control, enable or disable it, show or hide it, or play an
animation.

## Attributes

- **Screen** (`screen`) - Names the `vgui_screen`
- **Control Name** (`controlname`) - Names the control in the screen's layout file. With "Play animation", it names
  the state group that keeps the animation for players who join later
    - If you leave this key empty with "Play animation", the animation plays once and isn't kept
- **Change** (`mode`) - Sets what it changes
    - Set the text (0, default) - It sets the text of a label or a button, or the value of a progress bar, an
      analog bar or a slider as a percentage from 0 to 100
    - Play animation (5) - It plays a sequence of the layout's `<panel name>_anims.txt`
- **Text / value / sequence** (`text`) - Sets the text, the value or the animation sequence, with up to 127
  characters. A `#Token` shows a translated text

## Notes

- The game keeps the latest change of each control, so players who join later see it too
- A [`trigger_changevalue`](trigger_changevalue.md) or a [`trigger_copyvalue`](trigger_copyvalue.md) can write its
  `text` key before the proxy is triggered

## See also

- [`vgui_screen`](vgui_screen.md) - the screen it changes
- [World screens](../features/world-screens.md) - layouts, controls and animations

## Changes since 1.38

- `vgui_control_proxy` is new
