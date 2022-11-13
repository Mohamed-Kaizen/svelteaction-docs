---
title: Breakpoints
description: Reactive viewport breakpoints. 
demo_link: https://svelte.dev/repl/6a1576a9bff349af99d0f19be7bb9ceb?version=3.52.0
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {breakpoints} from "sveltecore"

    const breakpoint = breakpoints({
        tablet: 640,
        laptop: 1024,
        desktop: 1280,
    })

    const laptop = breakpoint.between('laptop', 'desktop')
</script>

<h1>{$laptop}</h1>
```

## 👩‍💻API

### Arguments

| Name            | Description                          | Type                     | Required |
| --------------- | ------------------------------------ | ------------------------ | -------- |
| **breakpoints** | The breakpoints to use.              | `Record<string, number>` | Yes      |

### Returns

| Name        | Description                                    | Type                          |
| ----------- | -----------------------------------------------| ----------------------------- |
| **greater** | A function that checks if the breakpoint is greater than the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **greater_or_equal** | A function that checks if the breakpoint is greater than or equal to the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **smaller** | A function that checks if the breakpoint is smaller than the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **smaller_or_equal** | A function that checks if the breakpoint is smaller than or equal to the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **between** | A function that checks if the breakpoint is between the current breakpoint. | `(breakpoint: string, breakpoint2: string) => Readable<boolean>` |
| **is_greater**| A function that checks if the breakpoint is greater than the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **is_greater_or_equal** | A function that checks if the breakpoint is greater than or equal to the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **is_smaller** | A function that checks if the breakpoint is smaller than the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **is_smaller_or_equal** | A function that checks if the breakpoint is smaller than or equal to the current breakpoint. | `(breakpoint: string) => Readable<boolean>` |
| **is_in_between** | A function that checks if the breakpoint is between the current breakpoint. | `(breakpoint: string, breakpoint2: string) => Readable<boolean>` |

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
