---
title: FPS
description: Reactive FPS (frames per second).
demo_link: https://svelte.dev/repl/f8b7aafc166243318597ee6655159a10?version=3.53.1
---

# {{title}}

{{description}}

## ð¬ Usage

```html
<script>
    import {fps} from "sveltecore"

    const f = fps()
</script>
```

## ð©âð»API

### Options

| Name        | Description                          | Type                          | Default  |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **every**   | Calculate the FPS on every x frames. | `number`                      | `10`     |

### Returns

A subscribable store that updates with the current FPS.

## ð§ª Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
