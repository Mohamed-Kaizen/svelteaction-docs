---
title: Useragent
description:  Reactive useragent.
demo_link: https://svelte.dev/repl/d26439319c564b138fcc8cd609f33c28?version=3.53.1
---

# {{title}}

{{description}}

## 🎬 Usage

```html
<script>
    import {useragent} from "sveltecore"

    const {
        is_supported,
        mobile,
        architecture,
        model,
        platform,
        platform_version,
        bitness,
        brands
    } = useragent()
</script>
```

## 👩‍💻API

### Returns

| Name                 | Description                          | Type                            |
| -----------          | -------------------------------------| -----------------------------   |
| **is_supported**     | Is the userAgentData supported       | `Readable<boolean>`             |
| **mobile**           | Is the device mobile                 | `Readable<boolean>`             |
| **architecture**     | The device architecture              | `Readable<string>`              |
| **model**            | The device model                     | `Readable<string>`              |
| **platform**         | The device platform                  | `Readable<string>`              |
| **platform_version** | The device platform version          | `Readable<string>`              |
| **bitness**          | The device bitness                   | `Readable<number>`              |
| **brands**           | The device brands                    | `Readable<UserAgentDataBrand[]>`|


## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
