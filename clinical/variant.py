class Variant:
    VARIANT_ATTRIBUTES = ['#AlleleID',
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
                   'VariationID']
    attribute_values = []
    DIAGNOSES_TO_GENE_MAPPING = {
        "Colon Cancer": ['5395'],
        "Li-Fraumeni Syndrome": ['7157'],
        "Breast Cancer": ['5892'],
        "Ovarian Cancer": ['5892'],
        "Cardiomyopathy": ["2318"],
        "Myofibrillar Myopathy": ["2318"],
        "Alzheimer's Disease": ["5664"],
    }

    gene_id = ""
    gene_name = ""
    phenotype_list = ""
    start = -1
    stop = -1
    clinical_significance = ""
    chromosome = -1
    reference_allele = ""
    alternate_allele = ""
    diagnosis = ""

    def __init__(self, attribute_string):
        self.attribute_values = attribute_string.split('\t')

        self.gene_id = self.get_gene_id()
        self.gene_name = self.get_gene_name()
        self.phenotype_list = self.get_phenotype_list()
        self.start = self.get_start_position()
        self.stop = self.get_stop_position()
        self.chromosome = self.get_chromosome()
        self.reference_allele = self.get_reference_allele()
        self.alternate_allele = self.get_alternate_allele()
        self.clinical_significance = self.get_clinical_significance()
        self.diagnosis = self.get_diagnoses()

    def __str__(self):
        output_array = []
        for i in range(len(self.VARIANT_ATTRIBUTES)):
            output_array.append(self.VARIANT_ATTRIBUTES[i] + ": " + self.attribute_values[i] + '\n')

        return ''.join(output_array)

    def return_important_attributes(self):
        IMPORTANT_ATTRIBUTE_NAMES = ["#AlleleID", "GeneID", "GeneSymbol",
                                     "ClinicalSignificance", "PhenotypeList", "Chromosome",
                                     "Start", "Stop", "ReferenceAllele",
                                     "AlternateAllele"]
        output_array = []
        for i in range(len(self.VARIANT_ATTRIBUTES)):
            if self.VARIANT_ATTRIBUTES[i] in IMPORTANT_ATTRIBUTE_NAMES:
                output_array.append(self.VARIANT_ATTRIBUTES[i] + ": " + self.attribute_values[i])
        return output_array

    def get_gene_id(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("GeneID")]

    def get_phenotype_list(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("PhenotypeList")]

    def get_start_position(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("Start")]

    def get_stop_position(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("Stop")]

    def get_chromosome(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("Chromosome")]

    def get_reference_allele(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("ReferenceAllele")]

    def get_alternate_allele(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("AlternateAllele")]

    def get_clinical_significance(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("ClinicalSignificance")]

    def get_gene_name(self):
        return self.attribute_values[self.VARIANT_ATTRIBUTES.index("GeneSymbol")]

    def get_diagnoses(self):
        for diag, gene in self.DIAGNOSES_TO_GENE_MAPPING.items():
            if self.gene_id in gene:
                return diag
        return "No diagnosis available"
