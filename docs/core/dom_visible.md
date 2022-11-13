---
title: DOM Visible
description: Reactive document.visibilityState 
demo_link: https://svelte.dev/repl/fa0a2df545c0403db7361617bb2e4deb?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {dom_visible} from "sveltecore"

    const visible = dom_visible()
</script>
```

## 👩‍💻API

### Returns

A subscribable store that contains the current visibility state.

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
