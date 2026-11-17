import DefaultAdmonitionTypes from '@theme-original/Admonition/Types';
import AdmonitionTypeTodo from "./Type/Todo";
import AdmonitionTypeBug from "./Type/Bug";

const AdmonitionTypes = {
    ...DefaultAdmonitionTypes,
    'todo': AdmonitionTypeTodo,
    'bug': AdmonitionTypeBug,
}

export default AdmonitionTypes;
