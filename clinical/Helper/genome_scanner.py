# This module supports scanning for SNPs in a genome.
import os.path
from Bio import SeqIO


GENOME_DIRECTORY_PATH = 'static/genome/'
BASE = '/Users/darshankalola/Desktop/cosmosEHR-project'
CHROMOSOME_LEVEL_FILE_HEADER = 'chr'
CHROMOSOME_LEVEL_FILE_EXTENSION = '.fa'
PROXIMATE_SEQUENCE_LENGTH = 10


class GenomeScanner:
    nucleotide_at_position = ''
    proximate_sequence_front = ''
    proximate_sequence_back = ''
    proximate_sequence = ''
    snp_exists = False

    def __init__(self, variant_to_scan):
        self.scan_for_snp(variant_to_scan)

    def scan_for_snp(self, variant_to_scan):
        path_components = [BASE, GENOME_DIRECTORY_PATH,
                           CHROMOSOME_LEVEL_FILE_HEADER +
                           str(variant_to_scan.chromosome) +
                           CHROMOSOME_LEVEL_FILE_EXTENSION]

        file = os.path.join('', *path_components)

        with open(file, "r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                if len(record) <= variant_to_scan.start <= 0:
                    raise Exception("Position of nucleotide is out of bounds.")

                lower_cutoff = variant_to_scan.start - 1 - PROXIMATE_SEQUENCE_LENGTH
                upper_cutoff = variant_to_scan.start - 1 + PROXIMATE_SEQUENCE_LENGTH
                if upper_cutoff >= len(record):
                    upper_cutoff = len(record)

                if lower_cutoff <= 0:
                    lower_cutoff = 0

                self.nucleotide_at_position = record[variant_to_scan.start - 1]
                self.proximate_sequence_front = record[lower_cutoff:variant_to_scan.start-1].seq
                self.proximate_sequence_back = record[variant_to_scan.start:upper_cutoff + 1].seq

                self.proximate_sequence = record[lower_cutoff:upper_cutoff + 1].seq
                self.snp_exists = variant_to_scan.alternate_allele == self.nucleotide_at_position.upper()







