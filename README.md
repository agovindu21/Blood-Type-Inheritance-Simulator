# Blood Type Inheritance Simulator

# Background
A person’s blood type is determined by two alleles. The three possible alleles are A, B, and O, of which each person has two (possibly the same, possibly different). Each of a child’s parents randomly passes one of their two blood type alleles to their child. The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA, and BB.

For example, if one parent has blood type AO and the other parent has blood type BB, then the child’s possible blood types would be AB and OB, depending on which allele is received from each parent. Similarly, if one parent has blood type AO and the other OB, then the child’s possible blood types would be AO, OB, AB, and OO.

# Specification
This Python program allows users to simulate the blood types for n generations of individuals, by creating a family of a specified generation size and assigning blood type alleles to each family member based on their parents. The oldest generation's blood types are randomly generated, which each subsequent generation having a random combination of their parents' alleles.

# Usage
In the command line type: "python inheritance.py number_of_generations"
- "number_of_generations" is the integer number of generations you want to simulate
- improper command-line usage will produce this reminder: "Usage: python inheritance.py <number_of_generations>"
