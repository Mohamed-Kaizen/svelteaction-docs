---
title: Clipboard
description: Reactive Clipboard. 
demo_link: https://svelte.dev/repl/24808df5421e4ed4a9992552bd98cd7f?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
  import {clipboard} from "sveltecore"

    const { text, is_supported, copy, copied } = clipboard()
</script>
```

## 👩‍💻API

### Options

| Name        | Description                          | Type                       | Default    |
| ----------- | ------------------------------------ | ---------------------------| --------   |
| **read**    | Read clipboard                       | `boolean`                  | `false`    |
| **source**  | Copy from source                     | `Source`                   | `undefined`|
| **copied_during** | Milliseconds to reset state of `copied` store | `number`    | `1500`     |
| **legacy**  | Use legacy clipboard API             | `boolean`                  | `false`    |

### Returns

| Name        | Description                                | Type                               |
| ----------- | -------------------------------------------| -----------------------------      |
| **is_supported** | Is the browser support Clipboard API  | `Readable<boolean>`                |
| **text**    | Clipboard text                             | `Readable<string>`                 |
| **copied**  | Is the text copied                         | `Readable<boolean>`                |
| **copy**    | Copy text to clipboard                     | `(text: string) => Promise<void>`  |

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
