---
title: Preferred Contrast
description: Reactive prefers-contrast media query.
demo_link: https://svelte.dev/repl/9644e3f62b5641f3b0a82d78ecc40293?version=3.53.1
---

# {{title}}

{{description}}

## ð¬ Usage

```html
<script>
    import {preferred_contrast} from "sveltecore"

    const contrast = preferred_contrast()
</script>
```

## ð©âð»API

### Returns

A subscribable store with the value of the prefers-contrast media query.

## ð§ª Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
