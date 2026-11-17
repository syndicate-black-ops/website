A `trigger_changeparent` gives entities a new parent to move with when you trigger it, or takes their parent away.

## Attributes

- **Name** (`targetname`) - Triggering the entity by this name changes the parent. See
  [Common keys](common-keys.md#targetname)
- **Entity to re-parent** (`target`) - Names the entities that get the new parent, and every entity with this name
  changes. It also takes a name ending in `*`, an alias (`*name`), a member of an [`info_group`](info_group.md),
  `!activator` and `!caller`. See
  [What * means in a name](../guide/entity-triggering.md#what-star-means) for more details.
  Here `!caller` is the `trigger_changeparent` itself
- **New parent** (`m_iszNewParent`) - Names the new parent, which is the first entity with this name. It takes the
  same kinds of names as **Entity to re-parent**. A name ending in `.1` to `.4` puts a sprite or a model that isn't
  solid on that attachment point of the parent's model
    - If you leave this key empty, the entities stop where they are and don't move with anything after that

## Notes

- Each entity keeps its place and angles at the moment of the change. After that, it moves with the new parent from
  where it is
- If no entity has the name in **New parent**, nothing changes. With `developer 1` set in the console, the console
  shows a message about it
- An entity that can't move with a parent, such as a monster or a `func_train`, gets no parent. With `developer 1`
  set in the console, the console says why
- A [`trigger_changevalue`](trigger_changevalue.md) on the `movewith` key of an entity does the same

## See also

- [Moving objects](../features/moving-objects.md) - how Move With works, with examples
- [`trigger_changetarget`](trigger_changetarget.md) - changes the **Target** of an entity in the same way

## Changes since 1.38

- `trigger_changeparent` is new in SBO 2.1.0
