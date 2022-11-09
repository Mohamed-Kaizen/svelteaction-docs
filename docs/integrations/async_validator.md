---
title: Async Validator
description: Wrapper for async-validator. 
demo_link: https://svelte.dev/repl/1779dc6afb884f799ef82ed7895e584d?version=3.52.0
---
# {{title}}

Wrapper for [async-validator](https://github.com/yiminghe/async-validator).

## ⚡️ Prerequisites

- [x] Install the ***async-validator*** package:

<div class="termy">

```console
$ pnpm add async-validator

---> 100%
```

</div>

## 🎬 Usage

```html
<script>
    import {async_validator} from "svelteintegrations/async_validator"

    const form = { email: "", name: "", age: "" }

    const rules = {
        name: {
            type: "string",
            min: 5,
            max: 20,
            required: true,
        },
        age: {
            type: "number",
            required: true,
        },
        email: [
            {
                type: "email",
                required: true,
            },
        ],
    }

    const { errors, error_info, error_fields, pass, finished } = async_validator(
        form,
        rules
    )
</script>

```

## 👩‍💻API

### Arguments

| Name        | Description                          | Type                          | Required |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **value**   | The value to be validated.           | `object`                      | `true`   |
| **rules**   | The rules to validate the value.     | `Rules` from `async-validator`| `true`   |

### Options

Read the [async-validator](https://github.com/yiminghe/async-validator#options) documentation for more information.

### Returns

| Name        | Description                                 | Type                          |
| ----------- | ------------------------------------------- | ----------------------------- |
| **errors**  | The errors of the validation.               | `{field: string, message: string, fieldValue: any}[]`                                                                      |
| **error_info** | The error information of the validation. | `Error`                       |
| **error_fields** | The error fields of the validation.    | `object`                      |
| **pass** | The validation result.                         | `Readable<boolean>`                                                                         |
| **finished** | The validation finished.                   | `Readable<boolean>`                                                                         |

## 🧪 Playground

<iframe class="h-120 w-full" src="{{demo_link}}"></iframe>
