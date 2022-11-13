---
title: File Dialog
description: Reactive File Dialog. 
demo_link: https://svelte.dev/repl/2ba9641536ce4478a87db2e8c0cde5f8?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {file_dialog} from "sveltecore"

    const { files, open, reset } = file_dialog()
</script>
```

## 👩‍💻API

### Options

| Name         | Description                          | Type                       | Default    |
| -----------  | ------------------------------------ | ---------------------------| --------   |
| **multiple** | Allow multiple files to be selected  | `boolean`                  | `false`    |
| **accept**   | File types to accept                 | `string`                   | `*`        |

### Returns

| Name        | Description                                | Type                               |
| ----------- | -------------------------------------------| -----------------------------      |
| **files**   | Array of selected files                    | `Readable<File[]>`                 |
| **open**    | Open the file dialog                       | `() => void`                       |
| **reset**   | Reset the file dialog                      | `() => void`                       |

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
