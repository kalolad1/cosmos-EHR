# This script will parse through a variant.txt file and create Variant objects. It
# should be used only when the variant.txt experiences an update and then it should
# be used on the new additions, only.
import os.path
from clinical.models import Variant

# Constants
# These variables hold path constants.
VARIANT_TEXT_FILE_PATH = 'static/variant_samples/variant_samples.txt'
BASE = os.path.dirname(os.path.abspath(__file__))

# An array with all of the attributes for a Variant.
VARIANT_ATTRIBUTES = [
    '#AlleleID',
    'Type',
    'Name',
    'GeneID',
    'GeneSymbol',
    'HGNC_ID',
    'ClinicalSignificance',
    'ClinSigSimple',
    'LastEvaluated',
    'RS# (dbSNP)',
    'nsv/esv (dbVar)',
    'RCVaccession',
    'PhenotypeIDS',
    'PhenotypeList',
    'Origin',
    'OriginSimple',
    'Assembly',
    'ChromosomeAccession',
    'Chromosome',
    'Start',
    'Stop',
    'ReferenceAllele',
    'AlternateAllele',
    'Cytogenetic',
    'ReviewStatus',
    'NumberSubmitters',
    'Guidelines',
    'TestedInGTR',
    'OtherIDs',
    'SubmitterCategories',
    'VariationID'
]


def store_all_variant_samples():
    """
    This function stores all variants in a text file as variant objects.
    """
    file = open(os.path.join(BASE, VARIANT_TEXT_FILE_PATH), 'r')

    for line in file:
        # Creates an array out of a tab-separated row of information.
        variant_row = line.split('\t')

        # Creates a new Variant object and updates all of its important fields.
        new_variant = Variant()
        new_variant.gene_id = variant_row[VARIANT_ATTRIBUTES.index('GeneID')]
        new_variant.gene_name = variant_row[VARIANT_ATTRIBUTES.index('GeneSymbol')]
        new_variant.phenotype_list = variant_row[VARIANT_ATTRIBUTES.index('PhenotypeList')]
        new_variant.start = variant_row[VARIANT_ATTRIBUTES.index('Start')]
        new_variant.stop = variant_row[VARIANT_ATTRIBUTES.index('Stop')]
        new_variant.chromosome = variant_row[VARIANT_ATTRIBUTES.index('Chromosome')]
        new_variant.clinical_significance = variant_row[VARIANT_ATTRIBUTES.index('ClinicalSignificance')]
        new_variant.reference_allele = variant_row[VARIANT_ATTRIBUTES.index('ReferenceAllele')]
        new_variant.alternate_allele = variant_row[VARIANT_ATTRIBUTES.index('AlternateAllele')]

        # Saves the object in the database.
        new_variant.save()
