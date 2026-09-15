# Silo: public URL after setup

For Silo builds using API v2, complete initial setup, then set `server.public_url`
in Silo's admin settings to the browser-facing origin of the main Silo web UI.
For the default HTTPS deployment, this is the resolved `silo_role_web_url`, for
example `https://silo.example.com`.

Use the actual external scheme and hostname (and port if nonstandard). Do not use
the container address, a WebSocket/API path, or the optional Jellyfin/Audiobookshelf
compatibility endpoint. If the external origin changes, update this setting too.

## Why this is needed

[Silo's API v2 migration](https://github.com/Silo-Server/silo-server/pull/1075)
replaced the `SILO_PUBLIC_URL` environment variable with the database-backed
`server.public_url` setting. The old environment variable no longer configures
that setting.

The API v2 WebSocket handshake checks the browser's `Origin` against the configured
public URL. When it is unset, Silo instead derives the origin from the request
host and trusted proxy scheme information. If that inference does not match the
browser origin, the handshake returns `403 origin refused`; the web client retries
and its realtime activity indicator may show a connection problem.

Setting the public URL explicitly avoids relying on scheme inference for this
check. It does not replace correct trusted-proxy configuration or fix unrelated
authentication, routing, or WebSocket forwarding problems.

## Existing installations and safety

- Existing API v2 installations that relied on `SILO_PUBLIC_URL` should configure
  `server.public_url` in the admin settings; this is not an automatic migration.
- The role does not edit Silo's database, reset settings, or overwrite an existing
  administrator-selected public URL.
- The setting is persisted in Silo's database and survives container recreation.
- Intentionally pinned pre-API-v2 builds that still need the old environment
  variable can retain it through the existing custom environment override:

  ```yaml
  silo_role_docker_envs_custom:
    SILO_PUBLIC_URL: "{{ lookup('role_var', '_web_url', role='silo') }}"
  ```

## Verification

Reload the web UI and inspect its `/api/v2/events/ws` connection in the browser's
network tools. A valid authenticated handshake should upgrade successfully and
stop repeatedly returning `403 origin refused`. Do not disable Origin checks or
use a wildcard-origin workaround.
