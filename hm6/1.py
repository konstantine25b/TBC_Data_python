from pyspark.sql import SparkSession
from collections import defaultdict
# jer ganvsazgvrit fasta  da headlinebi gavfiltrot
spark = SparkSession.builder.appName("GenomeProcessing").getOrCreate()
rdd = spark.sparkContext.textFile("s3a://retail-employees/data/final_genome.fasta")
sequence_rdd = rdd.filter(lambda line: not line.startswith('>')).flatMap(lambda line: list(line.strip()))
sequence = sequence_rdd.collect()
stage1_results = []
positions_dict = defaultdict(list)

# exa aq vqmnit lists 
for i, ch in enumerate(sequence):
    positions_dict[ch].append(i)
for i, ch in enumerate(sequence):
    p = positions_dict[ch]
    j = p.index(i)
    if j < len(p) - 1:
        nxt = p[j + 1]
        d = nxt - i - 1
        direction = "R"
        c = len(set(sequence[i+1:nxt]))
    else:
        d = 0
        direction = "N"
        c = 0
    stage1_results.append((ch, (i, d, direction, c)))
    
# aq vaketebt paralelurad gashvebas
stage1_rdd = spark.sparkContext.parallelize(stage1_results)

def max_key_distance(x):
    return x[1][1]
def max_key_combo(x):
    return x[1][1] + x[1][3]
def compute_max_per_char(rdd, key_selector):
    g = rdd.groupBy(lambda x: x[0])
    return g.mapValues(lambda vals: max(vals, key=key_selector))

max_distances = compute_max_per_char(stage1_rdd, max_key_distance).collect()
max_combo = compute_max_per_char(stage1_rdd, max_key_combo).collect()

# aq vitvlit unique valuebs
stage3_rdd = stage1_rdd.map(lambda x: (x[0], (x[1][1], x[1][2], x[1][3])))
counts = stage3_rdd.countByValue()
stage3_df = stage3_rdd.toDF(["char", "rest"]).groupBy("char", "rest").count().orderBy("count", ascending=False)
stage3_df.show()
spark.stop()
