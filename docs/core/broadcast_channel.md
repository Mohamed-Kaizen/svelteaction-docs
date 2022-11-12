---
title: Broadcast Channel
description: Reactive Broadcast Channel. 
demo_link: https://svelte.dev/repl/839a0d215a45493daec15db5421c1e3c?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {broadcast_channel} from "sveltecore"

    const {data, post, error} = broadcast_channel()


    $: if ($data) alert($data)

    let value = "HI"
</script>

<h1>Open new Tab, and start a broadcaset :)</h1>
<input type="text" bind:value />

<button on:click="{() => post(value)}">Post</button>
```

## 👩‍💻API

### Options

| Name        | Description                          | Type                          | Default  |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **name**    | The name of the broadcast channel    | `string`                      | `""`     |

### Returns

| Name        | Description                                    | Type                          |
| ----------- | -----------------------------------------------| ----------------------------- |
| **is_supported** | Is the browser support broadcast channel  | `Readable<boolean>`           |
| **is_closed**   | Is the broadcast channel closed            | `Readable<boolean>`           |
| **data**    | The data from the broadcast channel            | `Readable<any | undefined>`   |
| **error**   | The error from the broadcast channel           | `Readable<Event | null>`      |
| **close**   | Close the broadcast channel                    | `() => void`                  |
| **post**    | Post a function to the broadcast channel       | `(data: any) => void`         |
| **channel** | The broadcast channel                          | `Readable<BroadcastChannel | undefined>`|


## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
