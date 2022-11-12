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

| Name        | Description                          | Type                          | Required |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **breakpoints** 

### Returns

| Name        | Description                                    | Type                          |
| ----------- | -----------------------------------------------| ----------------------------- |
| **state**   | The state of the async function                | Readable(T)                   |
| **is_ready**| Whether the async function is ready to execute | Readable(boolean)             |
| **is_loading**| Whether the async function is loading        | Readable(boolean)             |
| **error**   | The error of the async function                | Readable(unknown)             |
| **execute** | A function to execute the async function. It can accept a `delay` option to delay the execution and an `arg` option to pass an argument to the async function. | `function(delay?: number, ...args: any[])` |

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
