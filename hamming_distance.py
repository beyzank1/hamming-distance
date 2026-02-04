def hamming_distance_list(seq1, seq2):
    """
    Generic Hamming distance for two sequences (lists).
    Extra elements count as mismatches.
    """
    max_len = max(len(seq1), len(seq2))
    distance = 0

    for i in range(max_len):
        if i >= len(seq1) or i >= len(seq2) or seq1[i] != seq2[i]:
            distance += 1

    return distance
# PART A: WORD HAMMING DISTANCE

print("PART A: WORD HAMMING DISTANCE")

word_pairs = [
    ("potting", "putting"),
    ("banana", "bananas")
]

for word1, word2 in word_pairs:
    distance = hamming_distance_list(list(word1.lower()), list(word2.lower()))
    print(f"\n'{word1}' vs '{word2}'")
    print(f"  Hamming Distance: {distance}")

# PART B: PHRASE DISTANCE

print("PART B: PHRASE DISTANCE")

phrase_pairs = [
    ("two dogs and two cats", "two cats and two dogs"),
    ("two dogs and two cats", "three dogs and two cats")
]

for phrase1, phrase2 in phrase_pairs:
    d = hamming_distance_list(phrase1.lower().split(),phrase2.lower().split())
    print(f"\n'{phrase1}' vs '{phrase2}'")
    print(f"  Distance: {d}")

# INTERACTIVE TESTING 
print("INTERACTIVE TESTING")

if __name__ == "__main__":
    print("\nTest your own words:")
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")
    print(f"Hamming Distance: "
          f"{hamming_distance_list(list(w1.lower()), list(w2.lower()))}")
    
    print("\nTest your own phrases:")
    p1 = input("Enter first phrase: ")
    p2 = input("Enter second phrase: ")
    print(f"Phrase Distance (word-by-word): "
          f"{hamming_distance_list(p1.lower().split(), p2.lower().split())}")
