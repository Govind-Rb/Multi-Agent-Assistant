class ReviewerAgent:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def review(self, response):
        final_response = f"Final Answer: {response}"

        return final_response


# Later we can make the reviewer use the LLM to check correctness and quality.