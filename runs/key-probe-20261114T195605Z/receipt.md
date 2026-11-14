# Key probe receipt

UTC: 2026-11-14T19:56:04.210308+00:00
Key: OPENROUTER_API_KEY secret (value never logged). Probes: 1 token each.

## openai/gpt-6-sol (paid pair A)
- HTTP status: 403
- Response head: {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/caaf036f9da587a4277edb74bb5de247af6854075a31efc3e9a9441ea00d6d49 $10.00 of $10.00 used; does not reset.","code":403,"metadata":{"limit_source":"openrouter_key_limit","remedy_hint":"Raise or remove this API key's usage limit at https://openrouter.ai/settings/keys, or use a key without a limit.","scope":"key_limit","limit_usd":10,"spend_usd":10.002616816,"resets_at":null}}}

## mistralai/mistral-medium-3-5 (paid pair B)
- HTTP status: 403
- Response head: {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/caaf036f9da587a4277edb74bb5de247af6854075a31efc3e9a9441ea00d6d49 $10.00 of $10.00 used; does not reset.","code":403,"metadata":{"limit_source":"openrouter_key_limit","remedy_hint":"Raise or remove this API key's usage limit at https://openrouter.ai/settings/keys, or use a key without a limit.","scope":"key_limit","limit_usd":10,"spend_usd":10.002616816,"resets_at":null}}}

## nvidia/nemotron-3-ultra-550b-a55b:free (free control)
- HTTP status: 503
- Response head: {"error":{"message":"Provider returned error","code":503,"metadata":{"raw":"{\"message\":\"Service temporarily overloaded\",\"type\":\"Overloaded\",\"code\":503}","provider_name":"Nvidia","is_byok":false}},"user_id":"user_3KVtWazZjkNIOhQNotvtZBu88Ym"}
