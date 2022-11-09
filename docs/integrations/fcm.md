---
title: Fcm
description: Wrapper for firebase cloud messaging. 
---

# {{title}}

Wrapper for [firebase cloud messaging](https://firebase.google.com/docs/cloud-messaging).

## ⚡️ Prerequisites

- [x] Install the ***firebase*** package:

<div class="termy">

```console
$ pnpm add firebase

---> 100%
```

</div>

## 🎬 Usage

```html
<script>
    import { initializeApp } from "firebase/app"
    import {fcm} from "svelteintegrations/fcm"

    const config = {
        ...
    }

    const app = initializeApp(config)

    const { token, error, is_supported, messaging, on_message } = fcm(app)

</script>

```

## 👩‍💻API

### Arguments

| Name           | Description                          | Type                     | Required |
| -------------- | ------------------------------------ | -------------------------| -------- |
| **firebase**   | Firebase app instance.               | `firebase.app.App`       | Yes      |

### Options

| Name        | Description                          | Type                          | Default  |
| ----------- | ------------------------------------ | ----------------------------- | -------- |
| **vapid_key** | The public vapid key to use for push notifications. | **string** | `No default` |
| **sw_path** | The url path to the service worker file. | **string** | `No default` |

### Returns

| Name        | Description                              | Type                          |
| ----------- | ---------------------------------------- | ----------------------------- |
| **token**   | The token to use for push notifications. | `Readable<string>`            |
| **error**   | The error if any.                        | `Readable<Error>`             |
| **is_supported** | Whether push notifications are supported. | `Readable<boolean>`     |
| **messaging** | The firebase messaging instance.        | `Readable<firebase.messaging.Messaging>` |
| **on_message** | The function to call when a message is received. | `fn: (payload: unknown) => void`       |