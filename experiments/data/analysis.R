# From http://www.astatsa.com/KruskalWallisTest/
# ----------------------------------------------
# The Kruskal-Wallis test is built-into the base R. 
#
# The post-hoc tests require one-time installation of the R package PMCMR 
# Start R under "Run as Administrator" in Windows or sudo in Linux or OSX.
# select a download mirror at the install.packages command 
# install.packages("PMCMR")
library("PMCMR")

cat ("--------------------------------------------------\n")
cat ("C0: condition = 0: Control / Saline / 10 firsts\n")
cat ("C1: condition = 1: Control / Saline / 10 lasts\n")
cat ("C2: condition = 2: Day 1 / Muscimol / 10 firsts\n")
cat ("C3: condition = 3: Day 1 / Muscimol / 10 lasts\n")
cat ("C4: condition = 4: Day 2 / Saline / 10 firsts\n")
cat ("C5: condition = 5: Day 2 / Saline / 10 lasts\n")
cat ("--------------------------------------------------\n")

cat ("Experimental results\n")
cat ("--------------------------------------------------\n")

data = read.table("experimental-raw-data.txt",
                  col.names=c("performance", "session_id", "condition"))
          
P = as.vector(t(data["performance"]))
C = as.factor(as.vector(t(data["condition"])))
k1 <- kruskal.test( P, C ) 
print (k1) 
# Post-hoc tests are conducted only if omnibus Kruskal-Wallis test p-value is 0.01 or less.
if ( k1$p.value < 0.01 ) 
{ 
  d2 <- posthoc.kruskal.dunn.test(P, C, p.adjust.method="fdr")
  summary(d2)
} 

cat ("\n")
cat ("Theroretical results\n")
cat ("--------------------------------------------------\n")

data = read.table("theoretical-raw-data.txt",
                  col.names=c("performance", "session_id", "condition"))

P = as.vector(t(data["performance"]))
C = as.factor(as.vector(t(data["condition"])))
k1 <- kruskal.test( P, C ) 
print (k1) 
# Post-hoc tests are conducted only if omnimus Kruskal-Wallis test p-value is 0.01 or less.
if ( k1$p.value < 0.01 ) 
{ 
  d2 <- posthoc.kruskal.dunn.test(P, C, p.adjust.method="fdr")
  summary(d2)
} 

