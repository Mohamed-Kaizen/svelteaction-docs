---
title: Preferred Reduced Motion
description: Reactive prefers-reduced-motion media query.
demo_link: https://svelte.dev/repl/e940527d0dd14e95beefd07af58b83b7?version=3.53.1
---

# {{title}}

{{description}}

## ð¬ Usage

```html
<script>
    import {preferred_reduced_motion} from "sveltecore"

    const motion = preferred_reduced_motion()
</script>
```

## ð©âð»API

### Returns

A subscribable store with the value of the prefers-reduced-motion media query.

## ð§ª Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
