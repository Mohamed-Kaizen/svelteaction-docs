---
description: A collection of utility functions, which help you build powerful app. 
---

# Svelte Action

<p align="center">

<svg  role="img"  height="17rem" 
	 viewBox="0 0 595.28 841.89">
<polygon style="fill:#5AC4BE;" points="491.68,276.44 418.67,175.1 358.67,276.49 183.17,276.55 124.77,174.88 82.63,246.7 124.85,174.73 
	418.51,174.86 "/>
<polygon style="fill:#5C499D;" points="183.17,276.55 65.1,276.59 82.63,246.7 124.77,174.88 "/>
<polygon style="fill:#4480C2;" points="271.55,430.43 212.51,532.4 64.95,276.84 65.1,276.59 183.17,276.55 "/>
<polygon style="fill:#EE3670;" points="491.68,276.44 358.67,276.49 418.67,175.1 "/>
<polygon style="fill:#F68B60;" points="491.86,276.69 425.82,392.19 358.59,276.62 358.67,276.49 491.68,276.44 "/>
<polygon style="fill:#54C3BA;" points="491.26,555.42 372.48,555.42 285.81,404.55 344.6,302.87 "/>
<polygon style="fill:none;" points="492.43,557.44 432.74,660.31 491.75,556.28 "/>
<polygon style="fill:#5C489D;" points="491.75,556.28 432.74,660.31 372.48,555.42 491.26,555.42 "/>
<polygon style="fill:#4480C2;" points="432.74,660.31 432.6,660.55 140.01,660.22 65.2,555.42 65.22,555.42 139.88,660.01 198.5,555.42 
	372.48,555.42 "/>
<polygon style="fill:none;" points="492.24,555.42 491.75,556.28 491.26,555.42 "/>
<polygon style="fill:#F68A5E;" points="198.5,555.42 139.88,660.01 65.22,555.42 "/>
<polygon style="fill:#EE3770;" points="198.51,555.4 198.5,555.42 65.22,555.42 65.03,555.16 131.67,442.71 "/>
</svg>

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

=== "Core"

	<div class="termy">

	```console
	$ pnpm add -D sveltecore

	---> 100%
	```

	</div>


=== "Shared"

	<div class="termy">

	```console
	$ pnpm add -D svelteshareds

	---> 100%
	```

	</div>


=== "Integrations"

	<div class="termy">

	```console
	$ pnpm add -D svelteintegrations

	---> 100%
	```

	</div>

## 🧪 Example

=== "Core"

    ``` html
	<script>
		import {permission} from "sveltecore"

		const { state, is_supported } = permission("geolocation", {controls: true})

	</script>

	<h1>Is supported is: {$is_supported}</h1>
	<h1>state is: {$state}</h1>
    ```

=== "Shared"

    ``` html
	<script>
		import {toggleable} from "svelteshareds"

		const [value, toggle] = toggleable()

	</script>

	<h1>value is: {$value}</h1>

	<button on:click="{() => toggle()}">Toggle</button>
    ```

=== "Integrations"

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