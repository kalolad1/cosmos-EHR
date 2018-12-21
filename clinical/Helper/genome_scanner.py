# This module contains a helper class for scanning for SNPs in a genome.
import os.path
from Bio import SeqIO

# Constants
# Where the genome is kept.
GENOME_DIRECTORY_PATH = 'static/genome/'

# Base path of the project
BASE = '/Users/darshankalola/Desktop/cosmosEHR-project'

# Naming scheme of the chromosome level files.
CHROMOSOME_LEVEL_FILE_HEADER = 'chr'
CHROMOSOME_LEVEL_FILE_EXTENSION = '.fa'

# This variable stores how long of a proximate sequence should be sent to the user. 10 is default.
PROXIMATE_SEQUENCE_LENGTH = 10


class GenomeScanner:
    # This variable stores the ground truth nucleotide at the variant site location.
    nucleotide_at_position = ''

    # This is the sequence which comes before the variant site.
    proximate_sequence_front = ''

    # This is the sequence which comes after the variant site.
    proximate_sequence_back = ''

    # This is the front and back sequence concatenated together with the relevant nucleotide.
    proximate_sequence = ''

    # This is a boolean of whether an SNP (Single Nucleotide Polymorphism) exists at the variant site.
    # It is set False by default.
    snp_exists = False

    # A GenomeScanner class takes in a Variant object.
    def __init__(self, variant_to_scan):
        self.scan_for_snp(variant_to_scan)

    def scan_for_snp(self, variant_to_scan):
        """
        This function scans a chromosome file to check for a SNP.

        Params:
            variant_to_scan: A Variant object that is checked against the genome.

        Returns:
             Nothing, however, it updates five of the above class fields.
        """
        # Generates the path needed to reach the correct chromosome level file.
        path_components = [BASE, GENOME_DIRECTORY_PATH,
                           CHROMOSOME_LEVEL_FILE_HEADER +
                           str(variant_to_scan.chromosome) +
                           CHROMOSOME_LEVEL_FILE_EXTENSION]

        file = os.path.join('', *path_components)
        with open(file, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                # Checks to see if the variant position is out of bounds.
                if len(record) <= variant_to_scan.start <= 0:
                    raise Exception("Position of nucleotide is out of bounds.")

                # Calculates lower and upper cutoffs to generate the proximate sequence.
                lower_cutoff = variant_to_scan.start - 1 - PROXIMATE_SEQUENCE_LENGTH
                upper_cutoff = variant_to_scan.start - 1 + PROXIMATE_SEQUENCE_LENGTH
                if upper_cutoff >= len(record):
                    upper_cutoff = len(record)

                if lower_cutoff <= 0:
                    lower_cutoff = 0

                # Updates all of the class fields with results from the scan.
                self.nucleotide_at_position = record[variant_to_scan.start - 1]
                self.proximate_sequence_front = record[lower_cutoff:variant_to_scan.start-1].seq
                self.proximate_sequence_back = record[variant_to_scan.start:upper_cutoff + 1].seq
                self.proximate_sequence = record[lower_cutoff:upper_cutoff + 1].seq
                self.snp_exists = variant_to_scan.alternate_allele == self.nucleotide_at_position.upper()
