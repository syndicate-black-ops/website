The Assassin is a quick fighter with a pistol and hand grenades, and on the hardest skill level it cloaks itself in a
fight.

## Attributes

- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Assassin's AI picks its animations
- **Ignore Friendly Damage** (`Ff`) - Sets whether damage from monsters on its side hurts it
    - No (0, default) - All damage hurts it
    - Yes (1) - Damage from monsters on its side doesn't hurt it

## In combat

The Assassin has 100 health, and each pistol shot deals 8 to 22 damage. It only cloaks itself when the server setting
`skill` is 3 (set in `server.cfg` or in the server console). Then it turns almost invisible while it stands on the
ground in a fight, and it shows again while it walks, runs, jumps or dies. With any other `skill` value, it is always
visible. The game sets its **Render Mode** and **FX Amount** itself, so the values you give these keys have no effect.
Players earn XP for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [monster_human_assassin on TWHL](https://twhl.info/wiki/page/monster_human_assassin) - the Half-Life entity

## Changes since 1.38

- Fixed Ignore Friendly Damage turning off on Feds, Heavy Weapons Feds, Fed Hunters, Assassins and Sentry Guns when
  the map gave another key after it. Every later key set it back to off. This was a bug in SBO 1.38
