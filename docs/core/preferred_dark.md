---
title: Preferred Dark
description: Reactive dark theme preference.
demo_link: https://svelte.dev/repl/193511b8894043d8b19b5108a31dbeb4?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {preferred_dark} from "sveltecore"

    const dark = preferred_dark()
</script>
```

## 👩‍💻API

### Returns

A subscribable store with the value of the prefers-color-scheme media query.

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
