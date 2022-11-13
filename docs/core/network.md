---
title: Network
description: Network status. 
demo_link: https://svelte.dev/repl/ae4adc87b9524abe88a0ea8f0bb15fac?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {network} from "sveltecore"

    const {
        is_supported,
        online,
        offline_at,
        online_at,
        downlink,
        downlink_max,
        effective_type,
        rtt,
        save_data,
        type,
    } = network()
</script>
```

## 👩‍💻API

### Returns

| Name             | Description                                | Type                         |
| -----------      | -------------------------------------------| -----------------------------|
| **is_supported** | Is the Network Information API supported   | `Readable<boolean>`          |
| **online**       | Is the device online                       | `Readable<boolean>`          |
| **offline_at**   | Timestamp of when the device went offline  | `Readable<number | undefined>`|
| **online_at**    | Timestamp of when the device went online   | `Readable<number | undefined>`|
| **downlink**     | Downlink speed estimate in megabits per second | `Readable<number | undefined>`|
| **downlink_max** | Maximum downlink speed estimate in megabits per second | `Readable<number | undefined>`|
| **effective_type** | Effective connection type | `Readable<NetworkEffectiveType | undefined>`|
| **rtt**          | Round-trip time estimate in milliseconds | `Readable<number | undefined>` |
| **save_data**    | Is the device in a "save data" mode | `Readable<boolean | undefined>`|
| **type**         | Connection type | `Readable<NetworkType>`                         |


## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
