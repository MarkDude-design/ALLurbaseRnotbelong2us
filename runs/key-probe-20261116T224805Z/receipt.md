# Key probe receipt

UTC: 2026-11-16T22:48:02.991729+00:00
Key: OPENROUTER_API_KEY secret (value never logged). Probes: 1 token each.

## openai/gpt-6-sol (paid pair A)
- HTTP status: 200
- Response head: 
         
{"id":"gen-1794869283-wdu2qHCVptwtSfbzDm7H","object":"chat.completion","created":1794869283,"model":"openai/gpt-6-sol","provider":"OpenAI","system_fingerprint":null,"service_tier":"default","choices":[{"index":0,"logprobs":null,"finish_reason":"stop","native_finish_reason":"completed","message":{"role":"assistant","content":"OK","refusal":null,"reasoning":null}}],"usage":{"prompt_tokens":13,"completion_tokens":5,"total_tokens":18,"cost":0.000076,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.000076,"upstream_inference_prompt_cost":0.000026,"upstream_inference_completions_cost":0.00005},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":

## mistralai/mistral-medium-3-5 (paid pair B)
- HTTP status: 200
- Response head: 
         
{"id":"gen-1794869284-ZnJSmK3GDzRVuyxDdvbS","object":"chat.completion","created":1794869284,"model":"mistralai/mistral-medium-3-5","provider":"Mistral","system_fingerprint":null,"service_tier":"default","choices":[{"index":0,"logprobs":null,"finish_reason":"length","native_finish_reason":"length","message":{"role":"assistant","content":"OK","refusal":null,"reasoning":null}}],"usage":{"prompt_tokens":22,"completion_tokens":1,"total_tokens":23,"cost":0.0000405,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0000405,"upstream_inference_prompt_cost":0.000033,"upstream_inference_completions_cost":0.0000075},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0

## mistralai/mistral-small-3.2-24b-instruct (low-cost continuity candidate)
- HTTP status: 200
- Response head: {"id":"gen-1794869284-L94pzI147mA9araaZGDj","object":"chat.completion","created":1794869284,"model":"mistralai/mistral-small-3.2-24b-instruct","provider":"Venice","system_fingerprint":null,"service_tier":"default","choices":[{"index":0,"logprobs":null,"finish_reason":"length","native_finish_reason":"length","message":{"role":"assistant","content":"OK","refusal":null,"reasoning":null}}],"usage":{"prompt_tokens":10,"completion_tokens":1,"total_tokens":11,"cost":0.0000011875,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0000011875,"upstream_inference_prompt_cost":9.375e-7,"upstream_inference_completions_cost":2.5e-7},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens

## nvidia/nemotron-3-ultra-550b-a55b:free (free control)
- HTTP status: 200
- Response head: {"id":"gen-1794869285-CsBkRoBaqirc1Hld4QAz","object":"chat.completion","created":1794869285,"model":"nvidia/nemotron-3-ultra-550b-a55b:free","provider":"Nvidia","system_fingerprint":null,"service_tier":null,"choices":[{"index":0,"logprobs":null,"finish_reason":"length","native_finish_reason":"length","message":{"role":"assistant","content":null,"refusal":null,"reasoning":"The","reasoning_details":[{"type":"reasoning.text","text":"The","format":"unknown","index":0}]}}],"usage":{"prompt_tokens":23,"completion_tokens":1,"total_tokens":24,"cost":0,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0,"upstream_inference_prompt_cost":0,"upstream_inference_completions_cost":0},"completion_t
