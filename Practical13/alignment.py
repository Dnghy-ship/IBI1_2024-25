#alignment
# Read and store sequences from FASTA files
def read_fasta(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Skip the header (first line) and join the remaining lines into a single sequence
        sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
    return sequence

# Parse the BLOSUM62 matrix (Copilot)
def parse_blosum62(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        amino_acids = lines[0].strip().split()  # First line contains amino acid labels
        blosum62 = {}
        for i, line in enumerate(lines[1:]):
            scores = line.strip().split()
            row_aa = scores[0]  # First column is the amino acid
            blosum62[row_aa] = {amino_acids[j]: int(scores[j + 1]) for j in range(len(amino_acids))}
    return blosum62

# Read sequences
seq1 = read_fasta("P04179.fasta.txt")
seq2 = read_fasta("P09671.fasta.txt")
seq3 = read_fasta("Random.fasta.txt")

blosum62=parse_blosum62("BLOSUM62.txt")

# Calculate alignment score using BLOSUM62
def get_alignment_score(seq1, seq2):
    alignment_score = 0
    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]
        alignment_score += blosum62[aa1][aa2]  # Add the score from the matrix
    return alignment_score

# Calculate percentage of identical amino acids
def calculate_identity_percentage(seq1, seq2):
    identical_count = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:  # Check if amino acids are identical
            identical_count += 1
    identity_percentage = (identical_count / len(seq1)) * 100  # Calculate percentage
    return identity_percentage

# Calculate the alignment scores
alignment_score1=get_alignment_score(seq1,seq2)
alignment_score2=get_alignment_score(seq1,seq3)
alignment_score3=get_alignment_score(seq2,seq3)
# Calculate identity percentages for the sequences
identity_percentage1 = calculate_identity_percentage(seq1, seq2)
identity_percentage2 = calculate_identity_percentage(seq1, seq3)
identity_percentage3 = calculate_identity_percentage(seq2, seq3)

print("Alignment score (Human and Mouse): ", alignment_score1)
print("Identity percentage (Human and Mouse): {:.2f}%".format(identity_percentage1))
print("Alignment score (Human and Random): ", alignment_score2)
print("Identity percentage (Human and Random): {:.2f}%".format(identity_percentage2))
print("Alignment score (Mouse and Random): ", alignment_score3)
print("Identity percentage (Mouse and Random): {:.2f}%".format(identity_percentage3))

#Statement: The most closely related sequences are human and mouse SOD2 proteins