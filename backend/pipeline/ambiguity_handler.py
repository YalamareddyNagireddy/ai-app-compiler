class AmbiguityHandler:
    def check(self, prompt: str):
        prompt = prompt.lower().strip()

        words = prompt.split()

        # ✅ Case 1: too short
        if len(words) < 4:
            return {
                "is_ambiguous": True,
                "questions": [
                    "Can you describe your idea in more detail?"
                ]
            }

        # ❌ ONLY treat as vague if VERY generic ONLY
        generic_prompts = [
            "build app",
            "make app",
            "create app",
            "build system",
            "make system",
            "create system"
        ]

        for gp in generic_prompts:
            if prompt == gp:
                return {
                    "is_ambiguous": True,
                    "questions": [
                        "What exactly do you want to build?",
                        "Who will use it?",
                        "What features should it have?"
                    ]
                }

        # ✅ Otherwise treat as valid
        return {
            "is_ambiguous": False
        }