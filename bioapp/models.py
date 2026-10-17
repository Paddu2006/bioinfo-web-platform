from django.db import models


class DNAAnalysis(models.Model):
    sequence = models.TextField()
    length = models.IntegerField()
    gc_content = models.FloatField()
    interpretation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DNA Analysis {self.id}"


class MutationDetection(models.Model):
    total_snps = models.IntegerField()
    transitions = models.IntegerField()
    transversions = models.IntegerField()
    mutation_rate = models.FloatField()
    similarity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mutation Detection {self.id}"


class FASTAAnalysis(models.Model):
    total_sequences = models.IntegerField()
    total_bases = models.IntegerField()
    avg_gc = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FASTA Analysis {self.id}"