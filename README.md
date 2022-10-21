# Svelte Action


<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://raw.githubusercontent.com/Mohamed-Kaizen/svelteaction-docs/main/docs/static/svelteaction2.png" alt="FastAPI"></a>
</p>

<p align="center" class="text-xl">
    <em class="text-2xl">Write less, Do more</em>
</p>

<p align="center">
<a href="https://www.npmjs.com/package/sveltecore" target="_blank">
    <img src="https://img.shields.io/npm/dm/sveltecore?color=50a36f&label=sveltecore">
</a>


<a href="https://www.npmjs.com/package/svelteshareds" target="_blank">
    <img src="https://img.shields.io/npm/dm/svelteshareds?color=50a36f&label=svelteshareds">
</a>


<a href="https://www.npmjs.com/package/svelteintegrations" target="_blank">
    <img src="https://img.shields.io/npm/dm/svelteintegrations?color=50a36f&label=svelteintegrations">
</a>

<a href="https://github.com/Mohamed-Kaizen/svelteaction-docs" target="_blank">
    <img src="https://img.shields.io/static/v1?label=functions&message=112&color=50a36f">
</a>

</p>

---
**Svelte Action** is a collection of utility functions, which help you build powerful app.

The key features are:

* **Type Strong 💪**: Written in TypeScript, with full TS docs.
* **Fast to code 🚀**: Increase the speed to develop features by about 200% to 300%.
* **Fewer bugs 🐞**: Reduce about 40% of human (developer) induced errors.
* **SSR Friendly 🕺**: Works perfectly with server-side.
* **Easy 💫**: Designed to be easy to use and learn. Less time reading docs.
* **Interactive demos 🎉** : Documentation of functions also come with interactive demos!.
* **Feature Rich  🌈**: 100+ functions for you to choose from.
* **Fully 🌳 shakeable**: Only take what you want.
* **⚙️ Flexible**:  Fully customizable, configurable event filters and targets.

## Installation


### Core

```bash
pnpm add -D sveltecore
```



### Shared

```bash
pnpm add -D svelteshareds
```



### Integrations

```bash
pnpm add -D svelteintegrations
```


## 🧪 Example

### Core

``` html
<script>
import {permission} from "sveltecore"

const { state, is_supported } = permission("geolocation", {controls: true})

</script>

<h1>Is supported is: {$is_supported}</h1>
<h1>state is: {$state}</h1>
```

### Shared

``` html
<script>
import {toggleable} from "svelteshareds"

const [value, toggle] = toggleable()

</script>

<h1>value is: {$value}</h1>

<button on:click="{() => toggle()}">Toggle</button>
```

### Integrations

``` html
<script>
import {jwt} from "svelteintegrations/jwt"

const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

const { header, payload } = jwt(token)

</script>

<h1>Header:</h1>
<h2>{JSON.stringify(header)}</h2>

<hr/>

<h1>Payload:</h1>
<h2>{JSON.stringify(payload)}</h2>
```

## 🙏 Thanks

This project is heavily inspired by the following awesome projects.

- [vueuse/vueuse](https://github.com/vueuse/vueuse/)
- [rayepps/radash](https://github.com/rayepps/radash)

## 📜 License

[MIT License](#License) © 2022-PRESENT [Mohamed Nesredin](https://github.com/mohamed-kaizen)
