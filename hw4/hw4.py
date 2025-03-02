from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("GenomeProcessing") \
    .getOrCreate()

rdd = spark.sparkContext.textFile("s3a://retail-employees/data/final_genome.fasta")
sequences = rdd.filter(lambda x: not x.startswith('>') and x.strip() != '')

def consecutive_groups(seq):
    if not seq:
        return []
    groups = []
    ch = seq[0]
    count = 1
    for c in seq[1:]:
        if c == ch:
            count += 1
        else:
            if count >= 2:
                groups.append(ch * count)
            ch = c
            count = 1
    if count >= 2:
        groups.append(ch * count)
    return groups

def no_repeats(seq):
    for i in range(len(seq) - 1):
        if seq[i] == seq[i+1]:
            return False
    return True

group_counts = sequences.flatMap(consecutive_groups) \
    .map(lambda g: (g, 1)) \
    .reduceByKey(lambda a, b: a + b)

non_repeating = sequences.filter(no_repeats).map(lambda s: (s, 1))

result_groups = group_counts.collect()
result_non_repeating = non_repeating.collect()

print(result_groups)
print(result_non_repeating)

spark.stop()
