# import argparse
import os
import csv
# import sys

result_map = {}
rs_set = set()

for filename in os.listdir(
    os.path.join(
        os.getcwd(),
        "tina_vcf")):
    if not filename.endswith(".vcf"):
        continue
    filepath = os.path.join(
        os.getcwd(),
        "tina_vcf",
        filename)

    # filepath

    with open(filepath, 'r') as f:
        summary = {}
        while not f.readline().startswith('#CHROM'):
            pass
        for line in f:
            # line
            line = line.strip()
            items = line.split('\t')
            rs_id = items[2]

            # rs_id

            BC_cell = items[7]

            # BC_cell


            BC = BC_cell.split(';')[1]
            REF = items[3]
            Freq = BC.split('=')[1]
            A = Freq.split(',')[0]
            T = Freq.split(',')[1]
            C = Freq.split(',')[2]
            G = Freq.split(',')[3]
            Total = [A, T, C, G]


            # Ref ratio

            if REF == "A":
                REFNUM = int(A)
            elif REF == "T":
                REFNUM = int(T)
            elif REF == "C":
                REFNUM = int(C)
            elif REF == "G":
                REFNUM = int(G)

            # SUM a,t,c,g

            SUM = int(A) + int(T) + int(C) + int(G)

            #print ("Reference frequency:", round(REFNUM/SUM,2))

            REFFREQ=round(REFNUM/SUM,2)

            rs_set.add(REFFREQ)
            summary[rs_id]=REFFREQ


#print (summary)

summary_file = os.path.join(os.getcwd(), "tina.output")

w = csv.writer(open(summary_file, "w"))
for key, val in summary.items():
    w.writerow([key, val])
