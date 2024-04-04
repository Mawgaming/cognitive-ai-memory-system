import spacy

class EthicalCompass:
    def __init__(self, principles, nlp_tool=None):
        self.principles = principles
        self.nlp_tool = nlp_tool or spacy.load("en_core_web_lg")

    def analyze(self, themes, threshold=0.7):
        ethical_lessons = []
        for theme in themes:
            theme_doc = self.nlp_tool(theme)
            for principle in self.principles:
                principle_doc = self.nlp_tool(principle)
                score = theme_doc.similarity(principle_doc)
                if score > threshold:
                    ethical_lessons.append(f"{theme} aligns with {principle} with similarity {score:.2f}")
        return ethical_lessons

