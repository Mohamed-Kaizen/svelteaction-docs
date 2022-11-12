---
title: Async State
description: Reactive async state. 
demo_link: https://svelte.dev/repl/65f10b7c54c94715929c783deb9647c3?version=3.52.0
---

# {{title}}

{{description}}


## 🎬 Usage

```html
<script>
    import {async_state} from "sveltecore"

   function my_async_function() {
        ...

        return "some result"
    }

    const { state } = async_state(my_async_function, "initial state")
</script>

<h1>{$state}</h1>

```

## 👩‍💻API

### Arguments

| Name        | Description                          | Type                          | Required |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **promise** | The promise to be resolved           | `Promise`                     | Yes      |
| **initial_state** | The initial state, used until the first evaluation finishes | `any` | Yes |

### Options

| Name        | Description                          | Type                          | Default  |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **delay** |  Delaying the executing of the promise, if `immediate` is true. In milliseconds. | `number`    | `0`      |
| **immediate** |  If true, the promise will be executed immediately. | `boolean`    | `true`   |
| **reset_on_execute** |  Sets the state to initial_state before executing the promise. | `boolean`    | `true`   |
| **throw_error** |  An error is thrown when executing the execute function. | `boolean`    | `false`   |
| **on_error** |  Callback when error is caught. | `function`    | `null`   |

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
