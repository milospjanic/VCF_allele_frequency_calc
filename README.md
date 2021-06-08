# VCF_allele_frequency_calc


For a test vcf of the following format, the script will output the frequency of the reference allele.

<pre>

##contig=<ID=chr2,length=243199373>
##contig=<ID=chr3,length=198022430>
##contig=<ID=chr4,length=191154276>
##contig=<ID=chr5,length=180915260>
##contig=<ID=chr6,length=171115067>
##contig=<ID=chr7,length=159138663>
##contig=<ID=chr8,length=146364022>
##contig=<ID=chr9,length=141213431>
##contig=<ID=chr10,length=135534747>
##contig=<ID=chr11,length=135006516>
##contig=<ID=chr12,length=133851895>
##contig=<ID=chr13,length=115169878>
##contig=<ID=chr14,length=107349540>
##contig=<ID=chr15,length=102531392>
##contig=<ID=chr16,length=90354753>
##contig=<ID=chr17,length=81195210>
##contig=<ID=chr18,length=78077248>
##contig=<ID=chr19,length=59128983>
##contig=<ID=chr20,length=63025520>
##contig=<ID=chr21,length=48129895>
#CHROM    POS    ID    REF    ALT    QUAL    FILTER    INFO    FORMAT    20389_S5.bam
chr1    11205058    rs1057079    T    A    100    PASS    DP=12;BC=105,96,0,1;cosmic=1|COSM4142146;EVS=0.545902|115|6503;GMAF=C|0.4525;AA=C;AF1000G=0.547524;phyloP=0.078;CSQT=1|MTOR|NM_004958.3|synonymous_variant,1|MTOR-AS1|NR_046600.1|intron_variant&non_coding_transcript_variant    GT:GQ:AD:DP:VF:NL:SB:NC    1/1:43:0,12:12:1.000:20:-100.0000:0.0000
chr1    11253467    rs28991008    A    G    100    PASS    DP=90;BC=130,0,0,86;GMAF=A|0.02516;AA=C;AF1000G=0.02516;phyloP=0.241;CSQT=1|MTOR|NM_004958.3|intron_variant,1|ANGPTL7|NM_021146.3|intron_variant    GT:GQ:AD:DP:VF:NL:SB:NC    0/1:100:38,52:90:0.578:20:-100.0000:0.0000
chr1    11288758    rs1064261    A    G    100    PASS    DP=93;BC=122,0,0,111;cosmic=1|COSM4142152;EVS=0.617561|95|6503;GMAF=G|0.2995;AA=A;AF1000G=0.700479;phyloP=-0.406;CSQT=1|MTOR|NM_004958.3|synonymous_variant    GT:GQ:AD:DP:VF:NL:SB:NC    1/1:100:0,93:93:1.000:20:-100.0000:0.0106
chr1    11297762    rs7524202    A    G    100    PASS    DP=48;BC=124,0,0,110;GMAF=T|0.2991;AA=C;AF1000G=0.700879;phyloP=-0.016;CSQT=1|MTOR|NM_004958.3|intron_variant    GT:GQ:AD:DP:VF:NL:SB:NC    1/1:100:0,48:48:1.000:20:-100.0000:0.0204

</pre>

