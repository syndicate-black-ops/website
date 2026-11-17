A `trigger_changetarget` changes the **Target** of another entity when you trigger it.

## Attributes

- **Target** (`target`) - Names the entity whose target changes, which is the first entity with this name. With a
  name that ends in `*`, it is the first entity whose name starts with the rest
- **New Target** (`m_iszNewTarget`) - Sets the new **Target** of that entity. A monster also stops following the path
  it was on

## Notes

- With **Delay before trigger**, the entity sets the new target that many seconds after the trigger. Another trigger
  while a change is waiting does nothing
- The entities named in **KillTarget** are removed when the change happens, at once or after the delay

## See also

- [`trigger_changevalue`](trigger_changevalue.md) - changes any key of an entity
- [trigger_changetarget on TWHL](https://twhl.info/wiki/page/trigger_changetarget) - the Half-Life entity

## Changes since 1.38

- Fixed `trigger_changetarget` ignoring its Delay and its Kill target. It changed the target at once and never read
  either key
