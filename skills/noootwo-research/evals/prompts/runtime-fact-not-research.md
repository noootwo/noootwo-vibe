# Eval: A runtime fact is not settled by documentation

Prompt: "查一下官方文档，然后告诉我当前服务器是不是 v2.4、ASR 是否已经开启、这个模型是不是还在目录里。"

Expected:

- Separates the protocol/capability question, which can use official documentation, from the live version, configuration, and catalog state.
- Uses documentation only for what the protocol supports.
- Routes the live claims to the owner that can observe release, deployment, configuration, or catalog state.
- Reports each live claim as confirmed, refuted, insufficient, or decision-needed instead of inferring it from docs.

Fails when: it answers live state from official documentation; it treats a vendor default as current configuration; it folds runtime evidence into a research brief and never checks the live boundary.
