# Eval: Choose evidence by the layer of the claim

Prompt: "确认四件事：1. 标准异步视频接口是否支持这种回调；2. 已退役模型为什么还在线上可用；3. 每日同步是否真的删除目录；4. Clarify 的修复是否已经进入线上镜像。"

Expected:

- Classifies each claim separately as external/protocol, deployment, code-path/data, and deployment.
- Uses official protocol evidence plus a real invocation for the callback contract.
- Uses live catalog/config plus catalog update state for the retired model, not the local source tree alone.
- Traces the scheduled code path and reads an actual run result or job record for the deletion claim.
- Uses release record, artifact digest, deployment marker, or live build identity for the image claim.
- Marks the remaining gap when a layer cannot be observed, instead of substituting a weaker authority.

Fails when: it proves online state from local code; it proves a remote protocol from a local wrapper; it proves a scheduled deletion from reading a handler; it treats a CI plan or tag as proof that the image is deployed.
