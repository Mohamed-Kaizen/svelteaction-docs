---
title: Change Case
description: Wrapper for change-case. 
demo_link: https://svelte.dev/repl/9bee5a5d101948c9b5496eb9df31d2d4?version=3.52.0
---

# {{title}}

Wrapper for [change-case](https://github.com/blakeembrey/change-case).

## ⚡️ Prerequisites

- [x] Install the ***change-case*** package:

<div class="termy">

```console
$ pnpm add change-case

---> 100%
```

</div>

## 🎬 Usage

```html
<script>
    import {change_case} from "svelteintegrations/change_case"

    let value = "Svelte Action"
</script>

<h1>{change_case(value, "snakeCase")}</h1>

<input bind:value>

```

## 👩‍💻API

### Arguments

| Name        | Description                          | Type                          | Required |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **input**   | The string to convert                | string                        | Yes      |
| **type**    | The type of conversion to perform    | string                        | Yes      |

### Options

Read the [change-case documentation](https://github.com/blakeembrey/change-case#options) for more information.

| Name        | Description                          | Type                          | Default  |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **splitRegexp** | used to split into word segments | **RegExp**                    | None     |
| **stripRegexp** | used to remove extraneous characters | **RegExp**                | /[^A-Z0-9]/gi |
| **delimiter** | Value used between words           | **string**                    | " "      |
|**transform** | Function used to transform each word | **function**                 | None     |

### Returns

The converted string.

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
