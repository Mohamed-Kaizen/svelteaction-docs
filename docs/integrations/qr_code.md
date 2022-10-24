---
title: QR Code
description: Wrapper for qrcode. 
demo_link: https://svelte.dev/repl/37c07f9e036249cfb53d90d6269c2772?version=3.52.0
---

# {{title}}

Wrapper for [qrcode](https://github.com/soldair/node-qrcode).

## ⚡️ Prerequisites

- [x] Install the ***qrcode*** package:

<div class="termy">

```console
$ pnpm add qrcode

---> 100%
```

</div>

## 🎬 Usage

```html
<script>
    import {qr_code} from "svelteintegrations/qr_code"

    let value = 'world';

    $: ({output, pending, error} = qr_code(value))
</script>

<img src="{$output}" alt="qrcode" />

<br/>

<p>Pending: {$pending}</p>

<p>Error: {$error}</p>

<br/>

<input bind:value />

```

## 👩‍💻API

### Arguments

| Name        | Description                          | Type                          | Required |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **text**    | The text to encode                   | `string`                      | Yes      |

### Options

Read the [qrcode documentation](https://github.com/soldair/node-qrcode#options-9)

### Returns

| Name        | Description                          | Type                          |
| ----------- | ------------------------------------ | ----------------------------- |
| **output**  | The base64 encoded image             | `Readable<string>`            |
| **pending** | When the image is being generated    | `Readable<boolean>`           |
| **error**   | When an error occurs                 | `Readable<string | unknown>`  |

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
