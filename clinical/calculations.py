from clinical.variant import Variant
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))

DIAGNOSES_TO_GENE_MAPPING = {
    "Colon Cancer": ['5395'],
    "Li-Fraumeni Syndrome": ['7157'],
    "Breast Cancer": ['5892'],
    "Cardiomyopathy": ["2318"],
    "Alzheimer's Disease": ["5664"],
}


def retrieve_all_variant_samples():
    file = open(os.path.join(BASE, "variant_samples/variant_samples.txt"), "r")

    all_variants = []
    for line in file:
        var = Variant(line)
        all_variants.append(var)
    return all_variants


def get_gene_ids(d_list):
    d_list_array = d_list.split(', ')

    relevant_genes = []
    for each in d_list_array:
        if each in DIAGNOSES_TO_GENE_MAPPING:
            relevant_genes.extend(DIAGNOSES_TO_GENE_MAPPING[each])

    return relevant_genes


def get_relevant_variants(gene_ids, all_variants):
    relevant_variants = []
    all_gene_ids = {}

    for each in all_variants:
        all_gene_ids[each.get_gene_id()] = each

    for entered_gene in gene_ids:
        if entered_gene in all_gene_ids:
            relevant_variants.append(all_gene_ids[entered_gene])

    return relevant_variants


def get_variant_samples_based_on_d_list(d_list):
    all_variants = retrieve_all_variant_samples()
    gene_ids = get_gene_ids(d_list)

    relevant_variants = get_relevant_variants(gene_ids, all_variants)
    return relevant_variants


def snp_exists_at(chrom, pos, ref, alt):
    # Open correct file
    file_name = "genome/chr" + str(chrom) + ".fa"
    file = open(os.path.join(BASE, file_name), "r")

    chrom_array = []
    with file as f:
        next(f)
        count = 0
        for line in f:
            if count > pos:
                break
            for each in line:
                count += 1
                if count % 1000000 == 0:
                    print(count)

                chrom_array.append(each)

    return is_mutation(chrom_array[pos], ref, alt), ''.join(chrom_array[pos-20:pos+20]), chrom_array[pos]


def is_mutation(nucleotide, ref, alt):
    if nucleotide == ref:
        return False
    elif nucleotide == alt:
        return True
    else:
        return False













