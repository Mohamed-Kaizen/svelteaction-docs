---
title: Drop Zone
description: Drop Zone area, where you can drop files. 
demo_link: https://svelte.dev/repl/b2af83ab9be543e39074f3b4b6418ee7?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {drop_zone} from "sveltecore"

    let is_over_drop_zone = false

    let files_data = []

    function on_drop(files) {
        files_data = []
        if (files) {
            files_data = files.map((file) => ({
                name: file.name,
                size: file.size,
                type: file.type,
                last_modified: file.lastModified,
            }))
        }
    }

    function on_drop_zone(el) {
        const result = drop_zone(el, on_drop)
        result.subscribe((x) => {
            is_over_drop_zone = x
        })
    }

</script>
<div use:on_drop_zone></div>
```

## 👩‍💻API

### Arguments

| Name        | Description                          | Type                            | Required|
| ----------- | ------------------------------------ | --------------------------------| --------|
| **target**  | DOM element to attach drop zone to   | `HTMLElement`                   | Yes     |
| **on_drop** | Callback function to handle drop     | `(files: File[] | null) => void`| Yes     |

### Returns

A subscribable store that contains the current drop zone state.

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
