def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(
            f"Comparing {strand_a} with {strand_b} failed. Cannot compare strands that are not of equal length."
        )

    hamming_distance = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1

    return hamming_distance