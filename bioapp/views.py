from django.shortcuts import render
from .models import DNAAnalysis, MutationDetection, FASTAAnalysis


def gc_percent(seq):
    return round((seq.count('G') + seq.count('C')) / len(seq) * 100, 2) if seq else 0


def clean(seq):
    return ''.join(seq.upper().split())


def home(request):
    return render(request, 'bioapp/home.html')


def dna_analyzer(request):
    result, error = None, None
    if request.method == 'POST':
        seq = clean(request.POST.get('sequence', ''))
        if not seq or set(seq) - set('ATGC'):
            error = 'Please enter a valid DNA sequence (only A, T, G, C).'
        else:
            gc = gc_percent(seq)
            if gc > 60:
                interpretation = 'High GC content'
            elif gc < 40:
                interpretation = 'Low GC content'
            else:
                interpretation = 'Moderate GC content'
            comp = seq.translate(str.maketrans('ATGC', 'TACG'))
            result = {
                'sequence': seq,
                'length': len(seq),
                'gc_content': gc,
                'a': seq.count('A'), 't': seq.count('T'),
                'g': seq.count('G'), 'c': seq.count('C'),
                'complement': comp,
                'reverse_complement': comp[::-1],
                'rna': seq.replace('T', 'U'),
                'interpretation': interpretation,
            }
            DNAAnalysis.objects.create(
                sequence=seq, length=len(seq),
                gc_content=gc, interpretation=interpretation)
    return render(request, 'bioapp/dna_analyzer.html',
                  {'result': result, 'error': error})


def mutation_detector(request):
    result, error = None, None
    if request.method == 'POST':
        s1 = clean(request.POST.get('sequence1', ''))
        s2 = clean(request.POST.get('sequence2', ''))
        if not s1 or not s2:
            error = 'Please enter both sequences.'
        else:
            n = min(len(s1), len(s2))
            purines, pyrimidines = set('AG'), set('CT')
            snps, ts, tv = [], 0, 0
            for i in range(n):
                if s1[i] != s2[i]:
                    pair = {s1[i], s2[i]}
                    if pair <= purines or pair <= pyrimidines:
                        snp_type = 'Transition'
                        ts += 1
                    else:
                        snp_type = 'Transversion'
                        tv += 1
                    snps.append({
                        'position': i + 1,
                        'original': s1[i],
                        'mutated': s2[i],
                        'type': snp_type,
                    })
            total = len(snps)
            rate = round(total / n * 100, 2)
            sim = round(100 - rate, 2)
            result = {
                'snps': snps,
                'total_snps': total,
                'transitions': ts,
                'transversions': tv,
                'mutation_rate': rate,
                'similarity': sim,
            }
            MutationDetection.objects.create(
                total_snps=total, transitions=ts, transversions=tv,
                mutation_rate=rate, similarity=sim)
    return render(request, 'bioapp/mutation_detector.html',
                  {'result': result, 'error': error})


def fasta_analyzer(request):
    result, error = None, None
    if request.method == 'POST':
        text = request.POST.get('fasta_text', '').strip()
        records, header, seq = [], None, []
        for line in text.splitlines():
            line = line.strip()
            if line.startswith('>'):
                if header is not None:
                    records.append((header, ''.join(seq).upper()))
                header, seq = line[1:], []
            elif line:
                seq.append(line)
        if header is not None:
            records.append((header, ''.join(seq).upper()))

        if not records:
            error = 'No valid FASTA sequences found. Each sequence must start with ">".'
        else:
            seqs = []
            for h, s in records:
                seqs.append({
                    'header': h, 'length': len(s), 'gc': gc_percent(s),
                    'a': s.count('A'), 't': s.count('T'),
                    'g': s.count('G'), 'c': s.count('C'),
                })
            total_bases = sum(x['length'] for x in seqs)
            avg_gc = round(sum(x['gc'] for x in seqs) / len(seqs), 2)
            result = {'total': len(seqs), 'total_bases': total_bases,
                      'avg_gc': avg_gc, 'sequences': seqs}
            FASTAAnalysis.objects.create(
                total_sequences=len(seqs), total_bases=total_bases, avg_gc=avg_gc)
    return render(request, 'bioapp/fasta_analyzer.html',
                  {'result': result, 'error': error})


def history(request):
    return render(request, 'bioapp/history.html', {
        'dna_analyses': DNAAnalysis.objects.order_by('-created_at'),
        'mutations': MutationDetection.objects.order_by('-created_at'),
        'fasta_analyses': FASTAAnalysis.objects.order_by('-created_at'),
    })