from django.shortcuts import render
from clinical import calculations

"""
Home page view.
"""
def clinicaltools(request):
    return render(request, 'clinical/clinicaltools.html')


"""
Patient view
"""
def patient(request):
    return render(request, 'clinical/patient.html')


"""
Entry view
"""
def entry(request):
    return render(request, 'clinical/entry.html')


"""
Processing view
"""
def processing(request):
    # Retrieve input
    if request.method == 'POST':
        d_list = request.POST.get("d_list")

        variants = calculations.get_variant_samples_based_on_d_list(d_list)
        print(variants)

        return render(request, 'clinical/processing.html', {'variants': variants})
    else:
        return render(request, '')


def scan(request, chrom, pos, ref, alt):
    snp_exists, proximate_sequence, snp_nuc = calculations.snp_exists_at(chrom, pos, ref, alt)

    print(snp_exists)
    print(snp_nuc)

    proximate_sequence = proximate_sequence.upper()
    spaced_seq = [proximate_sequence[i:i + 10] for i in range(0, len(proximate_sequence), 10)]
    proximate_sequence = '  '.join(spaced_seq)

    return render(request, 'clinical/scan.html', {'snp_exists': snp_exists,
                                                  "proximate_sequence": proximate_sequence,
                                                  "snp_nuc": snp_nuc,
                                                  "alt": alt})




