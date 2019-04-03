#!/usr/local/bin/python3
import collections
import math
import plotly


def from_rsem_ebseq():
    for treatment_name in treatments:
        samples = collections.defaultdict(set)
        for sample_id in treatments[treatment_name]:
            with open(treatments_dir + sample_id + calc_expr_extension, 'r') as calc_expr_file:
                for line in calc_expr_file:
                    line_split = line.split()
                    transcript_id = line_split[0]
                    tpm = line_split[5]
                    fpkm = line_split[6]
                    samples[sample_id].add(TranscriptExression(transcript_id, tpm, fpkm))

        treatment = Treatment(treatment_name, samples)



class ExpressionAnalysis(object):
    def __init__(self, treatments, ebseq_runs, treatments_dir, ebseq_dir, calc_expr_extension):
        self.treatments = collections.defaultdict
        self.ebseq_analyses =


class Treatment(object):  # rsem-calculate-expression output
    def __init__(self, name, samples):
        self.name = name
        self.samples = samples


class TranscriptExression(object):
    def __init__(self, id, tpm, fpkm):
        self.id = id
        self.tpm = tpm
        self.fpkm = fpkm


class EbseqAnalysis(object):  # rsem-run-ebseq output
    def __init__(self, transcript_comparisons, condition1, condition2):
        self.transcript_comparisons = transcript_comparisons
        self.condition1 = condition1
        self.condition2 = condition2

    def __iter__(self):
        return iter(self.transcript_comparisons.values())

    @property
    def diff_expressed(self):
        return [transcript for transcript in self if transcript.diff_expressed]

    @property
    def equal_expressed(self):
        return [transcript for transcript in self if transcript.equal_expressed]

    def graph_c2_vs_c1(self):
        plotly.offline.plot(plotly.graph_objs.Figure(data=[plotly.graph_objs.Scatter(x=[transcript.c1mean for transcript in self.equal_expressed], y=[transcript.c2mean for transcript in self.equal_expressed], mode='markers', name='equally_expressed', opacity=0.75),
                                                           plotly.graph_objs.Scatter(x=[transcript.c1mean for transcript in self.diff_expressed], y=[transcript.c2mean for transcript in self.diff_expressed], mode='markers', name="differentially_expressed", opacity=0.75)],
                                                     layout=plotly.graph_objs.Layout(title=('EBseq Analysis for ' + self.condition2 + ' vs ' + self.condition1), xaxis=dict(title=self.condition1), yaxis=dict(title=self.condition2))),
                            filename=self.condition2 + '_vs_' + self.condition1 + '.html')


class TranscriptComparison(object):
    significance_threshold = 0.95

    def __init__(self, id, ppee, ppde, postfc, realfc, c1mean, c2mean):
        """
        Manage transcript in an expression analysis.
        :param id: transcript/gene id
        :param ppee: posterior probability of equal expression
        :param ppde: posterior probability of differential expression
        :param postfc: post fold change
        :param realfc: real fold change
        :param c1mean: condition 1 mean
        :param c2mean: condition 2 mean
        """
        self.id = id
        self.ppee = float(ppee)
        self.ppde = float(ppde)
        self.postfc = float(postfc)
        self.realfc = float(realfc)
        self.c1mean = float(c1mean)
        self.c2mean = float(c2mean)

    @property
    def log2_postfc(self):
        return math.log(self.postfc, 2)

    @property
    def diff_expressed(self):
        return self.ppde >= TranscriptComparison.significance_threshold

    @property
    def equal_expressed(self):
        return self.ppee >= TranscriptComparison.significance_threshold
