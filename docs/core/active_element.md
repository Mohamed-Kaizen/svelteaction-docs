---
title: Active Element
description: Reactive document.activeElement 
demo_link: https://svelte.dev/repl/1e16ce396c59454cb028efc2a0b6f1da?version=3.53.1
---

# {{title}}

{{description}}

## ð¬ Usage

```html
<script>
    import {active_element} from "sveltecore"

    const el = active_element()
</script>
```

## ð©âð»API

### Returns

A subscribable store that contains the current active element.

## ð§ª Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
