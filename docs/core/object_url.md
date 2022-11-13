---
title: Object Url
description: URL representing an object.
demo_link: https://svelte.dev/repl/4a6efeadad944a79934ad4ed79fb5ff2?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {object_url} from "sveltecore"

    let file = undefined

    const onFileChange = (e) => {
        const target = e.target
        const files = target.files
        file = files && files.length > 0 ? files[0] : undefined
    }

    $: url = object_url(file)
</script>
<input type="file" on:change="{onFileChange}" />

{url ? url : ""}
```

## 👩‍💻API

### Arguments

| Name        | Description                          | Type                            | Required|
| ----------- | ------------------------------------ | --------------------------------| --------|
| **object**  | Object to create URL for             | `Blob` or `MediaSource`         | Yes     |

### Returns

A URL representing the object.

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
