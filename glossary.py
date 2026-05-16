"""Glossary: maps concepts/acronyms to authoritative, free, paywall-free
explainer URLs. Used by tools/linkify.py.

Order matters — longer / more-specific phrases come first so they are
matched and linkified before shorter substrings collide (e.g.
"Mixture-of-Experts" before "MoE").

All URLs verified to return HTTP 200 with no paywall as of build time.
"""

# (phrase, url) — phrase is matched literally (case-sensitive but
# anchored at word boundaries by the linkifier). Insertion happens at
# most ONCE per chapter for a given URL.
GLOSSARY: list[tuple[str, str]] = [
    # ---- Architecture / building blocks
    ("Mixture-of-Experts", "https://en.wikipedia.org/wiki/Mixture_of_experts"),
    ("State-space models", "https://en.wikipedia.org/wiki/State-space_model"),
    ("Vision Transformer", "https://en.wikipedia.org/wiki/Vision_transformer"),
    ("self-attention", "https://en.wikipedia.org/wiki/Attention_(machine_learning)"),
    ("transformer", "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"),
    ("softmax", "https://en.wikipedia.org/wiki/Softmax_function"),
    ("backpropagation", "https://en.wikipedia.org/wiki/Backpropagation"),

    # ---- Models / families
    ("BERT", "https://en.wikipedia.org/wiki/BERT_(language_model)"),
    ("GPT-3", "https://en.wikipedia.org/wiki/GPT-3"),
    ("Llama", "https://en.wikipedia.org/wiki/Llama_(language_model)"),
    ("Mistral", "https://en.wikipedia.org/wiki/Mistral_AI"),
    ("Phi series", "https://en.wikipedia.org/wiki/Phi_(language_model)"),
    ("Whisper", "https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)"),
    ("AlphaFold", "https://en.wikipedia.org/wiki/AlphaFold"),
    ("GitHub Copilot", "https://en.wikipedia.org/wiki/GitHub_Copilot"),
    ("CLIP", "https://web.archive.org/web/2026/https://openai.com/index/clip/"),

    # ---- Training / data
    ("Byte-Pair Encoding", "https://en.wikipedia.org/wiki/Byte_pair_encoding"),
    ("BPE", "https://en.wikipedia.org/wiki/Byte_pair_encoding"),
    ("AdamW", "https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam"),
    ("bfloat16", "https://en.wikipedia.org/wiki/Bfloat16_floating-point_format"),
    ("bf16", "https://en.wikipedia.org/wiki/Bfloat16_floating-point_format"),
    ("fp16", "https://en.wikipedia.org/wiki/Half-precision_floating-point_format"),
    ("FLOPs", "https://en.wikipedia.org/wiki/FLOPS"),

    # ---- Core concepts
    ("scaling laws", "https://en.wikipedia.org/wiki/Neural_scaling_law"),
    ("autoregressive", "https://en.wikipedia.org/wiki/Autoregressive_model"),
    ("in-context learning", "https://en.wikipedia.org/wiki/In-context_learning"),
    ("word embeddings", "https://en.wikipedia.org/wiki/Word_embedding"),
    ("n-gram", "https://en.wikipedia.org/wiki/N-gram"),
    ("recurrent", "https://en.wikipedia.org/wiki/Recurrent_neural_network"),

    # ---- Post-training / alignment
    ("RLHF", "https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback"),
    ("Supervised fine-tuning", "https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)"),
    ("AI alignment", "https://en.wikipedia.org/wiki/AI_alignment"),

    # ---- Reasoning
    ("Chain-of-thought", "https://en.wikipedia.org/wiki/Chain-of-thought_prompting"),

    # ---- Retrieval
    ("Retrieval-augmented generation", "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"),
    ("RAG", "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"),
    ("Vector DBs", "https://en.wikipedia.org/wiki/Vector_database"),
    ("cosine similarity", "https://en.wikipedia.org/wiki/Cosine_similarity"),

    # ---- Compression / serving
    ("Quantization", "https://en.wikipedia.org/wiki/Quantization_(signal_processing)"),
    ("Knowledge distillation", "https://en.wikipedia.org/wiki/Knowledge_distillation"),
    ("Distillation", "https://en.wikipedia.org/wiki/Knowledge_distillation"),
    ("Speculative decoding", "https://en.wikipedia.org/wiki/Speculative_decoding"),

    # ---- Multimodal / generation
    ("diffusion", "https://en.wikipedia.org/wiki/Diffusion_model"),

    # ---- Evaluation
    ("MMLU", "https://en.wikipedia.org/wiki/Massive_Multitask_Language_Understanding"),
    ("BLEU", "https://en.wikipedia.org/wiki/BLEU"),
    ("ROUGE", "https://en.wikipedia.org/wiki/ROUGE_(metric)"),
    ("SWE-bench", "https://en.wikipedia.org/wiki/SWE-Bench"),

    # ---- Safety / interpretability
    ("hallucination", "https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)"),
    ("Mechanistic interpretability", "https://en.wikipedia.org/wiki/Mechanistic_interpretability"),
    ("prompt-injection", "https://en.wikipedia.org/wiki/Prompt_injection"),
    ("prompt injection", "https://en.wikipedia.org/wiki/Prompt_injection"),
    ("Algorithmic bias", "https://en.wikipedia.org/wiki/Algorithmic_bias"),
    ("AI safety", "https://en.wikipedia.org/wiki/AI_safety"),

    # ---- Synthetic data / methodology
    ("synthetic data", "https://en.wikipedia.org/wiki/Synthetic_data"),
    ("Reproducing", "https://en.wikipedia.org/wiki/Reproducibility"),
]
