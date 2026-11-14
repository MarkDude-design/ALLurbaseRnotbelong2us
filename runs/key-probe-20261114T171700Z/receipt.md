# Key probe receipt

UTC: 2026-11-14T17:16:59.757799+00:00
Key: OPENROUTER_API_KEY secret (value never logged). Probes: 1 token each.

## openai/gpt-6-sol (paid pair A)
- HTTP status: 403
- Response head: {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/caaf036f9da587a4277edb74bb5de247af6854075a31efc3e9a9441ea00d6d49 $10.00 of $10.00 used; does not reset.","code":403,"metadata":{"limit_source":"openrouter_key_limit","remedy_hint":"Raise or remove this API key's usage limit at https://openrouter.ai/settings/keys, or use a key without a limit.","scope":"key_limit","limit_usd":10,"spend_usd":10.002616816,"resets_at":null}}}

## mistralai/mistral-medium-3-5 (paid pair B)
- HTTP status: 403
- Response head: {"error":{"message":"Key limit exceeded (total limit). Manage it using https://openrouter.ai/workspaces/default/keys/caaf036f9da587a4277edb74bb5de247af6854075a31efc3e9a9441ea00d6d49 $10.00 of $10.00 used; does not reset.","code":403,"metadata":{"limit_source":"openrouter_key_limit","remedy_hint":"Raise or remove this API key's usage limit at https://openrouter.ai/settings/keys, or use a key without a limit.","scope":"key_limit","limit_usd":10,"spend_usd":10.002616816,"resets_at":null}}}

## nvidia/nemotron-3-ultra-550b-a55b:free (free control)
- HTTP status: 200
- Response head: 
         
{"id":"gen-1794676619-OS8PurximbT4x5mWb91B","object":"chat.completion","created":1794676619,"model":"nvidia/nemotron-3-ultra-550b-a55b:free","provider":"Nvidia","system_fingerprint":null,"service_tier":null,"choices":[{"index":0,"logprobs":null,"finish_reason":"length","native_finish_reason":"length","message":{"role":"assistant","content":null,"refusal":null,"reasoning":"The","reasoning_details":[{"type":"reasoning.text","text":"The","format":"unknown","index":0}]}}],"usage":{"prompt_tokens":23,"completion_tokens":1,"total_tokens":24,"cost":0,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0,"upstream_inference_prompt_cost":0,"upstream_inference_completions_cost":0},"c
