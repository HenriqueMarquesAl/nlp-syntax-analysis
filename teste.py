print("🔥 INICIOU")

import spacy

print("✅ spaCy carregado")

nlp = spacy.load("pt_core_news_sm")

print("✅ modelo carregado")

frase = "O analista de PCP quebrou um galho para o desenvolvedor."

doc = nlp(frase)

print("TOKEN | POS | DEP | HEAD")
print("-" * 40)

for token in doc:
    print(token.text, "|", token.pos_, "|", token.dep_, "|", token.head.text)

print("🔥 FIM")