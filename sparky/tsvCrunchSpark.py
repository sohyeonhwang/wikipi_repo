import sys
from pyspark import SparkConf
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql import Window
import pyspark.sql.functions as f
from pyspark.sql import types
import pandas as pd
import argparse
import glob, os, re
import csv
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Create a dataset.')
    parser.add_argument('-i', '--input', help='Path for directory of wikiq tsv outputs', required=True, type=str)
    parser.add_argument('--lang', help='Specify which language edition', default='es',type=str)
    parser.add_argument('-o', '--output-dir', help='Output directory', default='./tsvCrunchOutput', type=str)
    parser.add_argument('--num-partitions', help = "number of partitions to output",type=int, default=1)
    args = parser.parse_args()
    return(args)

def coreColumns(onlyRegexCols):
    #CORE COLUMNS
    #ENGLISH:
    #SPANISH:	53_WIKIPEDIA:PUNTO_DE_VISTA_NEUTRAL, 69_WIKIPEDIA:WIKIPEDIA_NO_ES_UNA_FUENTE_PRIMARIA, 64_WIKIPEDIA:VERIFICABILIDAD
    #FRENCH: 	26_WIKIPÉDIA:NEUTRALITÉ_DE_POINT_DE_VUE, 19_WIKIPÉDIA:TRAVAUX_INÉDITS, 21_WIKIPÉDIA:VÉRIFIABILITÉ
    #GERMAN:
    #JAPANESE:	14_WIKIPEDIA:中立的な観点,16_WIKIPEDIA:独自研究は載せない, 15_WIKIPEDIA:検証可能性
    
    if "53_WIKIPEDIA:PUNTO_DE_VISTA_NEUTRAL" in onlyRegexCols:
        coreDFColumn = [c for c in onlyRegexCols if (c[:2]==str(53) or c[:2]==str(69) or c[:2]==str(64))]
    elif "26_WIKIPÉDIA:NEUTRALITÉ_DE_POINT_DE_VUE" in onlyRegexCols:
        coreDFColumn = [c for c in onlyRegexCols if (c[:2]==str(26) or c[:2]==str(19) or c[:2]==str(21))]
    else:
        coreDFColumn = [c for c in onlyRegexCols if (c[:2]==str(14) or c[:2]==str(15) or c[:2]==str(16))]

    return coreDFColumn

def cumulMonthly(regex_df):
    onlyRegexCols = [c for c in regex_df.columns if c[0].isdigit()]
    coreDFColumn = coreColumns(onlyRegexCols)

    monthly_regex_df = regex_df.select(regex_df.revid, f.concat_ws('_',f.year(regex_df.date_time),f.month(regex_df.date_time)).alias('year_month'),f.concat_ws(', ',*coreDFColumn).alias('core_regex'))
    monthly_regex_df = monthly_regex_df.na.replace('',None)
    monthly_regex_df = monthly_regex_df.select(*monthly_regex_df,f.when(monthly_regex_df.core_regex.isNotNull(),1).otherwise(0).alias('core_policy_invoked'))

    monthly_core_count_df = monthly_regex_df.groupBy('year_month').sum('core_policy_invoked')
    monthly_revn_count_df = monthly_regex_df.groupBy('year_month').count()

    monthly_joined_df = monthly_revn_count_df.join(monthly_core_count_df, on=['year_month'],how='left')

    return monthly_joined_df

def df_diff(input_df):
    # input_df should be regex_df in df_structurize
    regex_diff_df = input_df.orderBy("articleid")

    # 
    # year_month, {'ABC':0,'XYZ':3, ...} <-- a dictionary of counts

    # make an ordered list of year_month

    # iterate through the list and compare the dictionaries, get the diff

    # get the difference (diff_df) by month for each article

    # return a regex_diff_df that has the article_id, year_month, 

    return regex_diff_df.show()

def df_structurize(input_df, struct):
    # metadata columns
    metaColumns = struct.fieldNames()
    meta_df = input_df.select(*metaColumns)
    #meta_df.orderBy("articleid").show()

    # dataframe of the regex columns
    regexDFColumns = [c for c in input_df.columns if c[0].isdigit()]
    regexDFColumns.append("revid")
    regexDFColumns.append("date_time")
    regexDFColumns.append("articleid")
    regex_df = input_df.na.replace('None',None).select(*regexDFColumns)
    #regex_df.show(vertical=True)

    # combine the regex columns into one column, if not None/null
    # this has: revid, article_id, date/time, regexes
    #onlyRegexCols = [c for c in regex_df.columns if c[0].isdigit()]
    #regexes_revid_df = regex_df.select(regex_df.revid,regex_df.articleid, regex_df.date_time,f.concat_ws(', ',*onlyRegexCols).alias("REGEXES"))
    #regexes_revid_df.show(vertical=True)

    return meta_df, regex_df

def sparkit(wikiqtsv):
    # make wikiq tsv into a dataframe
    tsv2df = reader.csv(wikiqtsv,
                        sep="\t",
                        inferSchema=False,
                        header=True,
                        mode="PERMISSIVE")
    tsv2df = tsv2df.repartition(args.num_partitions)

    # basic structure
    struct = types.StructType().add("anon",types.StringType(),True)
    struct = struct.add("articleid",types.LongType(),True)
    struct = struct.add("date_time",types.TimestampType(), True)
    struct = struct.add("deleted",types.BooleanType(), True)
    struct = struct.add("editor",types.StringType(),True)
    struct = struct.add("editor_id",types.LongType(), True)
    struct = struct.add("minor", types.BooleanType(), True)
    struct = struct.add("namespace", types.LongType(), True)
    struct = struct.add("revert", types.BooleanType(), True)
    struct = struct.add("reverteds", types.StringType(), True)
    struct = struct.add("revid", types.LongType(), True)
    struct = struct.add("sha1", types.StringType(), True)
    struct = struct.add("text_chars", types.LongType(), True)
    struct = struct.add("title",types.StringType(), True)

    # structure the df to get the def with columns of metadata and regexes
    meta_df, regex_df = df_structurize(tsv2df,struct)

    cumul_month = cumulMonthly(regex_df)
    #cumul_month.orderBy(cumul_month.year_month).show()

    return cumul_month


if __name__ == "__main__":
    args = parse_args()
    conf = SparkConf().setAppName("Wiki Regex Spark to monthly")
    spark = SparkSession.builder.getOrCreate()
    reader = spark.read

    files = glob.glob(args.input)
    files = [os.path.abspath(p) for p in files]
    print(files)

    sample = ['eswiki_baby.tsv']

    monthly_dfs = []

    for f in sample:
        print(f)
        cumulMonthly = sparkit(f)
        print(type(cumulMonthly))

        print("\n\n======================================================================================================\n\n")

        #monthly_dfs.append(cumulMonthly)
        cumulMonthlyPandas = cumulMonthly.toPandas()
        print(type(cumulMonthlyPandas))
        cumulMonthlyPandas.head()




